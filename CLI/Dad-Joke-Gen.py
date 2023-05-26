import requests

try:
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})

    if response.status_code == 200:
        data = response.json()
        print(data['joke'])
    else:
        print('Failed to retrieve joke')
except Exception as e:
    print(f'An error occurred: {e}')
