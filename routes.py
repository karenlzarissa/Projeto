from flask import Flask
import requests

app = Flask("Projeto")

@app.route("/Dados", methods=["GET"])
def info():
    return {"Nome": "Karen Larissa Lima dos Santos",
        "Idade": "20",
        "Telefone": "984845619",
        }
app.run()
