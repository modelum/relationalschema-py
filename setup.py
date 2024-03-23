from setuptools import setup, find_packages

setup(
    name='relationalschema-py',
    version='0.1',
    packages=find_packages(),
    package_data={'relationalschema-py': ['relationalschema.ecore', 'relationalschema/*']},
    include_package_data=True,
    install_requires=[
        "pyecore>=0.15.0"
    ]
)