"""Simple setup file for installation of {{ cookiecutter.project_name }}

Use pip to install the package for development:

    $ python -m pip install -e .
"""

# Standard library imports
import pathlib

# Third party imports
from setuptools import setup

# Name of package
NAME = "{{ cookiecutter.repo_name }}"

# Bootstrap name of executable from {{ cookiecutter.repo_name }} package
init_path = pathlib.Path(__file__).resolve().parent / NAME / "__init__.py"
init_lines = init_path.read_text().split("\n")
EXE = [l.split()[-1].strip('"') for l in init_lines if l.startswith("__exe__ = ")].pop()


# This call to setup() does all the work
setup(
    name=NAME,
    version="{{ cookiecutter.version }}",
    packages=[NAME],
    include_package_data=True,
    install_requires=[  # In addition to requirements listed in environment.yml
        "midgard",
        "pyplugs",
    ],
    entry_points={"console_scripts": [f"{EXE}={NAME}.__main__:main"]},
)
