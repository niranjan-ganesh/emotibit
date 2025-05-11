# setup.py
from setuptools import setup, find_packages

setup(
    name="emoti",
    version="1.3.9",
    author="Niranjan Ganesan",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
