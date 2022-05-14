# Python
from email.policy import HTTP
from typing import List, Dict

# Models
from models import User, UserLogin, Tweet

# FastAPI
from fastapi import status
from fastapi import FastAPI

app = FastAPI()

# Path Operations

## Users

### Register a user
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


### Login a User
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


### Show all users
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


### Show a user
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


### Delete a user
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


### Update a User
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

### Post a tweet

@app.post(
    path='/post',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='Post a tweet',
    tags=['Tweets']
)
def post():
    pass


### Show all tweets
@app.get(
    path='/',
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary='Show all tweets',
    tags=['Tweets','Home'])
def home() -> Dict[str, str]:
    """
    Home Route

    Show a message explaining if Twitter API is working

    Parameters:
    - None

    Returns JSON key: 'Twitter API' and JSON value: 'Working'
    """
    return {'Twitter API': 'Working'}


### Show a Tweet
@app.get(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Show a tweet',
    tags=['Tweets']
)
def show_a_tweet():
    pass


### Delete a tweet
@app.delete(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Delete a tweet',
    tags=['Tweets']
)
def delete_a_tweet():
    pass


### Update a Tweet
@app.put(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Update a tweet',
    tags=['Tweets']
)
def update_a_tweet():
    pass
