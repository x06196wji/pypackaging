from setuptools import setup, find_packages

with open('README.md', 'rb') as f:
    readme = f.read()

setup(name='trytopkg',
      version='0.0.1',
      description='A python package test',
      long_description=readme,
      author='Brett Chen',
      author_email='x06196wji@gmail.com',
      url='https://github.com/x06196wji/pypackaging',
      packages=find_packages(exclude=('tests')),
      keywords=['package', 'example'])
