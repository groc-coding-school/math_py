import os
from setuptools import setup

setup (
        name='math_py',
        version='0.1.0',
        license='Apache License 2.0',
        author='Christopher Amadra Titus',
        packages= find_packages('src'),
        package_dir={'': 'src'},
        long_description='README.md',
        author_email='groc.coders.schools@gmail.com',
        url='https://groc-coders.blogspot.com',
        download_url='https://groc-coders.blogspot.com/downloads.html',
        version='0.1.0',
        description='A simple math calculator package',
        packages=['math_py'],
        zip_safe=False
    )