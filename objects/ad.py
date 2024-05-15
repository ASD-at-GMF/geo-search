from sqlalchemy import Column, Integer, String, JSON, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ad(Base):
    __tablename__ = 'ad'

    id = Column(Integer, primary_key=True)
    search_id = Column(String)
    position = Column(Integer)
    block_position = Column(String)
    title = Column(String)
    phone = Column(String)
    link = Column(String)
    displayed_link = Column(String)
    tracking_link = Column(String)
    description = Column(Text)
    extensions = Column(String)
    sitelinks = Column(JSON)
    products = Column(JSON)
    thumbnail = Column(String)
    Created = Column(DateTime)
    Updated = Column(DateTime)
    query = Column(String)
    location = Column(String)
    search_engine = Column(String)
    current_timestamp_str = Column(DateTime)

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