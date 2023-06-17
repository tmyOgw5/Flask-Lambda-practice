import requests

url = ''

response = requests.get(url)
print(response.text)

submit_data = {
    'user_id': 'TaroYamada',
    'password': 'Pass'
}

new_url = url + '/kake'
response = requests.post(
    new_url,
    json=submit_data
)
print(response.text)
