import json
import requests

api_key = "NgtvBLp13upL4FK2z6qyWSRJNcJ3U1w4fJcokZmi"
demo_key = "DEMO_KEY"


neo_adr = "https://api.nasa.gov/neo/rest/v1/neo/browse"
donki_adr = "https://api.nasa.gov/DONKI/"


def make_request(address_captured, key):
    key_used = _preparing_api_key(address_captured, key)

    request = requests.get(f"{address_captured}{key_used}", )
    required_dict = json.loads(request.text)

    return required_dict


def _preparing_api_key(address, key):
    brw = ''

    if address == neo_adr:
        brw = '?'
    elif address == donki_adr:
        brw = '&'

    key_to_use = '{}api_key={}'.format(brw, key)

    return key_to_use
