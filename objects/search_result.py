from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Search_Result(Base):
    __tablename__ = 'search_result'

    id = Column(Integer, primary_key=True)
    search_id = Column(String)
    position = Column(Integer)
    title = Column(String)
    link = Column(String)
    displayed_link = Column(String)
    thumbnail = Column(String)
    snippet = Column(String)
    snippet_highlighted_words = Column(String)
    about_this_result = Column(JSON)
    about_page_link = Column(String)
    about_page_serpapi_link = Column(String)
    cached_page_link = Column(String)