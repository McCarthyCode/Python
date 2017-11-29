import requests

query = raw_input("Search by album name: ")

url = "https://api.spotify.com/v1/search?q=" + query.replace(" ", "+") + "&type=album"
token = "Bearer BQCVuLvEpKm-uW6wzxNil_DMLaOXkqYRAwY3Esu0Y3KDwE8r3TK9jR6tFsZ_0uwOQTKnkUB62lHC4co9Gl0"
token += "netr13HDzeHYMTwIAdPsUX0TQE6SugMhlwL6SPS8Q_sXaP4TceTmcVlhpuQ"

r = requests.get(url, headers={"Accept": "application/json", "Authorization": token})

first = r.json()['albums']['items'][0]
second = r.json()['albums']['items'][1]
third = r.json()['albums']['items'][2]

print "Showing top three album results for query '" + query + "'"

print "First result:"
print "  Album name:", first['name']
print "  Artist name:", first['artists'][0]['name']

print "Second result:"
print "  Album name:", second['name']
print "  Artist name:", second['artists'][0]['name']

print "Third result:"
print "  Album name:", third['name']
print "  Artist name:", third['artists'][0]['name']
