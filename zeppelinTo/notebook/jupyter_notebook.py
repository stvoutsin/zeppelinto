import json
from .notebook import Notebook


class JupyterNotebook(Notebook):
    """
    Class that holds the Jupyter notebook information deserialized from a JSON object
    """


    def __init__(self, data=None):
        if data!=None:
            super(JupyterNotebook,self).__init__(data)

    @property
    def json_data(self):
        return json.dumps(self.__dict__)
