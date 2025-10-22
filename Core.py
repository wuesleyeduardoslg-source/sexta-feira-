import random
import os

# ---------- Calculadora ----------
def calcular(expressao):
    try:
        resultado = eval(expressao, {"__builtins__": None}, {})
        return resultado
    except Exception as e:
        return f"Erro: {e}"

# ---------- D20 ----------
def rolar_d20():
    return random.randint(1, 20)

# ---------- Música (exemplo simples) ----------
def tocar_musica():
    print("🎵 Música tocando (simulação)")
      
