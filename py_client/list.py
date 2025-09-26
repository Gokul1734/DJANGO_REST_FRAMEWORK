import requests
from getpass import getpass

auth_endpoint = 'http://localhost:8000/api/auth/'
username = input('Enter username: ')
password = getpass('Enter password: ')

auth_response = requests.post(auth_endpoint,json={'username':username,'password':password})

token = auth_response.json()['token']
print(token)
# headers = {
#    'Authorization': f'Bearer {token}'
# }
endpoint = "http://localhost:8000/api/products/1"
poster = requests.get(endpoint)
print(poster.json())