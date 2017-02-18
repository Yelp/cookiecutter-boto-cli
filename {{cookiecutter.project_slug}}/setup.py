#!/usr/bin/env python

from datetime import datetime
from setuptools import setup

setup(
    name='{{ cookiecutter.project_name }}',
    version=datetime.now().strftime('%Y.%m.%d.%H%M%S'),
    packages=['{{ cookiecutter.pkg_name }}'],
    # If you directly `import` packages, put them here.
    # The full dependency tree with specific versions goes in requirements.txt
    install_requires=['arrow', 'boto3', 'botocore'],
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.script_name }} = {{cookiecutter.pkg_name}}.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
)
