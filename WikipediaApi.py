import requests

url = "https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&utf8=1&formatversion=2&srsearch=apples"
response = requests.get(url)
data = response.json()

print(data)
