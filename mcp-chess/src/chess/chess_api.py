import requests

CHESS_API_BASE = "https://api.chess.com/pub"

def get_player_profile(username: str):
    url = f"{CHESS_API_BASE}/player/{username}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

headers = {"accept": "application/json",
           "User Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Python/3.10 requests/2.31.0 "}

def get_player_stats(username: str):
    url = f"{CHESS_API_BASE}/player/{username}/stats"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()