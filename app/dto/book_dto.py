from pydantic import BaseModel


class BookSchema(BaseModel):
    id : int = None
    title : str
    author : str
    year : int
    status : str