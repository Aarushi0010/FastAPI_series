from pydantic import BaseModel


class Content(BaseModel):
    title : str
    body : str
