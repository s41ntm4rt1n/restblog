import requests

endpoint='http://localhost:8008/api/articles/'

get_response=requests.get(endpoint)

print(get_response.json())