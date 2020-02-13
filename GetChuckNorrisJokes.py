import json, random
from urllib.request import Request, urlopen

import null as null

chosen_category = 'scienceefaew'
search_query = 'newtoeafafn'

def jokeCategory(category):

    url_of_available_categories = 'https://api.chucknorris.io/jokes/categories'
    available_categories = Request(url_of_available_categories, headers={'User-Agent': 'Mozilla/5.0'})

    non_decoded_categories = urlopen((available_categories)).read()

    decoded_categories = non_decoded_categories.decode('utf-8')

    deserialized_categories = json.loads(decoded_categories)

    if(category not in deserialized_categories):
        return None

    url = 'https://api.chucknorris.io/jokes/random?category=' + category
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    non_decoded_page= urlopen(req).read()

    decoded_page = non_decoded_page.decode('utf-8')

    deserialized_page = json.loads(decoded_page)

    if(len(deserialized_page) == 0):
        return None

    return deserialized_page['value']


def jokeSearch(query):

    url = 'https://api.chucknorris.io/jokes/search?query=' + query
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    non_decoded_page= urlopen(req).read()

    decoded_page = non_decoded_page.decode('utf-8')

    deserialized_page = json.loads(decoded_page)

    all_results = deserialized_page['result']

    if(len(all_results) == 0):
        return None

    random_joke_from_results = all_results[random.randrange(0, len(all_results))]

    joke = random_joke_from_results['value']

    return joke


print(jokeCategory(chosen_category))
print(jokeSearch(search_query))
