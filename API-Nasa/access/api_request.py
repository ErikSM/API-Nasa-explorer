import json
import requests

api_key = "NgtvBLp13upL4FK2z6qyWSRJNcJ3U1w4fJcokZmi"
demo_key = "DEMO_KEY"


neo_adr = "https://api.nasa.gov/neo/rest/v1/neo/browse"
donki_adr = "https://api.nasa.gov/DONKI/"


def make_request(address_captured, key, complement=None):
    key_used = _preparing_api_key(address_captured, key)

    if complement is None:
        address = address_captured
    else:
        address = address_captured + complement

    try:
        request = requests.get(f"{address}{key_used}")
        data_required = json.loads(request.text)

    except Exception as ex:

        if key_used[0] == '?':
            data_required = {'Error[make_request]': ex}
        elif key_used[0] == '&':
            data_required = [{'Error[make_request]': ex}]
        else:
            data_required = f'Error[make_request]: {ex}'

        print(data_required)

    return data_required


def _preparing_api_key(address, key):
    brw = ''

    if address == neo_adr:
        brw = '?'
    elif address == donki_adr:
        brw = '&'

    key_to_use = '{}api_key={}'.format(brw, key)

    return key_to_use
