import json
import requests

from tkinter import Text, END

api_key = "NgtvBLp13upL4FK2z6qyWSRJNcJ3U1w4fJcokZmi"
demo_key = "DEMO_KEY"

address = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08"
earth_ad = "https://api.nasa.gov/planetary/earth/assets?lon=-95.33&lat=29.78&date=2018-01-01&&dim=0.10"

neo_browse = "https://api.nasa.gov/neo/rest/v1/neo/browse"


def make_request(address_captured, key):
    key_used = '?api_key={}'.format(key)

    request = requests.get(f"{address_captured}{key_used}", )
    required_dict = json.loads(request.text)

    return required_dict


def opening_neows():
    required = make_request(neo_browse, demo_key)
    neo_dict_keys = None

    for i in required:
        '''print(i)
        print(type(required[i]))
        print(required[i])
        print(len(required[i]))
        print('\n')
'''
        if i == 'near_earth_objects':
            neo_dict_keys = set()
            print('\n\n\n')
            for j in required[i]:
                print(j['name_limited'])
                for z in j:
                    neo_dict_keys.add(z)

    for i in neo_dict_keys:
        pass
        #print(i)


def save_neows_data():

    temporary = Text()

    required = make_request(neo_browse, demo_key)
    neo_ws = required["near_earth_objects"]

    local_address = r'api_data\all_neows'
    format_type = 'txt'

    for i in neo_ws:
        file_name = i['name_limited']

        completed_address = r'{}\{}.{}'.format(local_address, file_name, format_type)
        #  file = open(completed_address, 'w+')

        print(f'-----{file_name}\n\n')

        for j in i:

            if j == 'estimated_diameter':
                print(f'[{j}] = ' + '{')
                temporary_dict = i[j]
                for z in temporary_dict:
                    print(f'    {z}: {temporary_dict[z]}, ')
                print("}\n")

            elif j == 'close_approach_data':

                print(f'[{j}] = [')

                temporary_list = i[j]
                for z in temporary_list:

                    print(f'\n({z["close_approach_date"]}) = ' + '{')

                    for y in z:

                        print(f'    {y}: {z[y]}, ')

                    print(" "*10 + "}\n")
                print("]\n")

            elif j == 'orbital_data':
                print(f'[{j}] = ' + '{')
                temporary_dict = i[j]
                for z in temporary_dict:
                    print(f'    {z}: {temporary_dict[z]}, ')
                print("}\n")

            else:
                print(f'{j}: {i[j]}')
                print('\n')

            temporary.insert(1.0, f'{i["name"]}')
        #  file.write(temporary.get(1.0, END))

        #  file.close()
        temporary.delete(1.0, END)


def teste(endereco, formato):

    arquivo = open(f"{endereco}.{formato}", "r")
    arquivo_lido = arquivo.read()


save_neows_data()

