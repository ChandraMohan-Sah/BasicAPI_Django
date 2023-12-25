import requests

endpoint = "http://localhost:8000/api/products/listcreate/"


# In this example request body is a JSON object.
data = {
    "title": "Jambo",
    "price":124,
}

x = requests.post(endpoint, json=data)
print(x.json())




