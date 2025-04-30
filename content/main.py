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