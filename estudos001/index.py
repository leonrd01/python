import requests
import json
from deep_translator import GoogleTranslator

def traduzirCita(texto):
    try:
       #usando API para traduzir o texto e alocando em uma var
       traduzido = GoogleTranslator(source='auto', target='pt').translate(texto)
       return traduzido
    except Exception as e:
        print(f"Erro ao traduzir a citação: {e}")
        return texto  # Retorna o texto original caso haja um erro na tradução
    
def get50():
    # alocando a url da API 
    url = "https://zenquotes.io/api/quotes"
    
    # fazendo a requisição para a API
    response = requests.get(url)
    
    # verifica se deu tudo certo
    if response.status_code == 200:

        # convertendo a requisição em JSON
        data = response.json()
        print("----------------------------------------------------------------------------------")

        # alocando as citações('q') e os autores('a') em variavéis e printando na tela
        for i in data:
            texto = i['q']
            autor = i['a']
            textoTraduzido = traduzirCita(texto)
            print(f"Autor: {autor} \nCitação: {texto} \nCitação Traduzida para Portugês: {textoTraduzido}")
            print("----------------------------------------------------------------------------------")
    else:
        print("Erro ao acessar a API: ", response.status_code)

get50()

