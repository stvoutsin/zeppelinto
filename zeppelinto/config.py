class Config:
    DEBUG = True
    DEFAULT_PY_NAME = "zeppelin_notebook.py"
    DEFAULT_JUPYTER_NAME = "jupyter_notebook.py"
    DEFAULT_OUTPUT_DIR = ""
    PYSPARK_CONTEXT_INIT = (
        "from pyspark import SparkConf, SparkContext\nconf = "
        'SparkConf().setMaster("yarn-client")\nsc = SparkContext(conf = conf)'
    )
    JHUB_METADATA = {}
    JHUB_METADATA["kernelspec"] = {}
    JHUB_METADATA["kernelspec"]["display_name"] = "Python 3"
    JHUB_METADATA["kernelspec"]["language"] = "python"
    JHUB_METADATA["kernelspec"]["name"] = "python3"
    JHUB_METADATA["language_info"] = {}
    JHUB_METADATA["language_info"]["display_name"] = "Python 3"
    JHUB_METADATA["language_info"]["language"] = "python"
    JHUB_METADATA["language_info"]["name"] = "python3"
    JHUB_METADATA["file_extension"] = ".py"
    JHUB_METADATA["mimetype"] = "text/x-python"
    JHUB_METADATA["name"] = "python"
    JHUB_METADATA["nbconvert_exporter"] = "python"
    JHUB_METADATA["pygments_lexer"] = "python"
    JHUB_METADATA["version"] = "3.6.7"
    JHUB = {"nbformat": 4, "nbformat_minor": 2}


config = Config()
