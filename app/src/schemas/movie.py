from datetime import date
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Integer

class Movie(BaseModel):
    id:int
    Name: str
    Actors: str
    Release:date
    Rating: int
    Image: str
  
    