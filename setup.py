from setuptools import setup, find_packages

setup(
    name="mwan",
    version="2.0",
    author="mwan (Josuan)",
    author_email="noahboat231@gmail.com",
    description="My first python module",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["datetime"],
    entry_points={"console_scripts": ["cloudquicklabs1 = src.mwan:mwan"]},
)