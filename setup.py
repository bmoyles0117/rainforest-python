from setuptools import setup
from setuptools import find_packages

setup(
    name                = "rainforest",
    version             = "1.0.0",
    description         = "Rainforest API client",
    author              = "Bryan Moyles",
    author_email        = "bmoy117@gmail.com",
    url                 = "https://github.com/bmoyles0117/rainforest-python/",
    keywords            = ["rainforest"],
    install_requires    = ["mock==1.0.1", "requests==2.2.1"],
    packages            = find_packages(),
    classifiers         = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: QA :: Automation"
    ],
    long_description    = """A python module for interacting with the Rainforest API initiating tests and observing the progress of existing tests.""",
)