import requests

r = requests.get("http://127.0.0.1:5000/Dados")
dic = r.json()

print("Nome: " + dic['Nome'])

print("Idade: " + dic['Idade'])

print("Telefone: " + dic['Telefone'])

print ("Status de requisição: ", r.status_code)
