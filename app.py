from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    # Isso vai nos mostrar no painel do Render tudo o que o jogo tentar acessar
    print(f"-> REQUISIÇÃO RECEBIDA: /{path} [{request.method}]")
    return jsonify({"status": "ok", "message": "Servidor ativo!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
  
