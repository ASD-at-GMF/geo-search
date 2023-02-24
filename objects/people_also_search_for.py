from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class People_Also_Search_For(Base):
    __tablename__ = 'people_also_search_for'

    id = Column(Integer, primary_key=True)
    search_id = Column(String)
    name = Column(String)
    link = Column(String)
    image = Column(String)
    news_results = Column(JSON)