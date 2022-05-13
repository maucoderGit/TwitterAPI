# Python
from uuid import UUID
from datetime import date as date_type
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from pydantic import validator

# FastAPI
from fastapi import FastAPI

app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8
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

class Tweet(BaseModel):
    pass

# Validators
@validator('birth_date')
def is_over_eighteen(cls, v):
    todays_date = date_type.today()
    delta = todays_date - v

    if delta.days/365 <= 13:
        raise ValueError('Must be over 13!')
    else:
        return v

@app.get(
    path='/',
    tags=['Home'])
def home():
    return {'Twitter API': 'Working'}