from flask import Flask, request, jsonify
from core.modulos import calcular, rolar_d20, tocar_musica
from core.internet import scrape_page, search_web_googlelike, download_file, fetch_json_api
from core.memoria import salvar_historico, carregar_historico
from voz.reconhecimento import ouvir_comando
from voz.sintetizador import falar

app = Flask(__name__)

# ---------- Módulos W.E.T.S ----------
@app.route("/modulo", methods=["GET"])
def modulo():
    cmd = request.args.get("cmd", "")
    if cmd == "calculadora":
        return jsonify({"resposta": "Digite expressão na interface ou por voz."})
    elif cmd == "musica":
        tocar_musica()
        return jsonify({"resposta": "Tocando música..."})
    elif cmd == "D20":
        resultado = rolar_d20()
        return jsonify({"resposta": f"D20: {resultado}"})
    else:
        return jsonify({"resposta": f"Módulo {cmd} não encontrado."})

# ---------- Comando de voz ----------
@app.route("/voz", methods=["GET"])
def comando_voz():
    cmd = ouvir_comando()
    falar(f"Você disse: {cmd}")
    return jsonify({"resposta": cmd})

# ---------- Internet ----------
@app.route("/web/scrape", methods=["GET"])
def web_scrape():
    url = request.args.get("url")
    if not url:
        return jsonify({"erro": "Informe o parâmetro url"})
    info = scrape_page(url)
    return jsonify(info)

@app.route("/web/search", methods=["GET"])
def web_search():
    query = request.args.get("q")
    if not query:
        return jsonify({"erro": "Informe o parâmetro q"})
    results = search_web_googlelike(query)
    return jsonify(results)

@app.route("/web/download", methods=["GET"])
def web_download():
    url = request.args.get("url")
    if not url:
        return jsonify({"erro": "Informe o parâmetro url"})
    path = download_file(url)
    return jsonify({"download_path": path})

@app.route("/web/fetch_json", methods=["GET"])
def web_fetch_json():
    url = request.args.get("url")
    if not url:
        return jsonify({"erro": "Informe o parâmetro url"})
    data = fetch_json_api(url)
    return jsonify(data)

# ---------- Memória ----------
@app.route("/memoria", methods=["GET","POST"])
def memoria():
    if request.method == "POST":
        cmd = request.json.get("cmd","")
        salvar_historico(cmd)
        return jsonify({"status":"salvo"})
    else:
        historico = carregar_historico()
        return jsonify(historico)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
  
