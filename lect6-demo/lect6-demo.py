import requests
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

MEDIA_TYPE = "viewed"
PERIOD = 1

BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

query_params = {
    "api-key": os.getenv("NYT_KEY"),
    "q": "Apple",
}

response = requests.get(
    BASE_URL,
    params=query_params,
)

# print(json.dumps(response.json(), indent=4, sort_keys=True))
articles = response.json()["response"]["docs"]
for article in articles:
    print(article["headline"]["main"])
