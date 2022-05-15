# Python
import json
from typing import List, Dict
from uuid import UUID
from xxlimited import Str

# Models
from models import User, UserLogin, Tweet, UserRegister

# FastAPI
from fastapi import status, HTTPException
from fastapi import FastAPI
from fastapi import Body, Path

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
    path='/auth/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Login a user',
    tags=['Auth', 'users']
)
def login(
    user: UserLogin = Body(
        ...,
        title='User login data',
        description='Object parameter gets UserLogin Model')
):
    """
    Login

    Path Operation to Login Users in the Twitter app.

    Parameter:
    - Request Body:
        - user: UserLogin
    
    Returns a JSON with the user login basic information: 
    - User_id: UUID
    - Email: EmailStr
    - Password: str
    """
    with open('users.json', 'r', encoding='UTF-8') as f:
        all_users: list[dict] = json.load(f)

        for i in all_users:
            if i['email'] == user.email and i['password'] == user.password:
                return i
        
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='The email or password is incorrect.'
        )


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
    user_id: UUID = Path(
        ...,
        title='User ID',
        description='Gets a user identifier'
        )
) -> User:
    with open('users.json', 'r', encoding='utf-8') as f:
        results = json.load(f)

        for i in results:
            if str(user_id) == i['user_id']:
                return i

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"¡This user_id doesn't exist!"
        )


### Delete a user
@app.delete(
    path='/users/{user_id}',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary='Delete a user',
    tags=['users']
)
def delete_a_user(
    user_id: UUID = Path(..., title='user id', description='User ID to be deleted')
):
    """
    Delete a user

    This Path Operation removes a user by UUID

    Parameters:
    - Request Body:
        - User_id: UUID

    Returns a json list with all users in the app, with the following keys:
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    with open('users.json', 'r+', encoding='utf-8') as f:
        results: List[dict] = json.load(f)

        for i in results:
            if i['user_id'] == str(user_id):
                results.remove(i)

                with open("users.json", "w", encoding="utf-8") as f:
                    f.seek(0)
                    json.dump(results, f)

                return results
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'This {user_id} doesn\'t exist.'
        )

### Update a User
@app.put(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Update a user',
    tags=['users']
)
def Update_a_user(
    user_id: UUID = Path(
        ...,
        title='User ID',
        description='Path parameter gets user information to update'),
    user: User = Body(
        ...,
        title='User Model',
        description='User model that will be modified')
):
    """
    Update a user

    Path operation gets user information by id.

    Parameters:
    - Request Body:
        - user_id: UUID
    - Optional information to update:
        - first_name: str
        - last_name: str
        - birth_date: date_tipe

    Returns a modified user model with optional:
    - id
    - first_name
    - last_name
    - birth_date
    """
    with open('users.json', 'r+', encoding='utf-8') as f:
        users: List[Dict] = json.load(f)

        for i in users:
            if i['user_id'] == str(user_id):
                index = users.index(i)
                
                user = dict(user)
                user['user_id'] = str(user['user_id'])
                user['birth_date'] = str(user['birth_date'])

                users[index] = user

                json.dump(users, f)

                return users[index]

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='USER ID NOT FOUND'
        )

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
    with open('tweets.json', 'r+', encoding='utf-8') as f:
        results = json.load(f)
        
        tweet_dict = tweet.dict()
        
        # Tweets
        tweet_dict['tweet_id'] = str(tweet_dict['tweet_id'])
        tweet_dict['created_at'] = str(tweet_dict['created_at'])
        
        if tweet_dict['updated_at']:
            tweet_dict['updated_at'] = str(tweet_dict['updated_at'])
        
        # Users
        tweet_dict['by']['user_id'] = str(tweet_dict['by']['user_id'])
        tweet_dict['by']['birth_date'] = str(tweet_dict['by']['birth_date'])
        
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

    This path opertation shows all tweets in the twitter app

    Parameters:
    - None

    Returns a JSON list with all tweets in the app, with the following keys:
    - tweet_id: UUID
    - content: str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - Birth_date: date_type
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
def show_a_tweet(
    tweet_id: UUID = Path(
        ...,
        title='Tweet ID',
        describe='Path parameter gets an ID from a Tweet'
    )
):
    """
    Show a Tweet

    This Path Operation Gets an ID and then show a tweet
    
    Parameters:
    - Request Body:
        - tweet_id: UUID

    Returns a Tweet model in a JSON output with:
    - tweet_id: UUID
    - content: str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - Birth_date: date_type
    """
    with open('tweets.json', 'r', encoding='utf-8') as f:
        results = json.load(f)

        for i in results:
            if i['tweet_id'] == str(tweet_id):
                return i
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='TWEET NOT FOUND'
        )

### Delete a tweet
@app.delete(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Delete a tweet',
    tags=['Tweets']
)
def delete_a_tweet(
    tweet_id: UUID = Path(
        ...,
        title='Tweet ID',
        description='Gets a tweet ID to remove'
    )
):
    """
    Delete a Tweet

    This Path Operation removes a user by UUID

    Parameters:
    - Request Body:
        - tweet_id: UUID

    Returns a json list with all tweets in the app, with the following keys:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: datetime
        - by: User
    """
    with open('tweets.json', 'r+', encoding='utf-8') as f:
        results: List[dict] = json.load(f)

        for i in results:
            if i['tweet_id'] == str(tweet_id):
                results.remove(i)

                with open("tweets.json", "w", encoding="utf-8") as f:
                    f.seek(0)
                    json.dump(results, f)

                return i
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'This {tweet_id} doesn\'t exist.'
        )



### Update a Tweet
@app.put(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Update a tweet',
    tags=['Tweets']
)
def update_a_tweet(
    tweet_id: UUID = Path(
        ...,
        title='Tweet ID',
        description='Gets the tweet ID'
    ),
    tweet: Tweet = Body(
        ...,
        title='Tweet Information',
        description='Basic information to update'
    )
):
    """
    Update a Tweet

    New functionality in Twitter app

    Parameters:
    - Request Body:
        - tweet_id: UUID
        - Tweet: tweet

    Returns the updated tweet.
    """
    with open('tweets.json', 'r+', encoding='utf-8') as f:
        tweets: List[Dict] = json.load(f)

        for i in tweets:
            if i['tweet_id'] == str(tweet_id):
                tweets.remove(i)
        
                tweet_dict = tweet.dict()
        
                # Tweets
                tweet_dict['tweet_id'] = str(tweet_dict['tweet_id'])
                tweet_dict['created_at'] = str(tweet_dict['created_at'])
                
                if tweet_dict['updated_at']:
                    tweet_dict['updated_at'] = str(tweet_dict['updated_at'])
                
                # Users
                tweet_dict['by']['user_id'] = str(tweet_dict['by']['user_id'])
                tweet_dict['by']['birth_date'] = str(tweet_dict['by']['birth_date'])
                
                tweets.append(tweet_dict)
                
                with open("tweets.json", "w", encoding="utf-8") as f:
                    f.seek(0)
                    json.dump(tweets, f)

                return tweet

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='USER ID NOT FOUND'
        )