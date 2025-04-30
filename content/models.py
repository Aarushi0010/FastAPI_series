from sqlalchemy import Column, Integer, String
from .database import Base


class Content(Base):

    __tablename__ = 'content'
    id = Column(Integer, primary_key=True)
    # title = Column(String)
    body = Column(String)