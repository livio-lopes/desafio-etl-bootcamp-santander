import pandas as pd
import requests
import json

# Extraindo lista de userIds do CSV
df = pd.read_csv('src/data/SDW2023.csv')
users_ids = df['userId'].tolist()

# Buscando informaçoes usuarios por id na API
SDW2023_API_URL = 'https://sdw-2023-prd.up.railway.app'
def get_user(id):
  response = requests.get(f'{SDW2023_API_URL}/users/{id}')
  return response.json() if response.status_code == 200 else None

users = [json.dumps(user) for id in users_ids if (user := get_user(id)) is not None]
