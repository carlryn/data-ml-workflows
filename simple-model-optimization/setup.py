# from setuptools import find_packages, setup

# INSTALL_REQUIRES = [
#     'sklearn',
#     'numpy',
#     'pandas==1.1',
#     'scipy',
#     'gensim',
# ]

# setup(
#     name='simple_model_optimization',
#     packages=find_packages(where='src'),
#     version='0.1.0',
#     description='Python package for simple model optimization for demo of data-ml-workflow tools',
#     author='Carl Rynegardh',
#     license='MIT',
#     install_requires=INSTALL_REQUIRES,
#     package_dir={"": "src"},

# )
import codecs
import os
import re

from setuptools import find_packages, setup

###############################################################################

NAME = "simple_model_optimization"
PACKAGES = find_packages(where="src")
INSTALL_REQUIRES = [
    "pandas",
    "scikit-learn",
    "matplotlib",
    "pyyaml",
    "joblib",
    "sqlalchemy",
    "attrs",
    "scikit-optimize",
]

META_PATH = os.path.join("src", NAME, "__init__.py")

###############################################################################



VERSION = "0.0.1"

setup(
    name=NAME,
    version=VERSION,
    long_description_content_type="text/markdown",
    zip_safe=False,
    python_requires=">=3.7",
    packages=PACKAGES,
    install_requires=INSTALL_REQUIRES,
    package_dir={"": "src"},
)
