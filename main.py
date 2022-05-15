# Python
import json
from typing import List, Dict

# Models
from models import User, UserLogin, Tweet, UserRegister

# FastAPI
from fastapi import status
from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

# Path Operations

## Users

### Register a user
@app.post(
    path='/auth/singup',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Register a user',
    tags=['Auth', 'users']
)
def singup(
    user: UserRegister = Body(...)
):
    """
    Singup a user

    This Path operation register a user in Twitter app

    Parameters:
    - Request Body Parameters:
        - user: UserRegister
    
    Returns a JSON with the basic user information:
    - model:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date_type
    """
    with open('users.json', 'r+', encoding='utf-8') as f:
        results = json.load(f)
        
        user_dict = dict(user)
        user_dict['user_id'] = str(user_dict['user_id'])
        user_dict['birth_date'] = str(user_dict['birth_date'])
        
        results.append(user_dict)
        
        f.seek(0)
        json.dump(results, f)

        return user


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
    """
    Show All Users

    This path operation Shows all users in the app

    Parameters:
    - Requests:
        - None

    Returns a Json list with all users in the app, with the following keys:
    - Model:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: datetipe
    """
    with open('users.json', 'r', encoding='utf-8') as f:
        results = json.load(f)

        return results


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
def post(
    tweet: Tweet = Body(
        ...
    )
):
    """
    Post Tweets

    This Path operation upload a tweet in Twitter app

    Parameters:
    - Request Body Parameters:
        - tweet: Tweet
    
    Returns a JSON with the basic tweet information:
    - model:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User 
    """
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.load(f)
        
        tweet_dict = tweet.dict()
        
        # Tweets
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        
        if tweet_dict["updated_at"]:
            tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        
        # Users
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])
        
        results.append(tweet_dict)
        f.seek(0)
        json.dump(results, f)
        
        return tweet


### Show all tweets
@app.get(
    path='/',
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary='Show all tweets',
    tags=['Tweets','Home'])
def home(

) -> Dict[str, str]:
    """
    Home Route

    Show all Tweets in Twitter app

    Parameters:
    - None

    Returns all tweets posted in Twitter app
    """
    with open('tweets.json', 'r', encoding='utf-8') as f:
        results = json.load(f)

        return results



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
