from flask import Flask, app, request
from flask.json import jsonify
import json

app = Flask(__name__)

Receitas = [
    {
        "Receita": "Beijinho de Coco",
        "Ingredientes": [
            "1 Leite MOÇA® (lata ou caixinha) 395 g"
            "1 colher (sopa) de manteiga"
            "4 colheres (sopa) de coco seco ralado"
            "coco seco ralado para passar os docinhos"
            "40 cravos-da-índia para decorar"
        ],
        "Modo de preparo": "1-Em uma panela, coloque o Leite MOÇA e a manteiga."

            "2-Leve ao fogo baixo, mexendo sempre até desprender do fundo da panela."
            
            "3-Retire do fogo, misture o coco, coloque em um prato untado com manteiga e deixe esfriar."
            
            "4-Enrole os docinhos, passe pelo coco ralado e decore-os com um cravo."
    
            "5-Coloque em forminhas de papel.",
        "Redimento": "¨40 Porções"
    },
]


@app.route("/rotaApiRest", methods=["POST", "GET"])
def Cadastro():
    if request.method == "GET":
        return jsonify(Receitas)
    elif request.method == "POST":
        newcadastro = json.loads(request.data)
        Receitas.append(newcadastro)
        return jsonify({
            "menssagem": "Cadastrado",
            "newValue": newcadastro

        })


@app.route('/rotaApiRest/<int:indice>', methods=['GET', 'PUT', 'DELETE'])
def cadastroID(indice):
    try:
        Receitas[indice]
    except IndexError:
        message = 'Receita ID {} Não Encontrada'.format(indice)
        return jsonify({
            "message": message,
            "status": "Error!"
        })
    except:
        message = 'Aconteceu um erro inesperado'
        return jsonify({
            "message": message,
            "status": "Error!"
        })

    if request.method == 'GET':
        return Receitas[indice]

    elif request.method == 'PUT':

        newValue = json.loads(request.data)

        Receitas[indice] = newValue
        return jsonify({
            "message": "Updated!",
            "newValue": newValue
        })
    elif request.method == 'DELETE':
        print(indice)
        Receitas.pop(indice)
        return jsonify({
            "message": "Deleted!",
            "arrayAtual": Receitas
        })


if __name__ == '__main__':
    app.run(debug=True)