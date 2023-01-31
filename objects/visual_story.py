from sqlalchemy import Column, Integer, String, JSON, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Visual_Story(Base):
    __tablename__ = "visual_story"

    id = Column(Integer, primary_key=True)
    search_id = Column(String)
    position = Column(Integer)
    title = Column(String)
    link = Column(String)
    thumbnail = Column(String)
    source = Column(String)
    source_icon = Column(String)