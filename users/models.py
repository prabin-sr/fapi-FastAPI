import peewee
from generics.mixins import ModelMixin


class User(ModelMixin):
    firstname = peewee.CharField(max_length=30, null=False)
    middlename = peewee.CharField(max_length=30, null=True)
    lastname = peewee.CharField(max_length=30, null=False)
    email = peewee.CharField(max_length=40, unique=True)
    is_superuser = peewee.BooleanField(default=False)
    is_active = peewee.BooleanField(default=False)
    password = peewee.CharField(max_length=500, unique=True)

    class Meta:
        db_table = 'Users'
