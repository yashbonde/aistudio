import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='aistudio',
      version='0.0.1',
      author="Yash Bonde",
      author_email="bonde.yash97@gmail.com",
      description="A Simple program to Handle AI Research Needs",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/yashbonde/aistudio",
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ]
    )
