import requests
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

MEDIA_TYPE = "viewed"
PERIOD = 1

BASE_URL = f"https://api.nytimes.com/svc/mostpopular/v2/{MEDIA_TYPE}/{PERIOD}.json"

query_params = {
    "api-key": os.getenv("NYT_KEY"),
}

most_popular_response = requests.get(
    BASE_URL,
    params=query_params,
)

search_response = requests.get(OTHER_URL, params=other_query_params)

# print(json.dumps(response.json(), indent=4, sort_keys=True))
articles = response.json()["results"]
for article in articles[:10]:
    print(article["title"])
