from setuptools import setup, find_packages

setup(
    name='ai_compliance_adk',
    version='0.1',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
)