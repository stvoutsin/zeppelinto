import logging
from os.path import dirname
from config import config
from znotebook import ZeppelinNotebook
from znotebook import JupyterNotebook


class ZeppelinConverter:
    """
    Convert a Zeppelin Notebook into Python or Jupyter notebooks
    """

    def __init__(self, notebook=None):
        self.notebook = notebook

    @staticmethod
    def _clean_cell(text: str, ignore_interpreter_binding: bool = False) -> str:
        """
        Clean a Cell

        Args:
            text: The cell text
            ignore_interpreter_binding: Whether to ignore interpreter binding

        Returns:
            The cleaned text
        """
        if "%pyspark" in text:
            if not ignore_interpreter_binding:
                text = text.replace("%pyspark", config.PYSPARK_CONTEXT_INIT, 1)
            else:
                text = text.replace("%pyspark", "", 1)

        return text

    def load_notebook(self, notebook: str) -> None:
        """
        Load a notebook given its path into memory into a Notebook instance

        Args:
            notebook: The notebook path
        """
        try:
            with open(notebook, encoding="utf-8-sig") as notebook_file:
                self.notebook = ZeppelinNotebook(data=notebook_file)
        except Exception as e:
            logging.error(f"Exception encountered while loading notebook: {str(e)}")
            if config.DEBUG:
                logging.debug(e)

    def to_python(self, name: str = None) -> str:
        """
        Converts the notebook into a Python file

        Args:
            name: The name of the Python file

        Returns:
            The file name of the new Python file
        """
        output = "#!/usr/bin/python\n"

        if not self.notebook:
            logging.error("No notebook loaded. Unable to convert to Python")
            return ""

        if not name:
            name = (
                self.notebook.name + ".py"
                if self.notebook.name
                else config.DEFAULT_PY_NAME
            )

        counter = 0

        for cell in self.notebook.paragraphs:
            if cell.get("text"):
                if counter > 0:
                    output += self._clean_cell(
                        cell["text"], ignore_interpreter_binding=True
                    )
                else:
                    output += self._clean_cell(cell["text"])
                counter += 1

        try:
            if not name.endswith(".py"):
                name = config.DEFAULT_OUTPUT_DIR + name + ".py"
            else:
                name = config.DEFAULT_OUTPUT_DIR + name

            with open(name, "wt") as py_file:
                py_file.write(output)
        except Exception as e:
            logging.error(f"Exception encountered while writing Python file: {str(e)}")
            if config.DEBUG:
                logging.debug(e)

        if config.DEBUG:
            logging.debug(f"Python Code:\n {output}")

        return name

    def to_jupyter_notebook(self, name: str = None) -> str:
        """
        Converts a Zeppelin Notebook to a Jupyter notebook

        Args:
            name: The name of the Jupyter notebook

        Returns:
            The file name of the new Jupyter notebook
        """
        if not self.notebook:
            logging.error("No notebook loaded. Unable to convert to Jupyter")
            return ""

        jupyter_notebook = JupyterNotebook()

        if not name:
            name = (
                self.notebook.name
                if self.notebook.name
                else config.DEFAULT_JUPYTER_NAME
            )

        jupyter_notebook.cells = []
        jupyter_notebook.metadata = config.JHUB_METADATA
        jupyter_notebook.nbformat = config.JHUB["nbformat"]
        jupyter_notebook.nbformat_minor = config.JHUB["nbformat_minor"]

        counter = 0

        for cell_text in self.notebook.paragraphs:
            cell = {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [],
            }

            cell_text_list = self._clean_cell(cell_text["text"]).splitlines()

            for cell_line in cell_text_list:
                output = ""
                if counter > 0:
                    output += self._clean_cell(
                        cell_line, ignore_interpreter_binding=True
                    )
                else:
                    output += self._clean_cell(cell_line)

                output += "\n"
                cell["source"].append(output)
                counter += 1

            jupyter_notebook.cells.append(cell)

        if config.DEBUG:
            logging.debug(f"Jupyter Notebook:\n {jupyter_notebook.__dict__}")

        try:
            if not name.endswith(".ipynb"):
                name = config.DEFAULT_OUTPUT_DIR + name + ".ipynb"
            else:
                name = config.DEFAULT_OUTPUT_DIR + name

            with open(name, "wt") as jupyter_file:
                jupyter_file.write(jupyter_notebook.json_data + "\n")
        except Exception as e:
            logging.error(
                f"Exception encountered while writing Jupyter Notebook file: {str(e)}"
            )
            if config.DEBUG:
                logging.debug(e)

        return name

    def convert_to_python(self, file_path: str) -> str:
        """
        Convert a Zeppelin notebook to a Python file

        Args:
            file_path: The path of the Zeppelin notebook file

        Returns:
            The file name of the new Python file
        """
        self.load_notebook(file_path)
        pyfile = self.to_python(file_path)
        return pyfile

    def convert_to_jupyter(self, file_path: str) -> str:
        """
        Convert a Zeppelin notebook to a Jupyter notebook

        Args:
            file_path: The path of the Zeppelin notebook file

        Returns:
            The file name of the new Jupyter notebook
        """
        self.load_notebook(file_path)
        pyfile = self.to_jupyter_notebook(file_path)
        return pyfile


if __name__ == "__main__":
    print(
        "Converting Sample Notebook to Python:\n-------------------------------------"
    )
    ZeppelinConverter().convert_to_python("data/sample-notebook.json")
    print(
        "Converting Sample Notebook to Jupyter:\n--------------------------------------"
    )
    ZeppelinConverter().convert_to_jupyter("data/sample-notebook.json")

    ZeppelinConverter().convert_to_python("/home/stelios/Desktop/test.json")
