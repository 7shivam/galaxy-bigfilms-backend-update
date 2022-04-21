from sqlalchemy import Table, Column
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import BLOB, Date, Integer, String
from config.db import meta, engine

movies = Table('movie', meta,
 Column('id', Integer, primary_key=True),
 Column('Name', String (255)),
 Column('Actors', String (255)),
 Column('Release', Date),
 Column('Rating',Integer),
 Column('Image',String(255))
#Column('sipnosis', String (255)),
 
)
meta.create_all(engine)