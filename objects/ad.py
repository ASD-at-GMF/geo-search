from sqlalchemy import Column, Integer, String, JSON, Text
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