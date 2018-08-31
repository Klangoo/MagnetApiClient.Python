# Magnet API Client for Python

# Getting Started

# Supported platforms
Compatibilities:
  * `python 3.x`
  * `python 2.x`

## Install

### Install MagnetAPIClient using pip:

```bash
pip install --upgrade klangooclient
```
### Install MagnetAPIClient using Manually:
Download and add to your project the file [MagnetAPIClient.py](https://github.com/Klangoo/MagnetApiClient.Python/blob/master/klangooclient/MagnetAPIClient.py) if your are using python 3.x or [MagnetAPIClientV2.py](https://github.com/Klangoo/MagnetApiClient.Python/blob/master/klangooclient/MagnetAPIClientV2.py) if your are using python 2.x

## Quick Start

This quick start tutorial will show you how to process a text

### Initialize the client

To begin, you will need to initialize the client. In order to do this you will need your API Key **CALK** and **Secret Key**.
You can find both on [your Klangoo account](https://connect.klangoo.com/).

```python
from klangooclient.MagnetAPIClient import MagnetAPIClient # install using PIP with python 3.x
#from klangooclient.MagnetAPIClientV2 import MagnetAPIClient # install using PIP with python 2.x
#from MagnetAPIClient import MagnetAPIClient # install manually with python 3.x
#from MagnetAPIClientV2 import MagnetAPIClient # install manually with python 2.x

ENDPOINT ='https://nlp.klangoo.com/Service.svc'
CALK ='enter your calk here'
SECRET_KEY ='enter your secret key here'

client = MagnetAPIClient(ENDPOINT, CALK, SECRET_KEY)

request = { 'text' : 'Real Madrid transfer news', 'lang' : 'en', 'format' : 'json' }

json = client.callwebmethod('ProcessDocument', request, 'POST')
```