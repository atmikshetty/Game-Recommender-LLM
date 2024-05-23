from google_play_scraper import search, Sort
import json

results = search(
    "Trending games",
    lang="en",
    country="us",
    n_hits=30  # max limit
)
# print(results)

def extract_req_info(game):
    return {
        'game_name': game.get('title', ''),
        'package_name': game.get('appId', ''),
        'description': game.get('description', ''),
        'icon_url': game.get('icon', ''),
        'genre': game.get('genre', ''),
        'rating': game.get('score', ''),
        'no_of_ratings': game.get('installs', '')
    }

extracted_info = [extract_req_info(game) for game in results]

for info in extracted_info:
    print(json.dumps(info, indent=4))

print(len(extracted_info))