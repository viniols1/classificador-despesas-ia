# 📊 Classificador Inteligente de Despesas

Este projeto é um script em Python desenvolvido para automatizar a leitura e a categorização de extratos bancários utilizando Inteligência Artificial. 

## 🚀 O que foi feito
* **Processamento de Dados:** Utilização da biblioteca `pandas` para ler e organizar dados de um arquivo CSV (`extrato.csv`) que simula transações bancárias.
* **Integração com IA:** Comunicação com o modelo `gemini-3.8-flash` via API do Google Gemini para interpretar a descrição de cada compra (ex: "UBER *TRIP", "NETFLIX") e classificá-la automaticamente (ex: Transporte, Lazer, Saúde).
* **Automação Resiliente:** Implementação de pausas estruturadas e blocos de tratamento de exceções (`try/except`) para garantir que o script continue rodando mesmo diante de instabilidades de rede.

## 🛠️ Como rodar o projeto
1. Instale as bibliotecas necessárias: `pip install -r requirements.txt`
2. Gere uma chave de API gratuita no Google AI Studio.
3. Substitua o texto `"COLE_A_SUA_CHAVE_AQUI"` no arquivo `processador.py` pela sua chave real.
4. Execute o script no terminal: `python processador.py`

## ⚠️ Nota sobre Erros de Servidor (503 Unavailable)
Este projeto utiliza a camada gratuita (Free Tier) da API do Google Gemini. Como os servidores do Google impõem limites de requisições por minuto e sofrem picos de acesso, é comum que o terminal exiba mensagens de erro como **`503 UNAVAILABLE: This model is currently experiencing high demand`**.

Isso **não** indica uma falha na lógica do código. O script foi projetado com resiliência: o bloco `try/except` captura a recusa do servidor, avisa o usuário no terminal e marca a despesa como "Erro ao analisar", permitindo que o programa continue processando as próximas linhas do extrato sem "quebrar" ou interromper a execução. Caso esse erro ocorra, basta aguardar alguns minutos para o servidor normalizar e rodar o script novamente.