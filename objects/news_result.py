from sqlalchemy import Column, Integer, String, JSON, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class News_Result(Base):
    __tablename__ = "news_result"

    id = Column(Integer, primary_key=True)
    search_id = Column(String)
    position = Column(String)
    snippet = Column(String)
    title = Column(String)
    date = Column(String)
    link = Column(String)
    source = Column(String)
    thumbnail = Column(String)
