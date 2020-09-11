# --*-- coding: utf-8 --*--
# Copyright 2020 PassManager
# Written by: * Abhishek patel - abhishekpatel946
# https://github.com/abhishekpatel946/
# Licesed <exists>

from setuptools import setup
import os


# requires depedancies
setup(
      version='0.1',
      description='PassManager',
      #url='http://github.com/storborg/PassManager-pyScript',
      author='Abhishek Patel',
      author_email='abhishekpatel946@gmail.com',
      license='MIT',
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

