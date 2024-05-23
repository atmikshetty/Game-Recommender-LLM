from google_play_scraper import app

result = app(
    'com.nianticlabs.pokemongo',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)

print(f'Name: {result["title"]}')
print(f'Package name: {result["appId"]}')
print(f'Description:  {result["description"]}')
print(f'Icon:  {result["icon"]}')