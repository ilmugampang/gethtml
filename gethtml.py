import requests

req = requests.get("https://www.google.com")

content = req.content
print(content)


