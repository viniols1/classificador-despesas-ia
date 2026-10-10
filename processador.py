import pandas as pd
import time
from google import genai

CHAVE_API = "COLE_SUA_CHAVE_AQUI"
cliente = genai.Client(api_key=CHAVE_API)


def categorizar_despesa(descricao):
    try:
        comando = f"Classifique a seguinte despesa financeira em apenas uma palavra (ex: Alimentação, Transporte, Saúde, Lazer, Educação, Moradia, Outros): {descricao}"

        resposta = cliente.models.generate_content(
            model='gemini-3.8-flash',
            contents=comando
        )

        time.sleep(2)

        return resposta.text.strip()

    except Exception as erro:
        print(
            f"\n[AVISO] Erro ao analisar '{descricao}'. O motivo foi: {erro}")
        return "Erro ao analisar"


print("Lendo o arquivo de extrato...")
tabela = pd.read_csv("extrato.csv")

print("A Inteligência Artificial está analisando as despesas...")
print("Isso pode levar alguns segundos. Aguarde...")
tabela['categoria'] = tabela['descricao'].apply(categorizar_despesa)

print("\n--- Extrato Categorizado pela IA ---")
print(tabela)
print("------------------------------------\n")
