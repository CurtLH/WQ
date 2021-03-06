import requests
from pprint import pprint
from time import sleep

def load_key(path_to_key):

    """
    loads API key to be used in request
    """

    return open(path_to_key).read().strip()



def databases():

    return ['alerts', 'almanac', 'astronomy', 'conditions', 'currenthurricane', 'forecast', 'forecast10day', 'geolookup', 'history', 'hourly', 'hourly10day', 'planner', 'rawtide', 'satellite', 'tide', 'webcams', 'yesterday']


def build_request(key, database='conditions', city='Arlington', state='VA'):

    """
    creates the approproiate API query URL
    """

    url = "https://api.wunderground.com/api/{}/{}/q/{}/{}.json".format(key, database, state, city)

    return url


def get_request(url):


    """
    fetch the response given the URL
    """

    num_try = 0
    while num_try < 5:
        try:
            s = requests.session()
            r = s.get(url)
            return r.json()
            break

        except:
            num_try += 1
            sleep(10)
            
    pass
