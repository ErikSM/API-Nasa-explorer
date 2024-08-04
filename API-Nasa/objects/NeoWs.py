class NeoWs:

    def __init__(self, all_info: dict):

        self.__all_info = all_info

        try:
            self.__name = self.__all_info['name']
        except Exception as ex:
            self.__name = f'Error: {ex}'

    def __str__(self):
        return self.__name

    def __len__(self):
        return len(self.__all_info)

    def __getitem__(self, item):
        return self.__all_info[item]

    def basic_data(self):
        basic_data_keys = ['name_limited', 'neo_reference_id', 'designation']

        for i in basic_data_keys:
            if i in self.__all_info:
                yield f'>{i.replace("_", " ").title()}:  {self.__all_info[i]}'

    def technical_data(self):
        technical_data_keys = ['is_sentry_object', 'is_potentially_hazardous_asteroid', 'absolute_magnitude_h']

        for i in technical_data_keys:
            if i in self.__all_info:
                yield f'>{i.replace("_", " ").title()}:  {self.__all_info[i]}'

    def links_data(self):
        try:
            yield f'{self.__all_info['links']['self']}'
            yield f'{self.__all_info['nasa_jpl_url']}'
        except KeyError:
            pass

    def advanced_data(self, specific=None):
        adv_data_keys = ['estimated_diameter', 'close_approach_data', 'orbital_data']

        advanced_data = dict()
        for i in adv_data_keys:
            try:
                advanced_data[i] = self.__all_info[i]
            except KeyError:
                advanced_data[i] = f' XX( Error )XX :   data not found'

        if specific is None:
            return advanced_data
        else:
            specified_advanced_data = advanced_data.get(specific)
            return specified_advanced_data
