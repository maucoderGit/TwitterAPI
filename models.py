# Python
from uuid import UUID
from datetime import date as date_type, datetime
from typing import Optional, List

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from pydantic import validator

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserPassword(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=100,
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
    )
    birth_date: Optional[date_type] = Field(default=None)

class UserLogin(UserPassword, UserBase):
    pass

class UserRegister(UserPassword, User):
    pass

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=280
        )
    created_at: datetime = Field(default=datetime.now())
    update_ad: Optional[datetime] = Field(default=None)
    tweeted_by: User = Field(...)

# Validators
@validator('birth_date')
def is_over_eighteen(cls, v):
    todays_date = date_type.today()
    delta = todays_date - v

    if delta.days/365 <= 13:
        raise ValueError('Must be over 13!')
    else:
        return v
