import requests

url = 'https://trackapi.nutritionix.com/v2/search/instant?query=date'
headers = {'x-app-id': '42cae472', 'x-app-key': '2d11b9f19d24df0b4657a6c745ab9da8', 'x-remote-user-id': '0'}
response = requests.get(url, headers=headers)
# print(response.content)
print(response.json())
