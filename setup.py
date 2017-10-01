from setuptools import setup
import Tree

def readme():
    with open("README.rst") as f:
        return f.read()

NAME = Tree.__name__
VERSION = Tree.__version__
AUTHOR = Tree.__author__
DESCRIPTION = "A package for creating and drawing trees"
LONG_DESCRIPTION = readme()
URL = "https://github.com/PixelwarStudio/PyTree"
REQUIRED = [
    "Pillow",
    "svgwrite",
    "setuptools",
    "click"
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,
    author=AUTHOR,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    install_requires=REQUIRED,
    license="MIT",
    packages=["Tree"],
    entry_points = {
        "console_scripts": ["tree-cli=Tree.cli:create_tree"],
    },
    zip_safe=False,
    include_package_data=True
)
