import click
import requests
from pprint import pprint

def load_key(path_to_key):

    """
    loads API key to be used in request
    """

    return open(path_to_key).read().strip()



def build_request(key, state='VA', city='Arlington'):

    """
    creates the approproiate API query URL
    """

    url = "https://api.wunderground.com/api/{}/conditions/q/{}/{}.json".format(key, state, city)

    return url


def get_request(url):


    """
    fetch the response given the URL
    """

    s = requests.session()
    r = s.get(url)

    return r.json()


# load API key
key = load_key("/home/curtis/etc/wunderground")

# build API request
url = build_request(key, state='VA', city='Arlington')

# get results
r = get_request(url)

# print results
pprint(r)

