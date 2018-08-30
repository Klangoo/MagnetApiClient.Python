# Magnet API Client for Python


# Getting Started


## Install

Install MagnetAPIClient using pip:

```bash
pip install --upgrade klangooclient
```


## Quick Start

This quick start tutorial will show you how to process a text

### Initialize the client

To begin, you will need to initialize the client. In order to do this you will need your API Key **CALK** and **Secret Key**.
You can find both on [your Klangoo account](https://connect.klangoo.com/).

```python
from klangooclient.MagnetAPIClient import MagnetAPIClient

ENDPOINT ='https://nlp.klangoo.com/Service.svc'
CALK ='enter your calk here'
SECRET_KEY ='enter your secret key here'

client = MagnetAPIClient(ENDPOINT, CALK, SECRET_KEY)

request = { 'text' : 'Real Madrid transfer news', 'lang' : 'en', 'format' : 'json' }

json = client.callwebmethod('ProcessDocument', request, 'POST')
```