class NeoWs:

    def __init__(self, all_info: dict):

        self.__all_info = all_info

        self.__name_limited = self.__all_info['name_limited']
        self.__id_code = self.__all_info['id_code']

        self.__estimated_diameter = self.__all_info['estimated_diameter']
        self.__close_approach_data = self.__all_info['close_approach_data']
        self.__orbital_data = self.__all_info['orbital_data']

    def __str__(self):
        return self.__all_info['name']

    def basic_data(self):
        others_data = ['estimated_diameter', 'close_approach_data', 'orbital_data']

        basic_data = dict()
        for i in self.__all_info:
            if i not in others_data:
                basic_data[i] = self.__all_info[i]

        return basic_data

    @property
    def name(self):
        return self.__name_limited

    @property
    def id_code(self):
        return self.__id_code

    @property
    def estimated_diameter(self):
        return self.__estimated_diameter

    @property
    def close_approach_data(self):
        return self.__close_approach_data

    @property
    def orbital_data(self):
        return self.__orbital_data
