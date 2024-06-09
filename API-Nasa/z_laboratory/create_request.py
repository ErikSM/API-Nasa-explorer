import json
import requests


api_key = "NgtvBLp13upL4FK2z6qyWSRJNcJ3U1w4fJcokZmi"
demo_key = "DEMO_KEY"

address = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08"
earth_ad = "https://api.nasa.gov/planetary/earth/assets?lon=-95.33&lat=29.78&date=2018-01-01&&dim=0.10"

neo_browse = "https://api.nasa.gov/neo/rest/v1/neo/browse"


def _create_request(address_captured, key):
    key_used = '?api_key={}'.format(key)

    request = requests.get(f"{address_captured}{key_used}", )
    required_dict = json.loads(request.text)

    return required_dict


def opening_neows():
    required = _create_request(neo_browse, demo_key)
    neo_dict_keys = None

    for i in required:
        '''print(i)
        print(type(required[i]))
        print(required[i])
        print(len(required[i]))
        print('\n')'''

        if i == 'near_earth_objects':
            neo_dict_keys = set()
            print('\n\n\n')
            for j in required[i]:
                print(j['name_limited'])
                for z in j:
                    neo_dict_keys.add(z)

    for i in neo_dict_keys:
        pass
        # print(i)
