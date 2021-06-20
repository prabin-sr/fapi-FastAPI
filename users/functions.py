from passlib.context import CryptContext

from .models import User


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def register_user(data):
    pass


async def create_db_values():
    user = User.create(
        first_name="Prabin",
        last_name="S",
        email="xyz@gmail.com",
        phone="9943289900",
        status=True
    )
    # print(created)
    # user.save()
    return user.id
