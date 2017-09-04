import click
import requests
from pprint import pprint
from time import sleep

def load_key(path_to_key):

    """
    loads API key to be used in request
    """

    return open(path_to_key).read().strip()



def build_request(key, city='Arlington', state='VA'):

    """
    creates the approproiate API query URL
    """

    url = "https://api.wunderground.com/api/{}/conditions/q/{}/{}.json".format(key, state, city)

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


@click.command()
@click.argument('city')
@click.argument('state')
def cli(city, state):

    # load API key
    key = load_key("/home/curtis/etc/wunderground")

    # build API request
    url = build_request(key, city=city, state=state)

    # get results
    r = get_request(url)

    # print results
    pprint(r)

