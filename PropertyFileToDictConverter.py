
class PropertyFileToDictConverter:
    
    @staticmethod
    def __is_valid_key_value_pair(line: str) -> bool:
        """ Validates if the line has proper data which can be parsed into a key value pair
        :param line: 
        :return: boolean result of check 
        """
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
        """ Splits and converts a line into key and value
        :param line: 
        :return: tuple with key and value
        """
        key, value = line.split('=')
        key = key.strip()
        value = value.strip()
        return key, value
    
    @staticmethod
    def parse(valid_file_name) -> dict:
        """ Parses a input property file and returns a dict object with all the valid key value pairs from the given input file
        :param valid_file_name: property file name
        :return: dict object 
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
