# FastAPI
from fastapi import FastAPI

app = FastAPI()

@app.get(
    path='/',
    tags=['Home'])
def home():
    return {'Twitter API': 'Working'}