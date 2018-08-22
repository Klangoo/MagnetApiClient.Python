
from klangooclient.MagnetAPIClientV3 import MagnetAPIClient

ENDPOINT ='https://nlp.klangoo.com/Service.svc'
CALK ='3D5F1F4B-1C47-40D7-B687-476C55EB591A'
SECRET_KEY ='zrKEvs8kISrVzpWp4e5xqxqBiX4HSD9NqJfYpWRa'

client = MagnetAPIClient(ENDPOINT, CALK, SECRET_KEY)

request = { 'text' : 'Hello \'World.\nThis \'is\' the system.', 'lang' : 'en', 'format' : 'json' }

json = client.callwebmethod('ProcessDocument', request, 'POST')
print(json)