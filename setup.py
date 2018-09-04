from setuptools import setup, find_packages
import codecs
from os import path

here = path.abspath(path.dirname(__file__))

with codecs.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='justice',
    version='sketch',
    description='A classifier for lightcurve',
    long_description=long_description,
    url='https://github.com/tedsinger/quaver',
    packages=find_packages(),
    install_requires=[
        'tensorflow',
        'matplotlib',
        'pandas',
        'scipy',
        'george',
        'gpy'
    ],
    extras_require={
        'dev': ['autopep8',
                'ipython',
                'jupyter',
                'pytest',
                'yapf']
    }
)
