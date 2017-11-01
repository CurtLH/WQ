# WQ: Weather Query

![https://img.shields.io/travis/curtlh/wq.svg](https://travis-ci.org/curtlh/wq)

Command line interface for querying Wunderground API

For more information about the Wunderground Weather API, visit https://www.wunderground.com/weather/api/d/docs

## Installiation

Clone the `wq` repo from github

```
git clone https://github.com/CurtLH/WQ.git
```

Navigate into the `wq` directory and install on your machine

```bash
$ cd WQ
$ pip install -e .
```

## Documentation

``` bash
$ wq --help
```

## Example

```python
from wq import cli as wq
from pprint import pprint

# load the API key
key = wq.load_key('/home/curtis/etc/wunderground')

# build the request URL
url = wq.build_request(key, database='forecast', city='Arlington', state='VA')

# query the API
r = wq.get_request(url)

# print the response
pprint(r)
```
