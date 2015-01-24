from setuptools import setup, find_packages
from codecs import open
import os

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='transposer',
    version='0.0.3',
    description='Transposes columns and rows in delimited text files',
    long_description=(read('README.rst')),
    url='https://github.com/keithhamilton/transposer',
    author='Keith Hamilton',
    maintainer='Keith Hamilton',
    maintainer_email='the.keith.hamilton@gmail.com',
    license='BSD License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Office/Business'
       ],
    keywords='text, csv, tab-delimited, delimited, excel, sheet, spreadsheet',
    packages=find_packages(exclude=['contrib', 'docs', 'test*', 'bin', 'include', 'lib', '.idea']),
    install_requires=[],
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [
           'transposer=transposer.script.console_script:main'
        ]
    }
)
