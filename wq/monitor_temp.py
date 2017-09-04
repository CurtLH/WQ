from wq import cli as wq
import psycopg2
from datetime import datetime
import json
from time import sleep

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
cur.execute("""CREATE TABLE IF NOT EXISTS arlington_weather
               (id SERIAL PRIMARY KEY NOT NULL,
                datetime timestamp NOT NULL,
                weather jsonb NOT NULL)""")

# load API key
key = wq.load_key("/home/curtis/etc/wunderground")

# build API request
url = wq.build_request(key, database='conditions', city='Arlington', state='VA')

# continuously get weather
while True:

    # get results
    r = wq.get_request(url) 

    # get current datetime
    dt_now = datetime.now()

    # put reading into databse
    cur.execute("""INSERT INTO arlington_weather 
                   (datetime, weather) 
                   VALUES (%s, %s)""", [dt_now, json.dumps(r)])

    # sleep for 15 minutes
    print(dt_now)
    sleep(900)
