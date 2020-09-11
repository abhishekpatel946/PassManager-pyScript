# --*-- coding: utf-8 --*--
# Copyright 2020 PassManager
# Written by: * Abhishek patel - abhishekpatel946
# https://github.com/abhishekpatel946/PassManager-pyScript
# GNU General Public License v3.0

import subprocess
import requests

def update_client_version(version):
    with open('version.txt', 'r') as vnum:
        if vnum.read != version:
            return True
        else:
            return False

def main():
    # here is a some issue <URL> with the raw file.[version.txt]
    url = 'https://raw.githubusercontent.com/abhishekpatel946/PassManager-pyScript/master/version.txt'
    r = requests.get(url)
    version = r.text
    print(version)
    if update_client_version(version) is True:
        subprocess.call(['git','pull','origin','master'])
        return print('[*] Updated to latest version: v{}..'.format(version))
    else:
        return print('[*] You are already up to date with git origin master.')


if __name__ == "__main__":
    print('[*] Checking version information...')
    main()
