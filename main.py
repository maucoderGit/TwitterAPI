# Python
from typing import List, Dict

# Models
from models import User, UserLogin, Tweet

# FastAPI
from fastapi import status
from fastapi import FastAPI

app = FastAPI()

# Path Operations

@app.get(
    path='/',
    tags=['Home'])
def home() -> Dict[str, str]:
    """
    Home Route

    Show a message explaining if Twitter API is working

    Parameters:
    - None

    Returns JSON key: 'Twitter API' and JSON value: 'Working'
    """
    return {'Twitter API': 'Working'}

## Users

@app.post(
    path='auth/singup',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Register a user',
    tags=['Auth', 'users']
)
def singup(

):
    pass

@app.post(
    path='auth/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Login a user',
    tags=['Auth', 'users']
)
def login(
    
):
    pass

@app.get(
    path='/users',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary='Show all user',
    tags=['users']
)
def show_all_users(
    
):
    pass

@app.get(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Show a user',
    tags=['users']
)
def show_a_users(
    
):
    pass

@app.delete(
    path='/users/{user_id}/delete',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Delete a user',
    tags=['users']
)
def delete_a_user(
    
):
    pass

@app.put(
    path='/users/{user_id}/update',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Update a user',
    tags=['users']
)
def Update_a_user(
    
):
    pass

## Tweets