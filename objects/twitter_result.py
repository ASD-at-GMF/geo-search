from sqlalchemy import Column, Integer, String, JSON, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Twitter_Result(Base):
    __tablename__ = "twitter_result"

    id = Column(Integer, primary_key=True)
    search_id = Column(String)
    link = Column(String)
    snippet = Column(String)
    published_date = Column(String)
    info = Column(String)
    thumbnail = Column(String)
    author  = Column(String)
