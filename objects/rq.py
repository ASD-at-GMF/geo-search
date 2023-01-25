from sqlalchemy import Column, Integer, String, JSON, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Related_Question(Base):
    __tablename__ = "related_question"

    id = Column(Integer, primary_key=True)
    search_id = Column(String)
    snippet = Column(String)
    title = Column(String)
    date = Column(String)
    link = Column(String)
    displayed_link = Column(String)
    next_page_token = Column(String)
    serpapi_link = Column(String)
