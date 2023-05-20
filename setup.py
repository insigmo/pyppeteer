#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from setuptools import setup
import sys

basedir = path.dirname(path.abspath(__file__))
extra_args = {}


packages = ['pyppeteer']
package_dir = {'pyppeteer': 'pyppeteer'}

readme_file = path.join(basedir, 'README.md')
with open(readme_file) as f:
    src = f.read()

try:
    from m2r import M2R
    readme = M2R()(src)
except ImportError:
    readme = src

requirements = [
    'pyee<6',
    'websockets',
    'appdirs',
    'urllib3<1.25',
    'tqdm'
]

test_requirements = [
    'syncer',
    'tornado>=5',
]

setup(
    name='pyppeteer',
    version='0.0.25',
    description=('Headless chrome/chromium automation library '
                 '(unofficial port of puppeteer)'),
    long_description=readme,

    author="Hiroyuki Takagi",
    author_email='miyako.dev@gmail.com',
    url='https://github.com/miyakogi/pyppeteer',

    packages=packages,
    package_dir=package_dir,
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'pyppeteer-install = pyppeteer.command:install',
        ],
    },

    license="MIT license",
    zip_safe=False,
    keywords='pyppeteer',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.6',
    test_suite='tests',
    tests_require=test_requirements,
    **extra_args
)
