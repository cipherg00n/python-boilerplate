"""Python setup.py for python_boilerplate package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("python_boilerplate", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="python_boilerplate",
    version=read("python_boilerplate", "VERSION"),
    description="Awesome python_boilerplate created by cipherg00n",
    url="https://github.com/cipherg00n/python-boilerplate/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="cipherg00n",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["python_boilerplate = python_boilerplate.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
