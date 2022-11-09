import configparser
from peewee import DateTimeField, ForeignKeyField, MySQLDatabase, Model
from peewee import CharField, PrimaryKeyField, TextField, IntegerField, FloatField
from playhouse.shortcuts import model_to_dict

import datetime
import pathlib

base = pathlib.Path(__file__).parent.parent

config = configparser.ConfigParser()
config.read(base / 'config.ini')
db_cfg = dict(config.items('db'))

db = MySQLDatabase(db_cfg['db'], user=db_cfg['username'], password=db_cfg['password'], host=db_cfg['host'], port=3306)


class Device(Model):
    id = PrimaryKeyField()
    serial = CharField()
    type_ = CharField(column_name='type')
    screen = FloatField()
    os = CharField()
    version = CharField()
    model = CharField()
    fitting = TextField()
    owner = CharField()
    user = CharField()
    since = DateTimeField(default=datetime.datetime.now(), formats='%Y-%m-%d %H:%M')
    condition = IntegerField()  # 几成新，0代表损坏

    class Meta:
        database = db
        table_name = 'tb_device'

    def to_dict(self):
        dct = model_to_dict(self)
        dct['since'] = dct['since'].strftime('%Y-%m-%d %H:%M')
        return dct


class History(Model):
    id = PrimaryKeyField()
    device_id = ForeignKeyField(Device, backref='history', lazy_load=False)
    to = CharField()  # 借用者
    from_ = CharField(column_name='from')
    date = DateTimeField(default=datetime.datetime.now(), formats='%Y-%m-%d %H:%M')

    class Meta:
        database = db
        table_name = 'tb_device_history'

    def to_dict(self):
        dct = {
            'date': self.date.strftime('%Y-%m-%d %H:%M'),
            'id': self.id,
            'from': self.from_,
            'to': self.to
        }
        return dct


if __name__ == "__main__":
    ret = Device.select().limit(1)
    print(ret)
    breakpoint()
