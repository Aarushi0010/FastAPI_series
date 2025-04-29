from fastapi import FastAPI
from . import schemas

app = FastAPI()


@app.post('/content')
def content(request : schemas.Content):
    return {f'content add with title {request.title}'}