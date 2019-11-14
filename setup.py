from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='HeStark',
      version='0.0.1',
      description='Calculate the Stark map for triplet Rydberg helium',
      url='',
      author='Klaudia Gawlas',
      author_email='klaudia.gawlas.13@ucl.ac.uk',
      license='BSD 3-clause',
      packages=['HeStark'],
      include_package_data=True,
      zip_safe=False)
