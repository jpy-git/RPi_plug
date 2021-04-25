from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="RPi_plug",
    version="0.0.1",
    author="Joseph Young",
    author_email="josephyoung.jpy@gmail.com",
    description="Python package for controlling Energenie Remote Controlled Sockets",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/jpy-git/RPi_plug",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
)
