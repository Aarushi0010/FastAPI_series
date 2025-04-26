from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def base():
    return 'yeaa'

@app.get('/data')
def data():
    return {'data' : {'name' : 'Aarushi'}}