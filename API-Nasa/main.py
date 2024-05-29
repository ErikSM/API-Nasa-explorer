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
        # print(i)


def save_neows_data():
    text_field = Text()

    required = make_request(neo_browse, demo_key)
    neo_ws = required["near_earth_objects"]

    local_address = r'api_data\all_neows'
    format_type = 'py'

    for i in neo_ws:
        file_name = i['name_limited']

        completed_address = r'{}\{}.{}'.format(local_address, file_name, format_type)
        file = open(completed_address, 'w+')

        title = f'#  {file_name}\n\n\n'
        text_field.insert(1.0, title)

        for j in i:

            if j == 'estimated_diameter':

                internal_dict_open = f'{j} = ' + '{\n'
                text_field.insert(END, internal_dict_open)

                for z in i[j]:

                    key_and_data = f'    "{z}": {i[j][z]}, \n'
                    text_field.insert(END, key_and_data)

                internal_dict_close = '}\n\n'
                text_field.insert(END, internal_dict_close)

            elif j == 'close_approach_data':

                dict_open = f'{j} = ' + '{\n'
                text_field.insert(END, dict_open)

                for z in i[j]:

                    internal_dict_open = f'\n"  {z["close_approach_date_full"]}": ' + '{\n'
                    text_field.insert(END, internal_dict_open)

                    for y in z:
                        key_and_data = f'       "{y}": "{z[y]}", \n'
                        text_field.insert(END, key_and_data)

                    internal_dict_close = " " * 10 + "}, \n"
                    text_field.insert(END, internal_dict_close)

                dict_close = "}\n\n"
                text_field.insert(END, dict_close)

            elif j == 'orbital_data':

                internal_dict_open = f'{j} = ' + '{\n'
                text_field.insert(END, internal_dict_open)

                for z in i[j]:

                    key_and_data = f'    "{z}": "{i[j][z]}", \n'
                    text_field.insert(END, key_and_data)

                internal_dict_close = "}\n\n"
                text_field.insert(END, internal_dict_close)

            else:

                var_and_data = f'{j} = "{i[j]}"\n\n'
                text_field.insert(END, var_and_data)

        file.write(text_field.get(1.0, END))

        #  file.close()
        text_field.delete(1.0, END)


def teste(endereco, formato):
    arquivo = open(f"{endereco}.{formato}", "r")
    arquivo_lido = arquivo.read()


save_neows_data()
