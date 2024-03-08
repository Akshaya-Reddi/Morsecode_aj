from setuptools import setup

# reading long description from file
with open('Description.txt') as file:
    long_description = file.read()


# specify requirements of your package here
REQUIREMENTS = ['requests']

# calling the setup function 
setup(name='morsecode_aj',
      version='1.2.3',
      description='A module for morse code translation',
      long_description=long_description,
      url='https://https://github.com/Akshaya-Reddi/Morsecode_aj',
      author='Akshaya Reddy Anna Reddy',
      author_email='annareddyakshayar@gmail.com',
      license='MIT',
      packages=['Morse Code'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='morse code'
      )
