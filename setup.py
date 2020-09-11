# --*-- coding: utf-8 --*--
# Copyright 2020 PassManager
# Written by: * Abhishek patel - abhishekpatel946
# https://github.com/abhishekpatel946/PassManager-pyScript
# GNU General Public License v3.0

from setuptools import setup
import os

# requires depedancies
setup(
      version='0.1',
      description='PassManager',
      url='https://github.com/abhishekpatel946/PassManager-pyScript',
      author='Abhishek Patel',
      author_email='abhishekpatel946@gmail.com',
      license='GNU General Public License v3.0',
      packages=['lib'],
      install_requires=[
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',
        'cryptography',
        'gspread',
        'oauth2client',
        'alive-progress',
      ],
    )

