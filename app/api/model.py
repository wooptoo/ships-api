import peewee as pw
import config

db = pw.PostgresqlDatabase(
    config.DB_NAME, host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASS
)


class BaseModel(pw.Model):
    class Meta:
        database = db


class Ships(BaseModel):
    imo = pw.PrimaryKeyField()
    name = pw.CharField()


class Positions(BaseModel):
    imo = pw.ForeignKeyField(Ships, field='imo', backref='positions')
    timestamp = pw.DateTimeField()
    latitude = pw.DoubleField()
    longitude = pw.DoubleField()