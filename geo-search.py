
from itertools import product  # importing the product method from itertools library
import requests
import traceback
from datetime import datetime
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# Internal Imports
from config import API_KEY, SERVER_URL, DATABASE, DB_USERNAME, DB_PASSWORD, FILE_NAME
from objects.search_query_results import Search_Query_Results
from objects.search_result import Search_Result
from objects.related_search import Related_Search
from objects.people_also_search_for import People_Also_Search_For
from objects.ad import Ad
from objects.q_and_a import Q_and_A
from objects.top_story import Top_Story
from objects.twitter_result import Twitter_Result
from objects.visual_story import Visual_Story
from objects.rq import Related_Question
from objects.news_result import News_Result

current_timestamp_str = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

# ignored = ['search_information', 'knowledge_graph', ]

def connect_to_db():

    # Define the connection string
    connection_string = 'postgresql+psycopg2://' + \
    DB_USERNAME+':'+DB_PASSWORD+'@'+SERVER_URL+'/'+DATABASE

    # Create the SQLAlchemy engine
    engine = create_engine(connection_string)
    
    # Connect to the database
    connection = engine.connect()   
    Base = declarative_base()
    Base.metadata.create_all(engine)

    # Table drop/create--leave as is unless change is needed
    # Search_Result.__table__.drop(engine)
    # Search_Result.__table__.create(engine)
    # Related_Search.__table__.drop(engine)
    # Related_Search.__table__.create(engine)
    # People_Also_Search_For.__table__.drop(engine)
    # People_Also_Search_For.__table__.create(engine)
    # Ad.__table__.drop(engine) 
    # Ad.__table__.create(engine)
    # Related_Question.__table__.drop(engine)
    # Related_Question.__table__.create(engine)
    # Q_and_A.__table__.drop(engine)
    # Q_and_A.__table__.create(engine)
    # Top_Story.__table__.drop(engine)
    # Top_Story.__table__.create(engine)
    # Twitter_Result.__table__.drop(engine)
    # Twitter_Result.__table__.create(engine)
    # Visual_Story.__table__.drop(engine)
    # Visual_Story.__table__.create(engine)
    # News_Result.__table__.drop(engine)
    # News_Result.__table__.create(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def form_parameters(query, location, search_engine, start = 0):
    params = {"api_key": API_KEY, "engine": search_engine}  # forming the query parameters
    
    if search_engine == "bing":
        params["q"] = query
        params["count"] = 40
        params["mkt"] = "en-GB"
    elif search_engine == "google":
        params["q"] = query
        params["num"] = 40
        params["location"] = location
    elif search_engine == "yandex":
        params["text"] = query
        params["yandex_domain"] = "yandex.ru"
        params["lr"] = 6708
        params["p"] = start
    elif search_engine == "baidu":
        params["q"] = query
        params["rn"] = 40
    elif search_engine == "bing_news":
        params["mkt"] = "en-GB"
        params["first"] = start + 1
        params["count"] = 10
        params["q"] = query
    elif search_engine == "google_news":
        params["engine"] = "google"
        params["tbm"] = "nws"
        params["count"] = 40
        params["q"] = query
        params["start"] = start
    else:
        params["q"] = query
    return params

def format_data( query, location, search_engine, data):
    query_res = Search_Query_Results()
    if 'organic_results' in data:
        data['organic_results'] = list(map(lambda item: {
            **item, 'search_id': query+'||'+location+'||'+search_engine + '||'+current_timestamp_str}, data['organic_results']))
        query_res.organic_results += data['organic_results']
    if 'related_searches' in data:
        if 'bottom' in data['related_searches']:
            data['related_searches']['bottom'] = list(map(lambda item: {
                **item, 'search_id': query+'||'+location+'||'+search_engine + '||'+current_timestamp_str}, data['related_searches']['bottom']))
            query_res.related_searches += data['related_searches']['bottom']
        else:
            data['related_searches'] = list(map(lambda item: {
                                            **item, 'search_id': query+'||'+location+'||'+search_engine + '||'+current_timestamp_str}, data['related_searches']))
            query_res.related_searches += data['related_searches']
    if 'people_also_search_for' in data:
        data['people_also_search_for'] = list(map(lambda item: {
            **item, 'search_id': query+'||'+location+'||'+search_engine + '||'+current_timestamp_str}, data['people_also_search_for']))
        query_res.people_also_search_for += data['people_also_search_for']
    if 'ads' in data:
        data['ads'] = list(map(lambda item: {
            **item, 'search_id': query+'||'+location+'||'+search_engine + '||'+current_timestamp_str}, data['ads']))
        query_res.ads += data['ads']
    if 'questions_and_answers' in data:
        data['questions_and_answers'] = list(map(lambda item: {
            **item, 'search_id': query+'||'+location+'||'+search_engine + '||'+current_timestamp_str}, data['questions_and_answers']))
        query_res.questions_and_answers += data['questions_and_answers']
    if 'related_questions' in data:
        data['related_questions'] = list(map(lambda item: {
            **item, 'search_id': query+'||'+location+'||'+search_engine + '||'+current_timestamp_str}, data['related_questions']))
        query_res.related_questions += data['related_questions']
    if 'twitter_results' in data:
        data['twitter_results'] = list(map(lambda item: {
            **item, 'search_id': query+'||'+location+'||'+search_engine + '||'+current_timestamp_str}, data['twitter_results']['tweets']))
        query_res.twitter_results += data['twitter_results']
    if 'top_stories' in data:
        data['top_stories'] = list(map(lambda item: {
            **item, 'search_id': query+'||'+location+'||'+search_engine + '||'+current_timestamp_str}, data['top_stories']))
        query_res.top_stories += data['top_stories']
    if 'visual_stories' in data:
        data['visual_stories'] = list(map(lambda item: {
            **item, 'search_id': query+'||'+location+'||'+search_engine + '||'+current_timestamp_str}, data['visual_stories']))
        query_res.visual_stories += data['visual_stories']
    if 'news_results' in data:
        data['news_results'] = list(map(lambda item: {
            **item, 'search_id': query+'||'+location+'||'+search_engine + '||'+current_timestamp_str}, data['news_results']))
        query_res.news_results += data['news_results']
    return query_res

def search_serpapi(query, location, search_engine, start = 0):
    query_res = Search_Query_Results()
    base_url = "https://serpapi.com/search"  # base url of the API
    params = form_parameters(query, location, search_engine, start=start)
    # sending the GET request to the API
    response = requests.get(base_url, params=params)
    data = response.json()  # getting the json response
    #next_link = data['serpapi_pagination']['next_link']
    query_res = format_data(query, location, search_engine, data)
    if 'organic_results' in data:
        print(str(len(data['organic_results'])) + ' Search Results Found')
    if 'news_results' in data:
        print(str(len(data['news_results'])) + ' News Results Found')

    return query_res

def save_to_db(query_res):
    for item in query_res.organic_results:
        result = Search_Result(**item)
        session.add(result)
    session.commit()
        
    for item in query_res.news_results:
        result = News_Result(**item)
        session.add(result)
    session.commit()

    for item in query_res.related_searches:
        result = Related_Search(**item)
        session.add(result)

    for item in query_res.people_also_search_for:
        result = People_Also_Search_For(**item)
        session.add(result)

    for item in query_res.ads:
        result = Ad(**item)
        session.add(result)

    for item in query_res.questions_and_answers:
        result = Q_and_A(**item)
        session.add(result)

    for item in query_res.related_questions:
        result = Related_Question(**item)
        session.add(result)

    for item in query_res.top_stories:
        result = Top_Story(**item)
        session.add(result)

    for item in query_res.twitter_results:
        result = Twitter_Result(**item)
        session.add(result)

    for item in query_res.visual_stories:
        result = Visual_Story(**item)
        session.add(result)

    session.commit()

session = connect_to_db()

with open(FILE_NAME, "r", encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    try:
        for row in reader:
            print(row)
            try:
                if(row['engine'] == 'google' or row['engine'] == 'bing' or row['engine'] == 'baidu' ):
                    query_res = search_serpapi(row['query'], row['location'], row['engine'])
                    save_to_db(query_res)
                else:
                    for start in range(0, 20, 10):
                        query_res = search_serpapi(row['query'], row['location'], row['engine'], start=start)
                        save_to_db(query_res)

            except Exception as e:
                traceback.print_exc()
                print(e)
                continue
    finally:
        session.close()