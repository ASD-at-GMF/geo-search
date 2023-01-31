
from itertools import product  # importing the product method from itertools library
import requests
import json
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#Internal Imports
from config import API_KEY, SERVER_URL, DATABASE, DB_USERNAME, DB_PASSWORD
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

queries = ["Scottish Independence"]#, "Ukraine War", "RT"]
locations = ["Greater London" ]#, "Scotland", "Northern Ireland", "Wales"]
search_engines = ["google"]# , "baidu", "bing", "yahoo", "yandex"]

current_timestamp_str = str(int(time.time()))

# ignored = ['search_information', 'knowledge_graph', ]
query_res = Search_Query_Results()


def search_serpapi(queries, locations, search_engines):
    api_key = API_KEY
    base_url = "https://serpapi.com/search"  # base url of the API
    # iterating through all the possible combinations of queries, locations, and search engines
    for query, location, search_engine in product(queries, locations, search_engines):
        params = {"q": query, "location": location, "api_key": api_key,
                  "engine": search_engine, "num": 40}  # forming the query parameters
        # sending the GET request to the API
        response = requests.get(base_url, params=params)
        data = response.json()  # getting the json response
        print(json.dumps(data, indent=2))  # printing the response
        if 'organic_results' in data:
            data['organic_results'] = list(map(lambda item: {**item, 'search_id': query+'||'+location+'||'+search_engine +'||'+current_timestamp_str}, data['organic_results']))
            query_res.organic_results +=  data['organic_results']
        if 'related_searches' in data:
            data['related_searches'] = list(map(lambda item: {**item, 'search_id': query+'||'+location+'||'+search_engine +'||'+current_timestamp_str}, data['related_searches']))
            query_res.related_searches  +=  data['related_searches']
        if 'people_also_search_for' in data:
            data['people_also_search_for'] = list(map(lambda item: {**item, 'search_id': query+'||'+location+'||'+search_engine +'||'+current_timestamp_str}, data['related_searches']))
            query_res.people_also_search_for  +=  data['people_also_search_for']
        if 'ads' in data:
            data['ads'] = list(map(lambda item: {**item, 'search_id': query+'||'+location+'||'+search_engine +'||'+current_timestamp_str}, data['ads']))
            query_res.ads +=   data['ads']
        if 'questions_and_answers' in data:
            data['questions_and_answers'] = list(map(lambda item: {**item, 'search_id': query+'||'+location+'||'+search_engine +'||'+current_timestamp_str}, data['questions_and_answers']))
            query_res.questions_and_answers  +=  data['questions_and_answers']
        if 'related_questions' in data:
            data['related_questions'] = list(map(lambda item: {**item, 'search_id': query+'||'+location+'||'+search_engine +'||'+current_timestamp_str}, data['related_questions']))
            query_res.related_questions  +=  data['related_questions']
        if 'twitter_results' in data:
            data['twitter_results'] = list(map(lambda item: {**item, 'search_id': query+'||'+location+'||'+search_engine +'||'+current_timestamp_str}, data['twitter_results']['tweets']))
            query_res.twitter_results  +=  data['twitter_results']
        if 'top_stories' in data:
            data['top_stories'] = list(map(lambda item: {**item, 'search_id': query+'||'+location+'||'+search_engine +'||'+current_timestamp_str}, data['top_stories']))
            query_res.top_stories  +=  data['top_stories']
        if 'visual_stories' in data:
            data['visual_stories'] = list(map(lambda item: {**item, 'search_id': query+'||'+location+'||'+search_engine +'||'+current_timestamp_str}, data['visual_stories']))
            query_res.visual_stories  +=  data['visual_stories'] 

search_serpapi(queries, locations, search_engines)
print(query_res.organic_results)
# # Define the connection string
connection_string = 'postgresql+psycopg2://'+DB_USERNAME+':'+DB_PASSWORD+'@'+SERVER_URL+'/'+DATABASE

# Create the SQLAlchemy engine
engine = create_engine(connection_string)

# Connect to the database
connection = engine.connect()
Base = declarative_base()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

try:
    for item in query_res.organic_results:
        result = Search_Result(**item)
        session.add(result)

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
finally:
    session.close()