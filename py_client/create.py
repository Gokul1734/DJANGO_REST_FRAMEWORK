import requests

endpoint = "http://localhost:8000/api/products/"

data = {
   "title":"Iphone 17 Air",
   "price":50000.00
      
}

# post_response = requests.post(endpoint,json=data)

get_response = requests.get(endpoint)
print(get_response.json())