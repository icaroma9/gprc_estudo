import peewee
from decouple import config

DATABASE = config("DB_NAME")
HOST = config("DB_HOST")
USER = config("DB_USER")
PASSWORD = config("DB_PASSWORD", default="localhost")
PORT = config("DB_PORT", default=5432, cast=int)

db = peewee.PostgresqlDatabase(
    DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT
)


class Endereco(peewee.Model):
    id = peewee.UUIDField(primary_key=True)
    cep = peewee.TextField()
    logradouro = peewee.TextField()
    bairro = peewee.TextField()
    cidade = peewee.TextField()
    estado = peewee.TextField()

    class Meta:
        database = db


db.connect()
db.create_tables([Endereco])
