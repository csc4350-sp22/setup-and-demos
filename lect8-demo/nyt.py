import requests
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"


def article_search(query):
    query_params = {
        "api-key": os.getenv("NYT_KEY"),
        "q": query,
    }

    response = requests.get(
        BASE_URL,
        params=query_params,
    )
    headlines = []
    snippets = []

    # print(json.dumps(response.json(), indent=4, sort_keys=True))
    articles = response.json()["response"]["docs"]
    for article in articles:
        headlines.append(article["headline"]["main"])
        snippets.append(article["snippet"])

    return headlines, snippets
