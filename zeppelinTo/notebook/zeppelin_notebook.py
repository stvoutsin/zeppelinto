import json
from .notebook import Notebook


class ZeppelinNotebook(Notebook):
    """
    Class that holds the Zeppelin notebook information deserialized from a JSON object
    """


    def __init__(self, data):
        super(ZeppelinNotebook, self).__init__(data)
