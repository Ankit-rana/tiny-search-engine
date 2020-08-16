import os
from setuptools import setup


setup(
    name = "tiny-search-engine",
    version = "0.0.1",
    author = "Ankit Rana",
    author_email = "connect.ankit.rana@gmail.com",
    description = ("An demonstration of how to implement a search engine in Python."),
    long_description=read('README.md'),
    entry_points={
        'console_scripts': [
            'crawler=crawler:main',
            'indexer=indexer:main',
            'query_engine=queryEngine:main'
        ],
    },
)
