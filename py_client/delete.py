import requests

pk = int(input("Enter a product ID to delete: "))

endpoint = f'http://localhost:8000/api/products/{pk}/delete'

viewpoint = f'http://localhost:8000/api/products/{pk}'

print('Deleted Data: ',requests.get(viewpoint).json())

delete_response = requests.delete(endpoint)

print('Status Code:', delete_response.status_code)

