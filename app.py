import requests
from flask import Flask, request, Response

app = Flask(__name__)

SERVER_ORIGINAL = "https://alpha-mfc.muneris.io/v10"

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    url_original = f"{SERVER_ORIGINAL}/{path}"
    if request.query_string:
        url_original += f"?{request.query_string.decode('utf-8')}"
        
    print(f"\n[ESPIÃO] O jogo pediu o caminho: /{path}")
    print(f"[ESPIÃO] Tentando buscar no servidor original: {url_original}")

    try:
        headers = {key: value for key, value in request.headers if key.lower() != 'host'}
        res = requests.request(
            method=request.method,
            url=url_original,
            headers=headers,
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False,
            timeout=10
        )
        
        print(f"[ESPIÃO] Resposta do servidor original: Status {res.status_code}")
        
        excluir_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        resposta_headers = [(k, v) for k, v in res.raw.headers.items() if k.lower() not in excluir_headers]
        
        return Response(res.content, res.status_code, resposta_headers)
        
    except Exception as e:
        print(f"[ESPIÃO] Erro ao conectar ao servidor antigo: {e}")
        return {"status": "error", "message": "Link quebrado ou offline"}, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
    
