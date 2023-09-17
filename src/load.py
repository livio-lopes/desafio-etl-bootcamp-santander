from transform import users_tranformed
import requests

def update_user(user):
    response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False


for user in users_tranformed:
    success = update_user(user)
    print(f"{user['name']} is updated? {success}")
