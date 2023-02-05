import requests

response = requests.get('https://official-joke-api.appspot.com/jokes/ten')
d = []
for i in response.json():
    s = i['type']
    d.append(s)
list(set(d))
    
