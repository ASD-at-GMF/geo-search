from sqlalchemy import Column, Integer, String, JSON, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Q_and_A(Base):
    __tablename__ = 'q_and_a'

    id = Column(Integer, primary_key=True)
    search_id = Column(String)
    link = Column(String)
    source = Column(String)
    question = Column(String)
    answer = Column(String)
    votes = Column(Integer)