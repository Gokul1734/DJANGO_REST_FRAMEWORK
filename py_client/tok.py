import requests

BASE_URL = "http://localhost:8000/api"

# 1️⃣ Get access/refresh tokens
login_res = requests.post(f"{BASE_URL}/token/", json={
    "username": "gokul1734",
    "password": "1234"
})

print("Status:", login_res.status_code)
print("Response:", login_res.text)

if login_res.status_code == 200:
    tokens = login_res.json()
    access = tokens["access"]
    refresh = tokens["refresh"]

    # 2️⃣ Use access token to call protected endpoint
    headers = {"Authorization": f"Bearer {access}"}
    products_res = requests.get(f"{BASE_URL}/products/", headers=headers)
    print(products_res.status_code, products_res.json())

    # 3️⃣ Refresh access token if expired
    refresh_res = requests.post(f"{BASE_URL}/token/refresh/", json={"refresh": refresh})
    print("Refresh:", refresh_res.status_code, refresh_res.text)
