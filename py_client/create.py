import requests

headers = {'Authorization': 'Bearer af3eb5e885a919ec0f921dcaf21243e5ff2bf19d'}
endpoint = "http://localhost:8000/api/products/"

data = {
   "title":"Iphone 17 Air",
   "price":50000.00
      
}

# post_response = requests.post(endpoint,json=data)

get_response = requests.post(endpoint,headers=headers,json=data)
print(get_response.json())