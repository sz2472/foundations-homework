import requests

#response = requests.get('http://www.nytimes.com')

response = requests.get('https://api.spotify.com/v1/search?query=80s&type=playlist')
#get the response, use .json()to convert the string (which looks like a dictionary but is actually a string and that's called json)
#into a real dictionary
data = response.json()
print(data.keys())
print(type(data['playlists']))
print(data['playlists'].keys())

playlists = data['playlists']['items']
print(type(playlists))

for playlist in playlists:
    print(playlist['name'], playlist['href'])
