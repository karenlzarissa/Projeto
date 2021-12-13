import requests

r = requests.get("http://127.0.0.1:5000/Dados")
r.status_code
print(r.json)
