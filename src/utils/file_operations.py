import os
import json
from datetime import datetime

def save_data(data, path):
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_path = os.path.join(path, f'currencies_{timestamp}.json')

    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Dados salvos em {file_path}")
