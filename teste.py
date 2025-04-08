import requests
import gspread
from functools import lru_cache

# Função para autenticação no Google Sheets (cache para evitar múltiplas autenticações)
@lru_cache(maxsize=1)
def get_gspread_client():
    credentials = {
        "type": "",
        "project_id": "",
        "private_key_id": "",
        "private_key": "",
        "client_email": "",
        "client_id": "",
        "auth_uri": "",
        "token_uri": "",
        "auth_provider_x509_cert_url": "",
        "client_x509_cert_url": "",
        "universe_domain": ""
    }
    return gspread.service_account_from_dict(credentials)

# Requisição para API
url = "https://randomuser.me/api/"
response = requests.get(url, headers={"Accept": "application/json"})

if response.status_code == 200:
    user = response.json()["results"][0]

    # Mapeamento direto para extrair os dados
    extracted_data = list(map(lambda key: (
        f"{user['name']['first']} {user['name']['last']}" if key == "name" else
        user["location"].get(key, "") if key in ["city", "state", "country"] else
        user.get(key, "").capitalize() if key == "gender" else
        user.get(key, "")
    ), ['gender', 'name', 'city', 'state', 'country', 'email', 'phone', 'cell']))

    # Conexão com o Google Sheets e inserção de dados
    sheet = get_gspread_client().open("Folha de leads").sheet1
    sheet.append_row(extracted_data)

    print("Dados inseridos com sucesso!")

else:
    print("Erro na requisição:", response.status_code)