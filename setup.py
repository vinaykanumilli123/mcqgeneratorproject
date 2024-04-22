#to install local packages in local virtual environment
from setuptools import find_packages,setup

setup(
    name='MCQGENERATORPROJECT',
    version='0.0.1',
    author='vinay',
    author_email='sasivinay2001@gmail.com',
    install_requires=["ollama","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
) 