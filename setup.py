import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pure-python-brl", # Replace with your own username
    version="0.0.1",
    author="Oliver Daniels-Koch",
    description="pure python bayesian rule list classifier",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
