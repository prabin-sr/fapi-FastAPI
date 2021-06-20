import peewee
from database.models import BaseModel


class User(BaseModel):
    first_name = peewee.CharField(max_length=30)
    last_name = peewee.CharField(max_length=30)
    email = peewee.CharField(max_length=40)
    phone = peewee.CharField(max_length=25)
    status = peewee.BooleanField(default=False)

    class Meta:
        db_table = 'Users'
