import requests

BASE_URL = "https://api.github.com"

def get_user_repos(username):
    url = f"{BASE_URL}/users/{username}/repos"
    response = requests.get(url)
    return response.json()