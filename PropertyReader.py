

class PropertyFileToDictConverter:

    @staticmethod
    def __is_valid_key_value_pair(line: str):
        if not line:
            return False
        if line[0] == '#':
            return False
        if '=' in line:
            return True
        else:
            return False

    @staticmethod
    def __parse_line(line: str):
        """ Line from a property file to convert into key and value
        :param line:
        :return:
        """
        key, value = line.split('=')
        key = key.strip()
        value = value.strip()
        return key, value

    @staticmethod
    def parse(valid_file_name)-> dict:
        """ Parses a input property file and returns a dict object
        :param valid_file_name: property file name
        :return:
        """
        dict_props = dict()
        with open(valid_file_name) as file:
            file_by_lines = file.readlines()
        for line in file_by_lines:
            line = line.strip()
            if PropertyFileToDictConverter.__is_valid_key_value_pair(line):
                key, value = PropertyFileToDictConverter.__parse_line(line)
                dict_props[key] = value
        return dict_props


class PropertyReader:
    """ This class stores the keys and values and serves them based on request """
    __properties: dict
    __fl_name: str

    def __init__(self, prop_file_name: str):
        """
        :param prop_file_name:
        """
        self.__fl_name = prop_file_name
        self.__properties = PropertyFileToDictConverter.parse(self.__fl_name)

    def load(self):
        """
        :return:
        """
        self.__properties = PropertyFileToDictConverter.parse(self.__fl_name)

    def get_value(self, key: str)-> str:
        """
        :param key:
        :return:
        """
        if key in self.__properties:
            value = self.__properties[key]
        else:
            raise KeyError('Key not found: ' + key)

        return value

