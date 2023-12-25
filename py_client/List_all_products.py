import requests

endpoint = "http://localhost:8000/api/products/list/"


# In this example request body is a JSON object.
x = requests.get(endpoint)
print(x.json())




