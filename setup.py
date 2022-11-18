from setuptools import setup, find_packages

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="py-gfm",
    version="2.0.0",
    description="An implementation of Github-Flavored Markdown written as an "
    "extension to the Python Markdown library.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Dart Team, Alexandre Macabies",
    author_email="web+oss@zopieux.com",
    url="https://github.com/zopieux/py-gfm",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["markdown>=3.3,<4"],
    python_requires=">=3.8",
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Markup",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
