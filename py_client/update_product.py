import requests

endpoint = "http://127.0.0.1:8000/api/products/27/update/"


# In this example request body is a JSON object.
data = {
    "title": "Updated-Value2",
    "content": "Hello World",
    "price":124,
}

x = requests.put(endpoint, 
    params={'abc':"urlsparameters"},
    json=data
    )
print(x.json())

