from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ftpcli',
    packages=['ftpcli'],

    version='1.0.2',

    license='MIT',

    install_requires=[],

    author='nanato12',
    author_email='admin@nanato12.info',

    url='https://github.com/nanato12/ftpcli',

    description='To easy ftp client.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='ftpcli ftp-client',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only'
    ],
)
