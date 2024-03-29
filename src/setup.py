import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = {}
with open("version.py") as fp:
    exec(fp.read(), version)

setuptools.setup(
    name="mypackage",
    version=version['__version__'],
    author="Luis Garcia",
    author_email="luisalbertogh@hotmail.com",
    description="A small example package",
    long_description="Long description",
    long_description_content_type="text/markdown",
    url="https://github.com/luisalbertogh/oopython",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)