from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'WebScrapes MyAnimeList.com'
LONG_DESCRIPTION = 'It gathers useful data and formats it into a json format.'

# Setting up
setup(
    name="MalTagger",
    version=VERSION,
    author="SilverVeritas (Patrick Serrano)",
    author_email="<Hello@pserrano.net>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['beautifulsoup4', 'requests'],
    keywords=['python', 'beautifulsoup4', 'requests'],
    classifiers=[
    ]
)