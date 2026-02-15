from setuptools import setup, find_packages

setup(
    name='Binary_analysis',  
    version='0.1',  
    packages=find_packages(), 
    install_requires=[
        "astroplan", "numpy", "astropy",
        "julian", "sympy", "datetime", 
        "matplotlib",
    ],
    author='Gaspard Duchêne, Elsa Huby, Marc-Antoine Martinod, Tomoyuki Kudo, Sebastien Vievard',
    author_email='',
    description='Tools to study binary systems',
    long_description=open('README.md').read(),  
)
