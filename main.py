from sanic import Sanic
from app.model import db
from app.device import bp

app = Sanic('device')
app.blueprint(bp)
app.static('/device/page', './static')

app.middleware('request')


async def handle_request(request):
    if db.is_closed():
        db.connect()


@app.middleware('response')
async def handle_response(request, response):
    if not db.is_closed():
        db.close()


app.run(host='127.0.0.1', port=9300, debug=True)
# app.url_for('post_handler', post_id=5)
