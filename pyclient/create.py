import requests

endpoint='http://localhost:8008/api/articles/'

data={
    "category":'IT',
    'title':'what you need to know about internet security',
    'author':'outis',
    'body':'this is not a body',
}
get_response=requests.post(endpoint, json=data)

print(get_response.json())