import requests

endpoint='http://localhost:8008/api/articles/1/'

data={
    "category":'AI',
    'title':'what you need to know about Artificial Intelligence',
    'author':'outis',
}
get_response=requests.post(endpoint, json=data)

print(get_response.json())