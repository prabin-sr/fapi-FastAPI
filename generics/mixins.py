import uuid
import datetime

import peewee

from settings.base import conn


class ModelMixin(peewee.Model):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = peewee.DateTimeField(default=datetime.datetime.now)
    updated_at = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = conn
