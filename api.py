# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)


import requests
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'
r = requests.get(url)
json_data = r.json()
for k in json_data.keys():
    print(k + ': ', json_data[k])
