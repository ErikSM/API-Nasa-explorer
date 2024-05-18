import json
import requests


api_key = "NgtvBLp13upL4FK2z6qyWSRJNcJ3U1w4fJcokZmi"
demo_key = "DEMO_KEY"


address = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key="


def testing_request(address_captured, key):
    request = requests.get(f"{address_captured}{key}")
    required = json.loads(request.text)

    return required


requided = testing_request(address, demo_key)


for i in requided:
    print(i)
    print(type(requided[i]))
    print(requided[i])
    print('\n')


print('\n\n\n**', type(requided), len(requided))

