import json
from .default_notebook import DefaultNotebook


class JupyterNotebook(DefaultNotebook):
    """
    Class that holds the Jupyter notebook information deserialized from a JSON object
    """

    def __init__(self, data=None):
        if data is not None:
            super(JupyterNotebook, self).__init__(data)

    @property
    def json_data(self):
        return json.dumps(self.__dict__)
