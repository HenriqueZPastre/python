import requests
import time
from utils.readjson import readJson
import os

url = 'https://www.sefaz.rs.gov.br/ASP/AAE_ROOT/NFE/SAT-WEB-NFE-NFC_2.asp'
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "iframe",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1"
}

chavesNfe = readJson('chaves.json')
print(len(chavesNfe))

def bodyData(chave):
	data = {
		"HML": "false",
		"chaveNFe": chave,
		"Action": "Avançar"
	}
	return data


def consultarChaves(chaves):
    os.makedirs("./chaves", exist_ok=True)
    for chave in chaves:
        dadosRequest= bodyData(chave)
        try:
            r = requests.post(url, headers=headers, data=dadosRequest)
            r.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            salvarPagina(chave, r.text)
            time.sleep(2)  # Optional: sleep to avoid overwhelming the server
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while consulting {chave}: {e}")

def salvarPagina(chave, response_text):
	with open(f"./chaves/{chave}.html", "w", encoding="utf-8") as file:
		file.write(response_text)
	print(f"Response for {chave} saved to ./chaves/{chave}.html")

consultarChaves(chavesNfe)