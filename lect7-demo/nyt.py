import os

import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # This is to load your API keys from .env

BASE_URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'

def get_article_data(keyword):
    """ Returns a list of headlines about a given topic """

    params = {
        'q': keyword,
        'api-key': os.getenv('NYT_KEY'),
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()
    articles = data['response']['docs']

    def get_headline(article):
        return article['headline']['main']

    def get_snippet(article):
        return article['snippet']

    headlines = map(get_headline, articles)
    snippets = map(get_snippet, articles)

    return {
        'headlines': list(headlines),
        'snippets': list(snippets),
    }
