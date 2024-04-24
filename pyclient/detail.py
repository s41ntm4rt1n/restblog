import requests

endpoint='http://localhost:8008/api/articles/1/'

get_response=requests.get(endpoint)

print(get_response.json())