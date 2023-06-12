# zeppelinTo

Python Client to Convert a Zeppelin Notebook into: Python or Jupyter Notebook fies


## Installation Instructions (virtualenv)

### Install pip & virtualenv

    pip3 install virtualenv

### Grab a copy of the github project  

    git clone https://github.com/stvoutsin/zeppelinTo.py.git

### Initialize a virtual environment in the project directory

    virtualenv --python=/usr/bin/python3 zeppelinto/

### Activate the virtualenv 

    cd zeppelinTo/
    source bin/activate


### Install ZeppelinTo using pip 

    pip3 install zeppelinto/

## Run Python and import ZeppelinConverter

    python
    

    from zeppelinto import ZeppelinConverter`
    ZeppelinConverter().convert_to_python("data/sample-notebook.json")

