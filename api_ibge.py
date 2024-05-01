import pandas as pd
import requests

url_municipios = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"

# Fazendo a requisição GET para obter todos os municípios
response = requests.get(url_municipios)

# Verificando se a requisição foi bem-sucedida (código 200)
if response.status_code == 200:
    municipios = response.json()  # Convertendo a resposta para formato JSON

    reorganizados = []
    for municipio in municipios:
        dados = {
            'Code': municipio['id'],
            'Names': municipio['nome'],
            'Mesorregiao': municipio['microrregiao']['mesorregiao']['nome'],
            'InterRegiao': municipio['regiao-imediata']['regiao-intermediaria']['nome'],
            'State': municipio['microrregiao']['mesorregiao']['UF']['nome'],
            'UF': municipio['microrregiao']['mesorregiao']['UF']['sigla'],
            'Region': municipio['microrregiao']['mesorregiao']['UF']['regiao']['nome'],
            'RegionAbbreviation': municipio['microrregiao']['mesorregiao']['UF']['regiao']['sigla']
        }
        reorganizados.append(dados)

    # Criando um DataFrame a partir dos dados reorganizados
    df = pd.DataFrame(reorganizados)
    print(df)  # Exibindo o DataFrame dos municípios
else:
    print(f"Erro ao obter os dados. Código de status: {response.status_code}")