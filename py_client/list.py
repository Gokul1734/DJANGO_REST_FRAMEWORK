import requests

endpoint = "http://localhost:8000/api/products/1"

poster = requests.get(endpoint)

print(poster.json())