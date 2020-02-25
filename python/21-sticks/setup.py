import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sticks",
    version="0.0.1",

    author="Mike Butt",
    author_email="mjbutt@hotmail.co.uk",
    description="A package for playing the game 21 sticks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
        classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[]
)
