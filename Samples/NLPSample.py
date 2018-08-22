#!/usr/bin/env python
# -- coding: UTF-8 --

"""
   Magnet API NLP Sample
   Copyright 2018, Klangoo Inc.
"""

from klangooclient.MagnetAPIClient import MagnetAPIClient

ENDPOINT = 'https://nlp.klangoo.com/Service.svc'
CALK = 'enter your calk here'
SECRET_KEY = 'enter your secret key here'

client = MagnetAPIClient(ENDPOINT, CALK, SECRET_KEY)

def test_process_document():
	request = { 'text' : 'The United States of America (USA), commonly known as the United States (U.S.) or America, is a federal republic composed of 50 states, a federal district, five major self-governing territories, and various possessions.', 
	'lang' : 'en', 'format' : 'json' }
	json = client.callwebmethod('ProcessDocument', request, 'POST')
	print('\nProcess Document:')
	print(json)
	
def test_get_summary():
	request = { 'text' : 'The United States of America (USA), commonly known as the United States (U.S.) or America, is a federal republic composed of 50 states, a federal district, five major self-governing territories, and various possessions.', 
	'lang' : 'en', 'format' : 'json' }
	json = client.callwebmethod('GetSummary', request, 'POST')
	print('\nGet Summary:')
	print(json)
	
def test_get_entities():
	request = { 'text' : 'The United States of America (USA), commonly known as the United States (U.S.) or America, is a federal republic composed of 50 states, a federal district, five major self-governing territories, and various possessions.', 
	'lang' : 'en', 'format' : 'json' }
	json = client.callwebmethod('GetEntities', request, 'POST')
	print('\nGet Entities:')
	print(json)
	
def test_get_categories():
	request = { 'text' : 'The United States of America (USA), commonly known as the United States (U.S.) or America, is a federal republic composed of 50 states, a federal district, five major self-governing territories, and various possessions.', 
	'lang' : 'en', 'format' : 'json' }
	json = client.callwebmethod('GetCategories', request, 'POST')
	print('\nGet Categories:')
	print(json)
	
def test_get_key_topics():
	request = { 'text' : 'The United States of America (USA), commonly known as the United States (U.S.) or America, is a federal republic composed of 50 states, a federal district, five major self-governing territories, and various possessions.', 
	'lang' : 'en', 'format' : 'json' }
	json = client.callwebmethod('GetKeyTopics', request, 'POST')
	print('\nGet Key Topics:')
	print(json)
	
if __name__ == "__main__":
	test_process_document()
	test_get_summary()
	test_get_entities()
	test_get_categories()
	test_get_key_topics()