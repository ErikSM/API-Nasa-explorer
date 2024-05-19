import json
import requests

api_key = "NgtvBLp13upL4FK2z6qyWSRJNcJ3U1w4fJcokZmi"
demo_key = "DEMO_KEY"

address = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08"
earth_ad = "https://api.nasa.gov/planetary/earth/assets?lon=-95.33&lat=29.78&date=2018-01-01&&dim=0.10"

neo_browse= "https://api.nasa.gov/neo/rest/v1/neo/browse"


def testing_request(address_captured, key):
    key_used = '?api_key={}'.format(key)

    request = requests.get(f"{address_captured}{key_used}", )
    required = json.loads(request.text)

    return required


requided = testing_request(neo_browse, demo_key)

for i in requided:
    print(i)
    print(type(requided[i]))
    print(requided[i])
    print(len(requided[i]))
    print('\n')

    if i == 'near_earth_objects':
        dict_keys = set()
        print('\n\n\n')
        for j in requided[i]:
            for z in j:
                dict_keys.add(z)

for i in dict_keys:
    print(i)

