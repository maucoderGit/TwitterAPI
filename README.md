# Twitter API clone with FastAPI

What does it mean?

Using FastAPI, I clone the Twitter API service using the CRUD model:

- Create User, Tweet.
- Read Users: by id, all; Tweet, by id, all.
- Update (Yes, it's a new functionality): user, by id; tweet, by id.
- Delete: Tweets and users using id.

## Useful in this project:

In this project, I use many programming concepts, like:
- API model.
- FastAPI concepts and use.
- Validations.
- HTTP verbs/methods, responses, and requests.
- Object-Oriented Programming.
- Function Documenting.
- Swagger UI Documentation.
- JSON Responses and Requests.

## How can you see this project?

First, run in your shell this(before activating the virtual environment):
```
pip3 install -r requirements.txt
uvicorn main:app
```
Now you might see this in your shell.
```
INFO:     Started server process [18740]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```
### Endpoints:

The easier way to use an API developed with FastAPI is to use interactive documentation.

The URL is http://127.0.0.1:8000/docs or http:localhost:8000/docs.
Using this, you can test by yourself the documented API.
