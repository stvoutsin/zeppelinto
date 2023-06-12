import json
from .default_notebook import DefaultNotebook


class ZeppelinNotebook(DefaultNotebook):
    """
    Class that holds the Zeppelin notebook information deserialized from a JSON object
    """

    def __init__(self, data):
        super(ZeppelinNotebook, self).__init__(data)
