from starlette.config import Config
from starlette.datastructures import Secret
from tortoise.models import Model
from tortoise import fields, Tortoise

from app.exceptions import ApiException

try:
    config = Config("app/.env")
    POSTGRES_USER = config("POSTGRES_USER", cast=str)
    POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
    POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="postgresql")
    POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
    POSTGRES_DB = config("POSTGRES_DB", cast=str)
    DATABASE_URL = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
except Exception:
    raise ApiException(400, 'Не найден .env файл с авторизационными данными')


class CargoType(Model):
    id = fields.IntField(pk=True)
    type = fields.CharField(max_length=60)
    price = fields.FloatField()

    def __str__(self):
        return self.type


class Insurance(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField()
    rate = fields.FloatField()
    cargo_type: fields.ForeignKeyRelation[CargoType] = fields.ForeignKeyField(
        "models.CargoType",
        related_name="insurances",
        on_delete=fields.CASCADE
    )

    def __str__(self):
        return f"{self.date}||{self.rate}"


async def init():
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={'models': ['app.database.models']}
    )
    await Tortoise.generate_schemas()
