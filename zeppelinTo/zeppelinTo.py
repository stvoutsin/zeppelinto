import json
from .notebook import ZeppelinNotebook
from .notebook import JupyterNotebook
from .notebook import Notebook
import logging
from . import config as cfg

class ZeppelinTo(object):
    """
    Convert a Zeppelin Notebook into python, or jupyter notebooks

    """

    def __init__(self, notebook=None):
        self.notebook = notebook


    def isvalid(self, notebook):
        """
        TODO: Check if valid notebook / Or remove class
        """
        return True


    def _clean_cell(self, text, ignore_interpreter_binding=False):
        """
        Clean a given cell, remove unneeded text and tags
        Parameters
        ----------
        text: str
            The cell text

        Returns
        -------
        newtext : str
           The cleaned text

        """

        if text.find("%pyspark") != -1:
            if ignore_interpreter_binding==False:
                text = text.replace("%pyspark", cfg._PYSPARK_CONTEXT_INIT, 1)
            else:
                text = text.replace("%pyspark", "", 1)

        return text


    def load_notebook(self, notebook=None):
        """
        Load a notebook given it's path into memory into a Notebook instance

        Parameters
        ----------
        notebook : str
            The notebook path

        Returns
        -------
           self

        """
        if notebook:

            if self.isvalid(notebook):
                try:
                    with open(notebook, encoding='utf-8-sig') as notebook_file:
                        self.notebook = ZeppelinNotebook(data=notebook_file)
                except Exception as e:
                    print ("Exception encountered while loading notebook: " + str(e))
                    if cfg._DEBUG:
                        logging.debug(e)

        return self


    def to_python(self, name=None):
        """
        Converts the notebook into a Python file

        """

        output = "#!/usr/bin/python\n"

        if not self.notebook:
            print ("No notebook loaded..Unable to convert to Python")
            return


        if self.notebook.name and name==None:
            name = self.notebook.name + ".py"
        elif not name:
            name = cfg._DEFAULT_PY_NAME

        counter = 0

        for cell in self.notebook.paragraphs:
            if cell["text"]:
                if counter>0:
                    output+= self._clean_cell(cell["text"], ignore_interpreter_binding = True)
                else :
                    output+= self._clean_cell(cell["text"])
            counter += 1

        try:

            if not name.endswith("py"):
                name = cfg._DEFAULT_OUTPUT_DIR + name + ".py"
            else:
                name = cfg._DEFAULT_OUTPUT_DIR + name 

            with open(cfg._DEFAULT_OUTPUT_DIR + name, "wt") as py_file:
                py_file.write(output)
        except Exception as e:
            print ("Exception encountered while writing Python file: " + str(e))
            if cfg._DEBUG:
                logging.debug(e)

        if cfg._DEBUG:
            print(f"Python Code:\n {output}")        

        return self


    def to_jupyter_notebook(self, name=None):
        """
        Converts a Zeppelin Notebook to a Jupyter equivalent
        """

        if not self.notebook:
            print ("No notebook loaded..Unable to convert to Jupyter")
            return

        jupyter_notebook = JupyterNotebook()

        if self.notebook.name and name==None:
            name = self.notebook.name
        elif not name:
            name = cfg._DEFAULT_JUPYTER_NAME

        jupyter_notebook.cells = []
        jupyter_notebook.metadata = cfg._JHUB_METADATA
        jupyter_notebook.nbformat = cfg._JHUB["nbformat"]
        jupyter_notebook.nbformat_minor = cfg._JHUB["nbformat_minor"]

        counter = 0

        for cell_text in self.notebook.paragraphs:

             cell = {}
             cell["cell_type"] = "code"
             cell["execution_count"] = None
             cell["metadata"] = {}
             cell["outputs"] = []
             cell["source"] = []

             cell_text_list = self._clean_cell(cell_text["text"]).splitlines()

             for cell_line in cell_text_list:
                 output = ""
                 if counter>0:
                    output+=self._clean_cell(cell_line, ignore_interpreter_binding = True)
                 else :
                    output+=self._clean_cell(cell_line)

                 output += "\n"
                 cell["source"].append(output)
                 counter+=1

             jupyter_notebook.cells.append(cell)

        if cfg._DEBUG:
            print(f"Jupyter Notebook:\n {jupyter_notebook.__dict__}")        


        try:
            if not name.endswith("ipynb"):
                name = cfg._DEFAULT_OUTPUT_DIR + name + ".ipynb"
            else:
                name = cfg._DEFAULT_OUTPUT_DIR + name

            with open(name, "wt") as jupyter_file:
                jupyter_file.write(jupyter_notebook.json_data)
        except Exception as e:
            print ("Exception encountered while writing Jupyter Notebook file: " + str(e))
            if cfg._DEBUG:
                logging.debug(e)


        return self


    def convert_to_python(file_path):
        """
        Convert a Zeppelin notebook to a Python file

        Parameters
        ----------
        file : str
            The path to the Zeppelin file we want to convert
        Returns
        -------
        """
        zep = ZeppelinTo()
        zep.load_notebook(file_path)
        pyfile = zep.to_python()


    def convert_to_jupyter(file_path):
        """
        Convert a Zeppelin notebook to a Python file

        Parameters
        ----------
        file : str
            The path to the Zeppelin file we want to convert
        Returns
        -------
        """
        zep = ZeppelinTo()
        zep.load_notebook(file_path)
        pyfile = zep.to_jupyter_notebook()


if __name__ == "__main__":
    print ("Converting Sample Notebook to Python:\n-------------------------------------\n")
    ZeppelinTo.convert_to_python("data/sample-notebook.json")
    print ("Converting Sample Notebook to Jupyter:\n--------------------------------------\n")
    ZeppelinTo.convert_to_jupyter("data/sample-notebook.json")
