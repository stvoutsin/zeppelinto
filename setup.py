import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "zeppelinto",
    version = "0.1.2",
    author = "Stelios Voutsinas",
    author_email = "stv@roe.ac.uk",
    description = ("A python suite for converting Zeppelin Notebooks"),
    license = "GNU",
    keywords = "apache zeppelin convert notebook jupyter",
    url = "https://github.com/stvoutsin/zeppelinto",
    include_package_data = True,
    packages=['zeppelinto','zeppelinto.znotebook','zeppelinto.tests', 'zeppelinto'],
    package_data={'zeppelinto': ['data/*']},

    long_description="README",
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Free For Home Use",
        "Programming Language :: Python"
    ]
)
