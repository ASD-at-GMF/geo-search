from sqlalchemy import Column, Integer, String, JSON, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Related_Question(Base):
    __tablename__ = "related_question"

    id = Column(Integer, primary_key=True)
    search_id = Column(String)
    question = Column(String)
    snippet = Column(String)
    title = Column(String)
    date = Column(String)
    link = Column(String)
    displayed_link = Column(String)
    next_page_token = Column(String)
    serpapi_link = Column(String)
    related_questions = Column(JSON)
    thumbnail = Column(String)
    list = Column(JSON)
    info = Column(JSON)
        
    @classmethod
    def get_allowed_keys(cls):
        # Get the column names from the table metadata
        column_names = cls.__table__.columns.keys()
        # Convert the column names to a list of strings
        allowed_keys = [str(column) for column in column_names]
        return allowed_keys

    def __init__(self, **kwargs):
        # Get the allowed keys for this class
        allowed_keys = self.get_allowed_keys()
        # Filter out any keys that are not in the allowed_keys list
        valid_kwargs = {k: v for k, v in kwargs.items() if k in allowed_keys}
        # Use the filtered kwargs to initialize the object attributes
        self.__dict__.update(valid_kwargs)