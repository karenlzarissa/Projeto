from flask import Flask, jsonify

app = Flask("Projeto")

@app.route("/Dados", methods=["GET"])
def info():
    return jsonify({"Nome": "Karen Larissa Lima dos Santos",
                    "Idade": "20",
                    "Telefone": "984845619",
           })
           
app.run()
