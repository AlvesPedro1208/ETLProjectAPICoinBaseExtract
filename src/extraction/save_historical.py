import os
import json
from datetime import datetime
from src.config.settings import HISTORICAL_PATH

def save_historical(data):
    now = datetime.utcnow()
    if now.weekday() == 0 and now.hour == 10 and now.minute == 0:  # Segunda-feira às 10h
        os.makedirs(HISTORICAL_PATH, exist_ok=True)
        file_name = now.strftime('currencies_historical_%Y%m%d.json')
        file_path = os.path.join(HISTORICAL_PATH, file_name)
        
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Dados históricos salvos em {file_path}")
