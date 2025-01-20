import requests
import time
from src.utils.file_operations import save_data
from src.extraction.save_historical import save_historical
from src.extraction.clean_old_files import clean_old_files
from src.config.settings import URL, BRONZE_PATH, INTERVAL

def continuous_extraction():
    while True:
        try:
            response = requests.get(URL)
            if response.status_code == 200:
                data = response.json()
                save_data(data, BRONZE_PATH)

                # Salvar dados históricos se for segunda-feira às 10h
                save_historical(data)
                # Limpar arquivos temporários antigos
                clean_old_files()
            else:
                print(f"Erro ao fazer a requisição: {response.status_code}")
        except Exception as e:
            print(f"Erro durante a extração: {e}")
        # Espera pelo próximo ciclo
        time.sleep(INTERVAL)
