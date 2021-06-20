from typing import Optional

from pydantic import BaseModel, EmailStr, validator


class RegisterUserRequest(BaseModel):
    firstname: str
    middlename: Optional[str]
    lastname: str
    email: EmailStr
    password1: str
    password2: str

    @validator('firstname')
    def firstname_validation(cls, v):
        if not v.isalpha():
            raise ValueError('firstname must be in alphabhetic characters.')
        if len(v) < 3:
            raise ValueError('firstname must contain at least 2 letters.')
        if len(v) > 30:
            raise ValueError('firstname must not contain more than 30 letters.')
        return v

    @validator('middlename')
    def middlename_validation(cls, v):
        if len(v) > 30:
            raise ValueError('middlename must not contain more than 30 letters.')
        return v

    @validator('lastname')
    def lastname_validation(cls, v):
        if not v.isalpha():
            raise ValueError('lastname must be in alphabhetic characters.')
        if len(v) < 1:
            raise ValueError('lastname must contain at least 1 letter.')
        if len(v) > 30:
            raise ValueError('lastname must not contain more than 30 letters.')
        return v

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('mismatched passwords.')
        if len(v) < 8:
            raise ValueError('password must contain at least 8 characters.')
        if len(v) > 16:
            raise ValueError('password must not contain more than 16 characters.')
        return v
