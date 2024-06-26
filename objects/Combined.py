from sqlalchemy import Column, Integer, String, JSON, Text
from sqlalchemy.ext.declarative import declarative_base

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
    


class News_Result(Base):
    __tablename__ = "news_result"

    id = Column(Integer, primary_key=True)
    search_id = Column(String)
    position = Column(String)
    snippet = Column(String)
    title = Column(String)
    date = Column(String)
    link = Column(String)
    source = Column(String)
    thumbnail = Column(String)

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
    


class Q_and_A(Base):
    __tablename__ = 'q_and_a'

    id = Column(Integer, primary_key=True)
    search_id = Column(String)
    link = Column(String)
    source = Column(String)
    question = Column(String)
    answer = Column(String)
    votes = Column(Integer)

    
        




class Related_Search(Base):
    __tablename__ = 'related_search'

    id = Column(Integer, primary_key=True)
    search_id = Column(String)
    query = Column(String)
    link = Column(String)
    serpapi_link = Column(String)



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

    
    



class Twitter_Result(Base):
    __tablename__ = "twitter_result"

    id = Column(Integer, primary_key=True)
    search_id = Column(String)
    link = Column(String)
    snippet = Column(String)
    published_date = Column(String)
    info = Column(String)
    thumbnail = Column(String)
    author  = Column(JSON)
    


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
        
    
        
