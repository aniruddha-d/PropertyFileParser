from collections import OrderedDict


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


class PropertyWriter:

    __properties: OrderedDict = OrderedDict()

    def set_value(self, key: str, value: str):
        """
        :param key:
        :param value:
        :return:
        """

        self.__properties[key] = value

    def dump(self, filename: str):
        """
        :param filename:
        :return:
        """

        with open(filename, 'wt') as fl:
            for key, value in self.__properties.items():
                line = key + ' = ' + value + '\n'
                fl.write(line)

