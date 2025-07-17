from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, String, Integer, Column

engine = create_engine('sqlite:///sales.db', echo=True)


class Base(DeclarativeBase):
    pass

class Customers(Base):
   __tablename__ = 'customers'
   
   id = Column(Integer, primary_key = True)
   name = Column(String)
   address = Column(String)
   email = Column(String)