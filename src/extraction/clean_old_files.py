import os
from datetime import datetime
from src.config.settings import BRONZE_PATH, RETAIN_TIME

def clean_old_files():
    now = datetime.utcnow()

    for file_name in os.listdir(BRONZE_PATH):
        if file_name.startswith('currencies_') and file_name.endswith('.json'):
            timestamp_str = file_name.replace('currencies_', '').replace('.json', '')
            file_time = datetime.strptime(timestamp_str, '%Y%m%d%H%M%S')

            if now - file_time > RETAIN_TIME:
                file_path = os.path.join(BRONZE_PATH, file_name)
                os.remove(file_path)
                print(f"Arquivo temporário excluído: {file_path}")
