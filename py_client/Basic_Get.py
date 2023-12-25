import requests

endpoint = "http://127.0.0.1:8000/api/"


# In this example request body is a JSON object.
data = {
    "title": "Examin-Requests",
    "content": "Hello World",
    "price":124,
}

x = requests.get(endpoint, 
    params={'abc':"urlsparameters"},
    json=data
    )

print(x.json())

