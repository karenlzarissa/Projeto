from flask import Flask
import requests

app = Flask("Teste")

@app.route("/Pessoa", methods=["GET"])
def olaMundo():
    return {"nome": "Karen Larissa Lima dos Santos",
        "idade": "20",
        "telefone": "984845619",
        "status_req": "status"}
        
app.run()