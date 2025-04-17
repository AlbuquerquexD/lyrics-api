import requests
endpoint ="https://api.lyrics.ovh/v1/Seu jorge/Mina do Condomínio"

response = requests.get(endpoint)

key = list(response.json().keys())[0]

data = response.json()[key]

print(data)