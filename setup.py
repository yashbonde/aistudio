from setuptools import setup

'''
with open("README.md", "r") as fh:
    long_description = fh.read()
'''
long_description = 'Software to Handle AI Research Needs'

setup(name='aistudio',
      version='0.1',
      scripts=['aistudio'] ,
      author="Yash Bonde",
      author_email="bonde.yash97@gmail.com",
      description="A Simple program to Handle AI Research Needs",
      long_description=long_description,
      long_description_content_type="text",
      url="https://github.com/yashbonde/aistudio",
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ]
    )
