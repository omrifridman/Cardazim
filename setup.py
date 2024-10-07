from pathlib import Path
from setuptools import find_packages, setup
from typing import List


REQUIREMENTS_FILE = Path('.') / 'requirements.txt'


def _read_requirements(file: Path) -> List[str]:
    with open(file) as req_file:
        lines = req_file.readlines()
    return [line.rstrip() for line in lines]


setup(
    name='Cardazim',
    version='0.0.1',
    author='Omri Fridman',
    author_email='omrifridman@mail.tau.ac.il',
    description='Cardazim project',
    long_description='''Cardazim project''',
    packages=find_packages('cardazim'),
    install_requires=_read_requirements(REQUIREMENTS_FILE)
)
