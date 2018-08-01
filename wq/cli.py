import click
from wq import wunderground as wg
from pprint import pprint

@click.command()
@click.version_option()
@click.option('--database', type=click.Choice(wg.databases()), default='conditions')
@click.argument('city')
@click.argument('state')
def cli(database, city, state):

    """
    API Access to Wunderground
    """

    # load API key
    key = wg.load_key("/home/curtis/etc/wunderground")

    # build API request
    url = wg.build_request(key, database, city=city, state=state)

    # get results
    r = wg.get_request(url)

    # print results
    pprint(r)

