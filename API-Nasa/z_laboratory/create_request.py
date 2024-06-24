import json
import requests

from access.actions_donki import donki_dict, source_address

api_key = "NgtvBLp13upL4FK2z6qyWSRJNcJ3U1w4fJcokZmi"
demo_key = "DEMO_KEY"

start_date = "2015-09-07"
end_date = "2015-10-08"

neo_browse = f"https://api.nasa.gov/neo/rest/v1/neo/browse"
neo_feed = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}"


def _create_request(address_captured, key):
    key_used = '&api_key={}'.format(key)

    request = requests.get(f"{address_captured}{key_used}", )
    required_dict = json.loads(request.text)

    print(f'\n??[[source_address_:  {address_captured}{key_used}]]??\n\n')

    return required_dict


def opening_neows():
    required = _create_request(neo_browse, api_key)
    neo_dict_keys = None

    for i in required:
        """print(i)
        print(type(required[i]))
        print(required[i])
        print(len(required[i]))
        print('\n')"""

        if i == 'near_earth_objects':
            neo_dict_keys = set()
            print('\n\n\n')
            for j in required[i]:
                print(j['name_limited'])
                for z in j:
                    neo_dict_keys.add(z)

    for i in neo_dict_keys:
        print(i)


def exploring_donki_s(donki_selected):
    #  [[donki_keys]]
    #  "Coronal Mass Ejection (CME)", "Coronal Mass Ejection (CME) Analysis", "Geomagnetic Storm (GST)",
    #  "Interplanetary Shock (IPS)","Solar Flare (FLR)","Solar Energetic Particle (SEP)",
    #  "Magnetopause Crossing (MPC)","Radiation Belt Enhancement (RBE)", "Hight Speed Stream (HSS)",
    #  "WSA+EnlilSimulation","Notifications"

    act_donki = donki_dict[donki_selected]

    donki_source_address = source_address
    donki_tuple = act_donki(start_date, end_date)

    address = donki_source_address + donki_tuple[0]
    about_parameters = donki_tuple[1]

    print(f'DONKI: {donki_selected}\n')

    for i in about_parameters:
        print(i)
    print("-"*30)

    requested = _create_request(address, api_key)
    print(f"(({len(requested)} {type(requested)}))\n")

    for i in requested:
        print(f'**{len(i)}{type(i)}')


exploring_donki_s("Coronal Mass Ejection (CME) Analysis")


