import json
from json import JSONDecodeError


class Helper:
    @staticmethod
    def get_dict_from_json(json_string):
        try:
            if isinstance(json_string, bytes):
                json_string = json_string.decode('utf-8')
            json_dict = json.loads(json_string)
        except (JSONDecodeError, ValueError):
            raise ValueError

        return json_dict
