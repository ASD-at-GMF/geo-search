
from itertools import product  # importing the product method from itertools library
import requests
import json
import csv
from config import API_KEY

queries = ["russia"]  # , "Ukraine War", "RT"]
locations = ["Greater London"]  # , "Scotland", "Northern Ireland", "Wales"]
search_engines = ["google"]  # , "baidu", "bing", "yahoo", "yandex"]

# ignored = ['search_information', 'knowledge_graph', ]
organic_results = {}
related_searches = {}
people_also_search_for = {}
answer_box = {}
twitter_results = {}
top_stories = {}


def save_to_csv(file_name, dictionary):
    with open(file_name, mode='w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Key', 'Value'])
        for key, value in dictionary.items():
            writer.writerow([key, value])   

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
        print(json.dumps(data, indent=2))  # printing the responsev
        if 'organic_results' in data:
            organic_results[query+'-'+location+'-'+search_engine
                            ] = data['organic_results']
        if 'related_searches' in data:
            related_searches[query+'-'+location+'-'+search_engine
                             ] = data['related_searches']
        if 'people_also_search_for' in data:
            people_also_search_for[query+'-'+location+'-'+search_engine
                                   ] = data['people_also_search_for']
        if 'answer_box' in data:
            answer_box[query+'-'+location+'-'+search_engine
                       ] = data['answer_box']
        if 'twitter_results' in data:
            answer_box[query+'-'+location+'-'+search_engine
                       ] = data['twitter_results']
        if 'top_stories' in data:
            answer_box[query+'-'+location+'-'+search_engine
                       ] = data['top_stories']
        if 'related_questions' in data:
            answer_box[query+'-'+location+'-'+search_engine
                       ] = data['related_questions']

search_serpapi(queries, locations, search_engines)
save_to_csv('organic_results.csv', organic_results)
save_to_csv('related_searches.csv', related_searches)
save_to_csv('people_also_search_for.csv', people_also_search_for)
save_to_csv('answer_box.csv', answer_box)
# print('Organic Results:',organic_results)
# print('Related Searches:',related_searches)
# print('People Also Search For:',people_also_search_for)
# print('Answer Box:',answer_box)
# print('top stories:',top_stories)
# print('twitter results:',twitter_results)
