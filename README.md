**This library allows you to easily use the Magnet API via Python.**

# Table of Contents

* [About](#about)
* [Installation](#installation)
* [Usage](#usage)

<a name="about"></a>
# About

Klangoo NLP API is a natural language processing (NLP) service that uses the rule-based paradigm and machine learning to recognize the aboutness of text. The service recognizes the category of the text, extracts key disambiguated topics, places, people, brands, events, and 41 other types of names; analyzes text using tokenization, parts of speech, parsing, word sense disambiguation, named entity recognition; and automatically finds the relatedness score between documents.

[Read More](https://klangoosupport.zendesk.com/hc/en-us/categories/360000812171-Klangoo-Natural-Language-API).

[Signup for a free trail](https://connect.klangoo.com/pub/Signup/)

<a name="installation"></a>
# Installation

## Prerequisites

- This library is compatible with python 3.x and python 2.x
- An API Key Provided by [Klangoo](https://klangoosupport.zendesk.com/hc/en-us/articles/360015236872-Step-2-Registering-to-Klangoo-NLP-API)
- An API Secret Provided by [Klangoo](https://klangoosupport.zendesk.com/hc/en-us/articles/360015236872-Step-2-Registering-to-Klangoo-NLP-API)


## Install

### Install MagnetAPIClient using pip:

```bash
pip install --upgrade klangooclient
```
### Install MagnetAPIClient manually:
Download and add to your project the file [MagnetAPIClient.py](https://github.com/Klangoo/MagnetApiClient.Python/blob/master/klangooclient/MagnetAPIClient.py) if your are using python 3.x or [MagnetAPIClientV2.py](https://github.com/Klangoo/MagnetApiClient.Python/blob/master/klangooclient/MagnetAPIClientV2.py) if your are using python 2.x

<a name="usage"></a>
# Usage

This quick start tutorial will show you how to process a text.

## Initialize the client

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

rsp = client.callwebmethod('ProcessDocument', request, 'POST')
```
