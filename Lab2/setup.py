# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="library_serialization",
    version="0.1.2",
    description="Demo library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IamDreamcatcher/ISP",
    author="Oleg Volkovskiy",
    author_email="OlegVolkovskiy2002@yandex.ru",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(),
    include_package_data=True
)
