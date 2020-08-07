import requests
import json
import urllib
import urllib2

# make query
query = urllib.urlencode(dict(q="blue angel", rpp=5, include_entities=1,
                              result_type="mixed"))  
# make request
resp = urllib2.urlopen("http://search.twitter.com/search.json?" + query)

# make dictionary (parse json response)
d = json.load(resp)

requests.post('http://localhost:51015/game_event',"""{
    "device-type": "screened",
    "mode": "screen",
    "zone": "one",
    "datas": [
        {
          "lines": [
            {
              "has-text": true,
              "context-frame-key": "first-line",
              "wrap": 1
            },
            {
              "has-text": true,
              "context-frame-key": "second-line"
            }
          ]
        }
      ]
}""")