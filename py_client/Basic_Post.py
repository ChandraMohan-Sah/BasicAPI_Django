import requests

endpoint = "http://127.0.0.1:8000/api/post/"


# In this example request body is a JSON object.
data = {
    "title": "Examin-Requests",
    "content": "Hello World",
    "price":124,
}

x = requests.post(endpoint, 
    params={'abc':"urlsparameters",},
    json=data
    )



#print(x.text) # print raw text response
#print(x.status_code)
print(x.json())


'''
HTTP Request -> HTML
REST API HTTP Request -> JSON
Javascript Object Notation ~ Python Dict
'''