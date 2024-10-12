"""
Package the project for distribution.
The only scripts are the std_in_sum.py and std_in_sum_cli.py
A cli executable is created for the std_in_sum_cli
"""
from setuptools import setup

setup(
    name="std_in_sum",
    version="0.1",
    py_modules=["std_in_sum", "std_in_sum_cli"],  # Le code python
    author="Christophe",
    entry_points={"console_scripts": [
        "std_in_sum = std_in_sum_cli:main",  # Une CLI façe à sa fonction main
    ]},
    install_requires=[],  # dépendances
)
