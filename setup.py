from setuptools import setup
import os

version = '0.1.0'


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='medius',
    version=version,
    description="Python API for Medium",
    long_description=read('README.md'),
    keywords='apis, Medium',
    author='Cléber Zavadniak',
    author_email='cleberman@gmail.com',
    url='https://github.com/cleberzavadniak/medius',
    license='MIT',
    packages=['medius'],
    package_dir={'medius': 'medius'},
    zip_safe=False,
    install_requires=['requests'],
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ),
)
