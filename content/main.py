from fastapi import FastAPI
from . import schemas , models
from .database import engine

models.Base.metadata .create_all(engine)

app = FastAPI()


@app.post('/content')
def content(request : schemas.Content):
    return {f'content add with title {request.title}'}