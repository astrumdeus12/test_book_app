from enum import Enum
from beanie import Document
from pydantic import Field

class Status(str, Enum):
    available = 'в наличие'
    issued = 'выдана'

    
    
class Book(Document):
    id : int = Field(default=1)
    title : str
    author : str
    year : int 
    status : Status = 'в наличие'
    
    class Settings:
        collection = 'books'
        
