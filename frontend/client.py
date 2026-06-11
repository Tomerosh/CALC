import requests

exp = input('Enter expression: ')
response = requests.post(f'http://10.0.0.17:8000/solve', params={'expression': exp})
print(response.json())