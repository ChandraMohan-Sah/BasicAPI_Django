import requests
endpoint = "http://127.0.0.1:8000/api/products/15"


# Featching Product Details.

x = requests.get(endpoint)
print(x.json())





