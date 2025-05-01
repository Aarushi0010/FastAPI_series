from fastapi import FastAPI, Depends
from . import schemas , models
from .database import engine , SessionLocal
from sqlalchemy.orm import session


models.Base.metadata .create_all(engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()


@app.post('/content')
def content(request : schemas.Content , db : session = Depends(get_db)):
    new_content = models.Content(body = request.body)

    db.add(new_content)
    db.commit()
    db.refresh(new_content)
    return new_content


#return ALL contents 
@app.get('/content')
def getContent(db : session = Depends(get_db)):
    content= db.query(models.Content).all()
    return content 


#return FILTERED content using id
@app.get('/blog/{id}')
def getBlog(id, db : session = Depends(get_db)):
    blog = db.query(models.Content).filter(models.Content.id == id).first()
    return blog 