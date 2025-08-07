import logging

# Configuração básica do logger
logging.basicConfig(
    level=logging.INFO,  # Define o nível mínimo a ser registrado
    format='%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app.log"),  # salva no arquivo
        logging.StreamHandler()          # também exibe no console
    ]
)

def obter_salario():
    try:
        valor = float(input("Digite o salário: "))
        logging.info("Salário inserido com sucesso.")
        return valor
    except ValueError as e:
        logging.info("Erro ao tentar converter o salário: %s", e)  
        return None
    except Exception as e:
        logging.exception("Erro inesperado ao obter salário.")  # inclui traceback
        return None

# Uso da função
salario = obter_salario()
if salario is not None:
    print("Salário:", salario)
else:
    print("Não foi possível obter o salário.")
