import requests
from getpass import getpass

# auth_endpoint = 'http://localhost:8000/api/auth/'
# username = input('Enter username: ')
# password = getpass('Enter password: ')

# auth_response = requests.post(auth_endpoint,json={'username':username,'password':password})

# token = auth_response.json()['token']
# print(token)
# headers = {
#    'Authorization': f'Bearer {token}'
# }
# endpoint = "http://localhost:8000/api/products/"
# poster = requests.get(endpoint,headers=headers)
# print(poster.json())


url = "http://localhost:8000/api/token/"  # JWT login endpoint
data = {
    "username": "gokul1734",
    "password": "1234"
}

res = requests.post(url, data=data)
if res.status_code == 200:
    tokens = res.json()
    print("Access:", tokens["access"])
    print("Refresh:", tokens["refresh"])
else:
    print("Login failed:", res.json())
