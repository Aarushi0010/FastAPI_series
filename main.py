from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def base():
    return 'yeaa'

@app.get('/data')
def data():
    return {'data' : {'name' : 'Aarushi'}}

@app.get('/blog/{id}')
def blog(id):
    return 'blog at',id

@app.get('/query')
def query(limit = 10 ,published :bool = True ,sort : Optional[str] = None ):
    if published:
        return {'data' : f'{limit} published blogs from db'}
    
    else :
        return {'data' : f'{limit} blogs from db'}
    

class Content(BaseModel):
    title : str
    body : str
    published : Optional[bool]


@app.post('/content')
def content(request : Content):
    return {f'content added with title {request.title}'}