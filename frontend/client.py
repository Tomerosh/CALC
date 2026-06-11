import requests
while True:
    exp = input('Enter expression: ')
    if exp:
        response = requests.post(f'http://127.0.0.1:8000/solve', params={'expression': exp})
        data = response.json()
        print(data)
        print(data['expression'])
        for step in data['path']:
            print(step['description'])
            print(step['expression'])
        print(data['result'])
    else:
        print('Field Required')