from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Related_Search(Base):
    __tablename__ = 'related_search'

    id = Column(Integer, primary_key=True)
    search_id = Column(String)
    query = Column(String)
    link = Column(String)
    serpapi_link = Column(String)