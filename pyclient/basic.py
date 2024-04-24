import requests

endpoint='http://localhost:8008/api/'

get_response=requests.get(endpoint, json={"query":"Hello World"})

print(get_response.json())