from setuptools import setup, find_packages

setup(
    name='ml_lp1',
    version='1.0.0',
    description='All LP-1 Machine Learning Experiments in One Package',
    author='Shubham Bhorkade',
    packages=find_packages(),
    install_requires=['pandas','numpy','scikit-learn','matplotlib','scipy','mlxtend']
)
