from sqlalchemy import Column, Integer, String, JSON, DateTime
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
    date = Column(String)
    snippet = Column(String)
    snippet_highlighted_words = Column(String)
    sitelinks =  Column(JSON)
    about_this_result = Column(JSON)
    about_page_link = Column(String)
    about_page_serpapi_link = Column(String)
    cached_page_link = Column(String)
    related_pages_link = Column(String)
    related_results = Column(JSON)
    rich_snippet = Column(JSON)
    displayed_results = Column(String)
    displayed_brand = Column(String)
    related_questions = Column(JSON)
    images = Column(JSON)
    rich_snippet_table = Column(JSON)
    source = Column(String)
    sitelinks_search_box = Column(JSON)
    tracking_link  = Column(String)
    missing  = Column(String)
    must_include  = Column(JSON)
    video_link = Column(String)
    key_moments = Column(JSON)
    related_news = Column(JSON)
    related_videos = Column(JSON)
    related_images = Column(JSON)
    tieba = Column(JSON)
    duration = Column(String)
    video_quality = Column(String)
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