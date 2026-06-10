import requests

exp = input('Enter expression: ')
response = requests.post(f'http://127.0.0.1:8000/solve/{exp}')
print(response.json())