# third-party modules
from passlib.context import CryptContext
from email_validator import validate_email, EmailNotValidError

# user-defined modules
from settings.base import conn
from users.models import User


def get_password_hash(password):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.hash(password)


def userdata_validator(firstname, lastname, email, password1, password2):
    if not firstname.isalpha():
        raise ValueError('firstname must be in alphabhetic characters.')
    if len(firstname) < 3:
        raise ValueError('firstname must contain at least 2 letters.')
    if len(firstname) > 30:
        raise ValueError('firstname must not contain more than 30 letters.')
    if not lastname.isalpha():
        raise ValueError('lastname must be in alphabhetic characters.')
    if len(lastname) < 1:
        raise ValueError('lastname must contain at least 1 letter.')
    if len(lastname) > 30:
        raise ValueError('lastname must not contain more than 30 letters.')
    try:
        valid = validate_email(email)
    except EmailNotValidError:
        raise ValueError("invalid email address.")
    email = valid.email
    if password1 != password2:
        raise ValueError('mismatched passwords.')
    if len(password1) < 8:
        raise ValueError('password must contain at least 8 characters.')
    if len(password1) > 16:
        raise ValueError('password must not contain more than 16 characters.')
    password = get_password_hash(password2)

    return email, password


firstname = input("Enter firstname: ").strip()
lastname = input("Enter lastname: ").strip()
email = input("Enter email address: ").strip()
password1 = input("Enter password: ").strip()
password2 = input("Confirm password: ").strip()

# Validate Input Data
email, password = userdata_validator(firstname, lastname, email, password1, password2)

# Initialize Connection
conn.connect()

# Create SuperUser
User.create(
    firstname=firstname,
    lastname=lastname,
    email=email,
    is_superuser=True,
    is_active=True,
    password=password
)

# Close Connection
conn.close()
