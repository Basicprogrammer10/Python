from requests import get
import json

word = "sad"
url = "https://thesaurus.altervista.org/thesaurus/v1?word="+word+"&language=en_US&key=8qMqwt4RVHWeTWGwdJJw&output=json"
data = json.loads(str(get(url).json()))
print(data['synonyms'])
