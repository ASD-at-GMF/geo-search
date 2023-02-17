from sqlalchemy import Column, Integer, String, JSON, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Top_Story(Base):
    __tablename__ = "Top_Story"

    id = Column(Integer, primary_key=True)
    search_id = Column(String)
    title = Column(String)
    link = Column(String)
    source = Column(String)
    date = Column(String)
    thumbnail = Column(String)
    live = Column(String)
