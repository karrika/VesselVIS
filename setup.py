# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion", "urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="STM Voyage Information Service SeaSWIM API",
    author_email="per.lofbom@sjofartsverket.se",
    url="",
    keywords=["Swagger", "STM Voyage Information Service SeaSWIM API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    long_description="""\
    Voyage Information Service API facing SeaSWIM through SSC exposing interfaces to SeaSWIM stakeholders
    """
)

