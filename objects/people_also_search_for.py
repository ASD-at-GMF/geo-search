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
    text = Column(String)
    serpapi_link = Column(String)
    
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