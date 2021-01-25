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


class Cliente(peewee.Model):
    id = peewee.UUIDField(primary_key=True)
    nome = peewee.TextField()
    sobrenome = peewee.TextField()
    cpf = peewee.TextField()
    sexo = peewee.TextField()
    telefone = peewee.TextField()
    email = peewee.TextField()
    endereco_id = peewee.UUIDField()

    class Meta:
        database = db


db.connect()
db.create_tables([Cliente])
