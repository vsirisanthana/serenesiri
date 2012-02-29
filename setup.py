import os

from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-serene",
    version = "0.0.1",
    author = "The Sirisanthana Team",
    author_email = "vsirisanthana@gmail.com",
    description = ("An enhanced djangorestframework. Serene is a RESTful framework with a touch of sirisanthana"),
    long_description = read('README.txt'),
    license = "Boost Software License - Version 1.0 - August 17th, 2003",
    keywords = "RESTful django djangorestframework",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Boost Software License - Version 1.0 - August 17th, 2003",
        ],
    packages = ['serene', 'serene.tests'],
    install_requires = ['djangorestframework'],
)

