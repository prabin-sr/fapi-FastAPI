import peewee

from settings.base import conn


class BaseModel(peewee.Model):
    created_at = peewee.DateTimeField()
    updated_at = peewee.DateTimeField()

    class Meta:
        database = conn
