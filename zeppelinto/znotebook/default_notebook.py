import json


class DefaultNotebook(object):
    """
    Class that holds the notebook information deserialized from a JSON object
    """

    def __init__(self, data):
        jsondata = json.load(data)
        self.__dict__ = jsondata
        self.__json_data = jsondata

    @property
    def json_data(self):
        return self.__json_data

    @json_data.setter
    def json_data(self, data):
        self.__json_data = data
