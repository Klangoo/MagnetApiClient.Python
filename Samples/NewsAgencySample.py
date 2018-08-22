#!/usr/bin/env python
# -- coding: UTF-8 --

"""
   Magnet API News Agency Sample
   Copyright 2018, Klangoo Inc.
"""
import sys
import xml.etree.ElementTree as ET
from klangooclient.MagnetAPIClient import MagnetAPIClient

# Constants
ENDPOINT_URI = 'https://magnetapi.klangoo.com/NewsAgencyService.svc';
CALK = ''; # use your own CALK
SECRET_KEY = ''; # use your own Secret Key

# API XML Namespace
NAMESPACE = {'api': 'http://schemas.datacontract.org/2004/07/API.Shared'}

# Initialize Magnet API Client
magnet_api_client = MagnetAPIClient(ENDPOINT_URI, CALK, SECRET_KEY)


def main():
	# call api method 'GetArticleEntities'
	get_article_entities('428561053');
	
	# call api method 'GetArticle'
	#get_article('428561053');
	
	# call api method 'ShowIndex'
	#show_index();
	
def get_article_entities(articleUID):
	try:
		request = { 'articleUID' : articleUID, 'format' : 'xml' }
			 
		response = magnet_api_client.callwebmethod('GetArticleEntities', request, 'GET')	
		
		xmlDoc = ET.ElementTree(ET.fromstring(response)).getroot()
		
		if get_api_status(xmlDoc) == 'OK':
			print 'GetArticleEntities:\n'
			print response + '\n';
		else:
			handle_api_error(xmlDoc)
	except:
		print 'Caught exception: ', sys.exc_info()[0]
		
def get_article(articleUID):
	try:
		request = { 'articleUID' : articleUID, 'format' : 'xml' }
			 
		response = magnet_api_client.callwebmethod('GetArticle', request, 'GET')	
		
		xmlDoc = ET.ElementTree(ET.fromstring(response)).getroot()
		
		if get_api_status(xmlDoc) == 'OK':
			print 'GetArticle:\n'
			print response + '\n';
		else:
			handle_api_error(xmlDoc)
	except:
		print 'Caught exception: ', sys.exc_info()[0]
		
def show_index():
	try:
		request = { 'page' : '0', 'orderByDate' : 'true', 'format' : 'xml' }
			 
		response = magnet_api_client.callwebmethod('ShowIndex', request, 'GET')	
		
		xmlDoc = ET.ElementTree(ET.fromstring(response)).getroot()
		
		if get_api_status(xmlDoc) == 'OK':
			print 'ShowIndex:\n'
			print response + '\n';
		else:
			handle_api_error(xmlDoc)
	except:
		print 'Caught exception: ', sys.exc_info()[0]
		
def get_api_status(xmlDoc):
	return xmlDoc.find('api:status', NAMESPACE).text

	
def handle_api_error(xmlDoc):
	error = xmlDoc.find('api:error', NAMESPACE);
	errorNo = error.find('api:errorNo', NAMESPACE).text;
	errorMessage = ''
	errorMessageElm = error.find('api:errorMessage', NAMESPACE)
	if errorMessageElm != None:
		errorMessage = errorMessageElm.text
	print 'Error occured -- errorNo: ', errorNo, ' -- errorMessage: ', errorMessage
	

if __name__ == '__main__':
    main()