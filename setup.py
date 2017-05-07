from setuptools import setup

setup(
    name="Tree",
    version="0.1b5",
    description="A module for creating fractal trees",
    url="https://github.com/PixelwarStudio/PyTree",
    author="Pixelwar",
    author_email='janko.matthes@gmx.net',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    install_requires=[
        "Pillow"
    ],
    license="MIT",
    packages=["Tree"],
    zip_safe=False
)
