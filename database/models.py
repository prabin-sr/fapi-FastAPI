import uuid

import peewee

from settings.base import conn


class BaseModel(peewee.Model):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = peewee.DateTimeField()
    updated_at = peewee.DateTimeField()

    class Meta:
        database = conn
