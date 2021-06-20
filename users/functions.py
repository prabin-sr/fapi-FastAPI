from . import models


async def create_db_values():
    user = models.User.create(
        first_name="Prabin",
        last_name="S",
        email="xyz@gmail.com",
        phone="9943289900",
        status=True
    )
    # print(created)
    # user.save()
    return user.id
