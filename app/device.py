from sanic import Blueprint, response
from sanic.views import HTTPMethodView
import qrcode
from .model import Device, History, db


bp = Blueprint("device_manage", url_prefix="/device/api")

def amis_response(data=''):
    return response.json({
        "status": 0,
        "msg": "ok",
        "data": data
        })


class DeviceListView(HTTPMethodView):
    def get(self, request):
        args = dict(request.query_args)
        page = int(args.get('page', 1))
        size = int(args.get('perPage', 10))
        select = Device.select()
        
        if args.get('os'):
            select = select.where(Device.os == args['os'])
        if args.get('version'):
            select = select.where(Device.version == args['version'])
        ret = select.paginate(page, size)
        data = {
            'items': [d.to_dict() for d in ret],
            'total': select.count()
        }
        return amis_response(data)

    async def post(self, request):
        Device.create(**request.json)
        return amis_response()

class DeviceView(HTTPMethodView):
    async def put(self, request, id):
        query = Device.update(**request.json).where(Device.id==id)
        code = query.execute()
        return amis_response()

    async def post(self, request, id: int):
        action = request.args.get('action')
        user = request.args.get('user')
        device = Device.get(Device.id==id)
        if action == '1':
            from_ = device.user
            to_ = user
        elif action == '2':
            from_ = user
            to_ = Device.get(Device.id==id).owner
        History.create(device_id=id, from_=from_, to=to_)
        device.user = to_
        device.save()
        return amis_response()

    async def get(self, request, id: int):
        dev = Device.get(Device.id==id)
        return amis_response(dev.to_dict())

    def delete(self, request):
        pass


@bp.get('/history/<id>')
async def history_handler(request, id):
    ret = History.select().where(History.device_id==id).order_by(History.date.desc())
    data = {
        'items': [d.to_dict() for d in ret],
    }
    return amis_response(data)

@bp.get('/qrcode/<id>')
def qrcode_handler(request, id):
    url = f'{request.scheme}://{request.host}/device/page/borrow.html?id={id}'
    img = qrcode.make(url)
    img.save('./static/img/qrcode.png')
    return response.file('./static/img/qrcode.png', mime_type="image/png")


bp.add_route(DeviceView.as_view(), '/device/<id>')
bp.add_route(DeviceListView.as_view(), '/device')

