from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
   long_description = f.read()

setup(
    name='transposer',
    version='0.0.1',
    description='Transposes columns and rows in delimited text files',
    long_description=long_description,
    url='https://github.com/keithhamilton/transposer',
    author='Keith Hamilton',
    maintainer='Keith Hamilton',
    maintainer_email='the.keith.hamilton@gmail.com',
    license='BSD License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Office/Business'
       ],
    keywords='text, csv, tab-delimited, delimited, excel, sheet, spreadsheet',
    packages=find_packages(exclude=['contrib', 'docs', 'test*', 'bin', 'include', 'lib', '.idea']),
    install_requires=[],
    package_data={
        'script': ['console_scripts.py']
    },
    data_files=[],
    entry_points={
        'console_scripts': [
           'transposer=script.console_scripts:main'
        ]
    }
)
