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


def update_and_save_neows_data():

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

        create_principal_dict = f'{i["name_limited"].lower()}_all_data = dict()\n\n\n'
        text_field.insert(END, create_principal_dict)

        for j in i:

            if j == 'estimated_diameter':

                internal_dict_open = f'{j} = ' + '{\n'
                text_field.insert(END, internal_dict_open)

                for z in i[j]:
                    key, data = z, i[j][z]

                    if type(data) is str:
                        data = f'"{data}"'
                    else:
                        data = data

                    key_and_data = f'    "{key}": {data}, \n'
                    text_field.insert(END, key_and_data)

                internal_dict_close = '}\n\n'
                text_field.insert(END, internal_dict_close)

            elif j == 'close_approach_data':

                dict_open = f'{j} = ' + '{\n'
                text_field.insert(END, dict_open)

                data_in_dict = ["relative_velocity", "miss_distance"]

                for z in i[j]:

                    internal_dict_name = z["close_approach_date_full"]
                    internal_dict_open = f'   "{internal_dict_name}": ' + '{\n'

                    text_field.insert(END, internal_dict_open)

                    for y in z:

                        if y in data_in_dict:

                            data_dict_key = y
                            data_dict_open = f'       "{data_dict_key}": ' + '{\n'

                            text_field.insert(END, data_dict_open)

                            for x in z[y]:

                                key, data = x, z[y][x]

                                if type(data) is str:
                                    data = f'"{data}"'
                                else:
                                    data = data

                                key_and_data = f'           "{key}": {data}, \n'
                                text_field.insert(END, key_and_data)

                            data_dict_close = "       " + "}, \n"
                            text_field.insert(END, data_dict_close)

                        else:

                            key, data = y, z[y]

                            if type(data) is str:
                                data = f'"{data}"'
                            else:
                                data = data

                            key_and_data = f'       "{key}": {data}, \n'
                            text_field.insert(END, key_and_data)

                    internal_dict_close = "   " + "}, \n"
                    text_field.insert(END, internal_dict_close)

                dict_close = "}\n\n"
                text_field.insert(END, dict_close)

            elif j == 'orbital_data':

                internal_dict_open = f'{j} = ' + '{\n'
                text_field.insert(END, internal_dict_open)

                data_in_dict = ["orbit_class"]

                for z in i[j]:

                    if z in data_in_dict:

                        data_dict_open = f'    "{z}": ' + '{\n'
                        text_field.insert(END, data_dict_open)

                        for x in i[j][z]:

                            key, data = x, i[j][z][x]

                            if key == "orbit_class_description":
                                key_and_data = f'        "description": "{data}", \n'
                                text_field.insert(END, key_and_data)
                            else:
                                if type(data) is str:
                                    data = f'"{data}"'
                                else:
                                    data = data
                                key_and_data = f'        "{key}": {data}, \n'
                                text_field.insert(END, key_and_data)

                        data_dict_close = "    }\n\n"
                        text_field.insert(END, data_dict_close)

                    else:

                        key, data = z, i[j][z]

                        if type(data) is str:
                            data = f'"{data}"'
                        else:
                            data = data

                        key_and_data = f'    "{key}": {data}, \n'
                        text_field.insert(END, key_and_data)

                internal_dict_close = "}\n\n"
                text_field.insert(END, internal_dict_close)

            else:

                if j == 'id':
                    var_name = f'{j}_code'
                else:
                    var_name = j

                if type(i[j]) is str:
                    data = f'"{i[j]}"'
                else:
                    data = i[j]

                var_and_data = f'{var_name} = {data}\n\n'
                text_field.insert(END, var_and_data)

        for j in i:

            if j == 'id':
                var_name = f'{j}_code'
            else:
                var_name = j

            dict_name = i["name_limited"]

            add_in_principal_list = f'{dict_name.lower()}_all_data["{var_name}"] = {var_name}\n'
            text_field.insert(END, add_in_principal_list)

        file.write(text_field.get(1.0, END))

        file.close()
        text_field.delete(1.0, END)


def teste(endereco, formato):
    arquivo = open(f"{endereco}.{formato}", "r")
    arquivo_lido = arquivo.read()


update_and_save_neows_data()
