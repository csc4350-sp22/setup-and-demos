import requests


def get_wiki_link(movie_name):
    """
    Given a movie name, query Wikipedia using the search API and return a link to the top
    result.
    """
    wiki_response = requests.get(
        "https://en.wikipedia.org/w/api.php",
        params={
            "action": "query",
            "format": "json",
            "prop": "info",
            "inprop": "url",
            "titles": [f"{movie_name}"],
        },
    )
    json_response = wiki_response.json()
    hits = json_response["query"]["pages"]
    return next(iter(hits.values()))["fullurl"]
