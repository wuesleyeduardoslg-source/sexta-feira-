import json
import os

MEMORIA_PATH = "banco/memoria.json"

def salvar_historico(cmd):
    historico = carregar_historico()
    historico.append(cmd)
    os.makedirs(os.path.dirname(MEMORIA_PATH), exist_ok=True)
    with open(MEMORIA_PATH, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)

def carregar_historico():
    if not os.path.exists(MEMORIA_PATH):
        return []
    with open(MEMORIA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
  
