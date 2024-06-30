class NeoWs:

    def __init__(self, all_info: dict):

        self.__all_info = all_info

        try:
            self.__name = self.__all_info['name']
            self.__name_limited = self.__all_info['name_limited']
            self.__id_code = self.__all_info['id_code']
        except Exception as ex:
            self.__name = f'Error:{ex}'

    def __str__(self):
        return self.__name

    def basic_data(self):
        basic_data_keys = ['name_limited', 'neo_reference_id', 'designation']

        basic_data = dict()
        for i in basic_data_keys:
            basic_data[i] = self.__all_info[i]

        return basic_data

    def links_data(self):

        links_data = dict()
        links_data['self_url'] = self.__all_info['links']['self']
        links_data['nasa_jpl_url'] = self.__all_info['nasa_jpl_url']

    def technical_data(self):
        technical_data_keys = ['is_sentry_object', 'is_potentially_hazardous_asteroid', 'absolute_magnitude_h']

        technical_data = dict()
        for i in technical_data_keys:
            technical_data[i] = self.__all_info[i]

        return technical_data

    def advanced_data(self, specific=None):
        adv_data_keys = ['estimated_diameter', 'close_approach_data', 'orbital_data']

        advanced_data = dict()
        for i in adv_data_keys:
            advanced_data[i] = self.__all_info[i]

        if specific is None:
            return advanced_data
        else:
            specified_advanced_data = advanced_data.get(specific)
            return specified_advanced_data

    @property
    def name(self):
        return self.__name_limited

    @property
    def id_code(self):
        return self.__id_code
