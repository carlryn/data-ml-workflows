from setuptools import find_packages, setup

INSTALL_REQUIRES = [
    'sklearn',
    'numpy',
    'pandas',
    'scipy'
]

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Python package for simple model optimization for demo of data-ml-workflow tools',
    author='Carl Rynegardh',
    license='MIT',
    install_requires=INSTALL_REQUIRES,
)
