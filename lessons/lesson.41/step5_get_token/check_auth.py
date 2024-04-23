import requests

url = 'http://127.0.0.1:8000/api/animals/'

response = requests.get(url)
print(response.status_code)
assert response.status_code, 401

# базовая авторизация
response = requests.get(url, auth=('admin', 'admin'))
print(response.status_code)
assert response.status_code, 200

# по токену
TOKEN = '52a9c3619c96f478e9b92f4709c6abf2b5134f11'
headers = {
    'Authorization': f'Token {TOKEN}'
}

response = requests.get(url, headers=headers)
print(response.status_code)
assert response.status_code, 200
