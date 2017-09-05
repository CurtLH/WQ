import logging
from wq import wunderground as wg
import psycopg2
from datetime import datetime
import json
from time import sleep


# enable logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# connect to the databse
conn = psycopg2.connect(database="postgres",
                        user="postgres",
                        password="apassword",
                        host="192.168.0.105",
                        port="5432")

# enable autocommit
conn.autocommit = True

# define cursor
cur = conn.cursor()

# create a table
cur.execute("""CREATE TABLE IF NOT EXISTS arlington_weather_forecast
               (id SERIAL PRIMARY KEY NOT NULL,
                datetime timestamp NOT NULL,
                forecast jsonb NOT NULL)""")

# load API key
key = wg.load_key("/home/curtis/etc/wunderground")

# build API request
url = wg.build_request(key, database='forecast', city='Arlington', state='VA')

# get results
r = wg.get_request(url) 

# get current datetime
dt_now = datetime.now()

# put reading into databse
cur.execute("""INSERT INTO arlington_weather_forecast
               (datetime, forecast) 
               VALUES (%s, %s)""", [dt_now, json.dumps(r)])

# log event
logger.info("Weather forcast updated")
