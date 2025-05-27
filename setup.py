# setup.py
from setuptools import setup, find_packages

setup(
    name="car-cli",
    version="0.1",
    packages=find_packages(),  # Automatically finds your modules/packages
    include_package_data=True,
    install_requires=[
        "click",
        "sqlalchemy",
    ],
    entry_points={
        "console_scripts": [
            "car-cli=car_cli.cli:cli",
        ],
    },
)