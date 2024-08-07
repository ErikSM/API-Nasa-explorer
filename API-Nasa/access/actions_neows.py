from tkinter import Text, END
from access.api_request import make_request

api_key = "NgtvBLp13upL4FK2z6qyWSRJNcJ3U1w4fJcokZmi"
demo_key = "DEMO_KEY"

source_address = "https://api.nasa.gov/neo/rest/v1/neo/browse"


def _neows_list_update(new_list=None, origin_file='', name_full=''):
    text_field = Text()

    if new_list is None:
        try:
            file = open(r'..\api_data\neows_data.py', 'w+')
        except FileNotFoundError:
            file = open(r'api_data\neows_data.py', 'w+')

        class_import_string = f"from objects.NeoWs import NeoWs\n"
        text_field.insert(1.0, class_import_string)

        principal_list_string = "\n\nneows_names = dict()\n\n"
        text_field.insert(END, principal_list_string)

        file.write(text_field.get(1.0, END))
        file.close()

    elif type(new_list) is str:
        try:
            old_file = open(r'..\api_data\neows_data.py', 'r+')
        except FileNotFoundError:
            old_file = open(r'api_data\neows_data.py', 'r+')

        text_field.insert(1.0, old_file.read())
        old_file.close()

        try:
            new_file = open(r'..\api_data\neows_data.py', 'w+')
        except FileNotFoundError:
            new_file = open(r'api_data\neows_data.py', 'w+')

        new_list_string = f"neows_names['{name_full}'] = NeoWs({new_list})"
        text_field.insert(END, new_list_string)

        new_import_string = f"from api_data.all_neows.{origin_file} import {new_list}\n"
        text_field.insert(1.0, new_import_string)

        new_file.write(text_field.get(1.0, END))
        new_file.close()


def update_and_save_neows_data():
    print('start update')
    text_field = Text()

    _neows_list_update()

    required = make_request(source_address, api_key)

    try:
        neo_ws = required["near_earth_objects"]

    except Exception as ex:
        print(f'error[update_and_save_data]: {ex}')

    else:
        for i in neo_ws:

            file_name = i['name_limited']
            neo_full_name = i['name']
            files_list_name = f'{i["name_limited"].lower()}_all_data'

            format_type = 'py'
            try:
                local_address = r'..\api_data\all_neows'

                completed_address = r'{}\{}.{}'.format(local_address, file_name, format_type)
                file = open(completed_address, 'w+')
                print('ok addr 1')

            except FileNotFoundError:

                local_address = r'api_data\all_neows'

                completed_address = r'{}\{}.{}'.format(local_address, file_name, format_type)
                file = open(completed_address, 'w+')
                print('ok addr 2')

            title = f'#  {file_name}\n\n\n'
            text_field.insert(1.0, title)

            create_principal_dict = f'{files_list_name} = dict()\n\n\n'
            text_field.insert(END, create_principal_dict)

            _neows_list_update(files_list_name, file_name, neo_full_name)

            for j in i:

                if j == 'estimated_diameter':

                    estimated_diameter_dict_open = f'{j} = ' + '{\n'
                    text_field.insert(END, estimated_diameter_dict_open)

                    processed = _processing_estimates_data(i[j])
                    text_field.insert(END, processed.get(1.0, END))

                    estimated_diameter_dict_close = '}\n\n'
                    text_field.insert(END, estimated_diameter_dict_close)

                elif j == 'close_approach_data':

                    close_approach_data_dict_open = f'{j} = ' + '{\n'
                    text_field.insert(END, close_approach_data_dict_open)

                    processed = _processing_approach_data(i[j])
                    text_field.insert(END, processed.get(1.0, END))

                    close_approach_data_dict_close = "}\n\n"
                    text_field.insert(END, close_approach_data_dict_close)

                elif j == 'orbital_data':

                    orbital_data_dict_open = f'{j} = ' + '{\n'
                    text_field.insert(END, orbital_data_dict_open)

                    processed = _processing_orbital_data(i[j])
                    text_field.insert(END, processed.get(1.0, END))

                    orbital_data_dict_close = "}\n\n"
                    text_field.insert(END, orbital_data_dict_close)

                else:

                    processed = _processing_simple_data(j, i[j])
                    text_field.insert(END, processed)

            for j in i:
                organized = _organizing_all_data_in_list(j, i)
                text_field.insert(END, organized)

            file.write(text_field.get(1.0, END))

            file.close()
            text_field.delete(1.0, END)

        print('finish update')


def _processing_estimates_data(all_data: dict):
    text_field = Text()

    for i in all_data:
        key, data = i, all_data[i]

        if type(data) is str:
            data = f'"{data}"'
        else:
            data = data

        key_and_data = f'    "{key}": {data}, \n'
        text_field.insert(1.0, key_and_data)

    return text_field


def _processing_approach_data(all_data: dict):
    text_field = Text()
    data_in_dict = ["relative_velocity", "miss_distance"]

    for i in all_data:
        internal_dict_name = i["close_approach_date_full"]
        internal_dict_open = f'   "{internal_dict_name}": ' + '{\n'

        text_field.insert(END, internal_dict_open)

        for j in i:

            if j in data_in_dict:
                data_dict_open = f'       "{j}": ' + '{\n'
                text_field.insert(END, data_dict_open)

                for z in i[j]:
                    key, data = z, i[j][z]

                    if type(data) is str:
                        data = f'"{data}"'
                    else:
                        data = data

                    key_and_data = f'           "{key}": {data}, \n'
                    text_field.insert(END, key_and_data)

                data_dict_close = "       " + "}, \n"
                text_field.insert(END, data_dict_close)

            else:
                key, data = j, i[j]

                if type(data) is str:
                    data = f'"{data}"'
                else:
                    data = data

                key_and_data = f'       "{key}": {data}, \n'
                text_field.insert(END, key_and_data)

        internal_dict_close = "   " + "}, \n"
        text_field.insert(END, internal_dict_close)

    return text_field


def _processing_orbital_data(all_data: dict):
    text_field = Text()
    data_in_dict = ["orbit_class"]

    for i in all_data:

        if i in data_in_dict:
            data_dict_open = f'    "{i}": ' + '{\n'
            text_field.insert(END, data_dict_open)

            for j in all_data[i]:
                key, data = j, all_data[i][j]

                if key == "orbit_class_description":
                    msg = data.encode("utf-8")

                    if len(msg) > 70:
                        key_and_data = (f'        "description": {msg[:69]}\n'
                                        f'                       {msg[69:]}, \n')
                    else:
                        key_and_data = f'        "description": {msg}, \n'

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
            key, data = i, all_data[i]

            if type(data) is str:
                data = f'"{data}"'
            else:
                data = data

            key_and_data = f'    "{key}": {data}, \n'
            text_field.insert(END, key_and_data)

    return text_field


def _processing_simple_data(var, data):
    if var == 'id':
        var_name = f'{var}_code'
    else:
        var_name = var

    if type(data) is str:
        data = f'"{data}"'
    else:
        data = data

    var_and_data = f'{var_name} = {data}\n\n'

    return var_and_data


def _organizing_all_data_in_list(var, data):
    dict_name = data["name_limited"]

    if var == 'id':
        var_name = f'{var}_code'
    else:
        var_name = var

    add_in_list = f'{dict_name.lower()}_all_data["{var_name}"] = {var_name}\n'

    return add_in_list
