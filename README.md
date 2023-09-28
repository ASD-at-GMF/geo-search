# SERP API Searcher

Ingests a list of searches (as defined in in searches.csv) and calls the SERP API to grab search or news results, then inserts the results (and related objects) into a PostgresSQL database.  

Requires a file 'config.py' not included in this repo in the root of this directory:

    API_KEY = "<SERPAPI API KEY>"
    SERVER_URL = '<URL or IP of Postgres database. May need port number>'
    DATABASE = '<database name>'
    DB_USERNAME = "<username of account used to access the database"
    DB_PASSWORD = "samplePassword12@!"
    FILE_NAME = "<local path to searches.csv; e.g. /usr/peter/repo/geo-search/searches. "

## searches.csv definition
| Header   | Definition                        | Example/Possiblities                                 |
|----------|-----------------------------------|------------------------------------------------------|
| query    | The term or phrase to be searched | Xi Jinping                                           |
| location | A geolocation to search           | Greater London, England, etc.                        |
| engine   | Search engine to search           | google, google_news, bing, bing_news, baidu, yandex  |

## Result Objects
These are the SQL objects created by the code and inserted into the database  

### Ads
ad.py is a SQLAlchemy ORM object that represents an advertisement retrieved from the SERP API. It contains information such as the ad's headline, description, and targeting data.

### news_result
news_result is a SQLAlchemy ORM object that represents a news article retrieved from the SERP API. It contains information such as the article's headline, author, publication date, and content.

### people_also_search_for
people_also_search_for is a SQLAlchemy ORM object that represents a list of related search queries retrieved from the SERP API. It contains information such as the query term and the related queries themselves.

### q_and_a
q_and_a is a SQLAlchemy ORM object that represents a question and answer retrieved from the SERP API. It contains information such as the question text, answer text, and the source of the answer.

### related_search
related_search is a SQLAlchemy ORM object that represents a list of related search queries retrieved from the SERP API. It contains information such as the query term and the related queries themselves.

### related_question
rq (related_question) is a SQLAlchemy ORM object that represents a related question retrieved from the SERP API.

### search_query_results
search_query_results is a SQLAlchemy ORM object that represents the results of a SERP API search query. It contains information such as the query term, the type of search conducted, the number of results returned, and the list of individual search results.

### search_result
search_result is a SQLAlchemy ORM object that represents an individual search result retrieved from the SERP API. It contains information such as the result's title, description, URL, and any other relevant metadata.

### top_story
top_story is a SQLAlchemy ORM object that represents a news article or other content item that is featured as a "top story" on a SERP. It contains information such as the item's headline, summary, and publication information.

### twitter_result
twitter_result is a SQLAlchemy ORM object that represents a tweet retrieved from the SERP API. It contains information such as the tweet text, author, timestamp, and any associated media (e.g. images, videos).

### visual_story
visual_story is a SQLAlchemy ORM object that represents a visually-rich content item featured on a SERP, such as an image gallery or video carousel. It contains information such as the item's title, description, and any associated media.
