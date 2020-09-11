# --*-- coding: utf-8 --*--
# Copyright 2020 PassManager
# Written by: * Abhishek patel - abhishekpatel946
# https://github.com/abhishekpatel946/PassManager-pyScript
# GNU General Public License v3.0

import os
import sys
import time
import pip
import getpass
from setuptools import setup
from cryptography.fernet import Fernet

BLUE, RED, WHITE, YELLOW, MEGENTA, GREEN, END = ['\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m']

# run as a root
if not os.geteuid() == 0:
    sys.exit('PassManager must be run as root')

# Clear
def clear():
    os.system('clear')

# Splash Screen
def warn():
    sys.stdout.write(
        GREEN + '''

########     ###     ######   ######  ##     ##    ###    ##    ##    ###     ######   ######## ########  
##     ##   ## ##   ##    ## ##    ## ###   ###   ## ##   ###   ##   ## ##   ##    ##  ##       ##     ## 
##     ##  ##   ##  ##       ##       #### ####  ##   ##  ####  ##  ##   ##  ##        ##       ##     ## 
########  ##     ##  ######   ######  ## ### ## ##     ## ## ## ## ##     ## ##   #### ######   ########  
##        #########       ##       ## ##     ## ######### ##  #### ######### ##    ##  ##       ##   ##   
##        ##     ## ##    ## ##    ## ##     ## ##     ## ##   ### ##     ## ##    ##  ##       ##    ##  
##        ##     ##  ######   ######  ##     ## ##     ## ##    ## ##     ##  ######   ######## ##     ##   
              
 ''' + RED + '''     
              _________               
             (         )         _____
             ##        ##       ($$$$$$)         ''' + RED + '''      [ Disclaimer Alert ] ''' + RED + '''
             ##        ##      ($$(__)$$)        ''' + WHITE + '''  Not Resposible For Misuse ''' + RED + '''
            (+----------+)     ($$$$$$)          ''' + WHITE + '''    or Illegal Purposes. ''' + RED + '''
            |     __     |     //   /            ''' + WHITE + ''' Use it just for ''' + RED + '''WORK''' + WHITE + ''' or ''' + RED + '''EDUCATIONAL''' + WHITE + ''' purpose ! ''' + RED + '''
            |    (  )    |    // --/
            |     ||     |   // --/    
            |     ||     |  // __/   
            +------------+  \__/               ''' + END)

# Heading
def heading():
    os.system('clear')
    sys.stdout.write(

        GREEN + '''        
          ##********************## 
        ****|| '''+RED+'''  I SECURE YOU '''+GREEN+'''  ||****                      
         @@@@******************@@@@           
         ''' + YELLOW + '''  
             _________             
            (         )         _____
            ##        ##       ($$$$$$) 
            ##        ##      ($$(__)$$)      
           (+==========+)     ($$$$$$)    
           |     __     |     //   /        
           |    (  )    |    // --/      
           |     ||     |   // --/      
           |     ||     |  // __/     
           +============+  \__/           version: '''+WHITE+'''1.0'''+YELLOW+'''
                                          by:''' + WHITE + ' Abhishek Patel (' + YELLOW + 'abhishekpatel946' + WHITE + ')' + '\n' + '\n' + END)    
    print('\n'' {0}[{1}I{0}]{1} Install'.format(YELLOW, END) + ' {0}[{1}Q{0}]{1} Quit'.format(YELLOW, END) + '\n')
    print(GREEN+'''\n\n\n Install the require dependecies...''' + YELLOW+'''\n PRESS ['''+WHITE+ '''I'''+YELLOW+'''] TO INSTALL''' + END )
   

# installing python module
def install():
    try:
        print('Installing dependancies....')

        # google-api;s and cryptography lib;s
        api_python_client = 'google-api-python-client'
        auth_httplib2 = 'google-auth-httplib2'
        auth_oauthlib = 'google-auth-oauthlib'
        cryptography_lib = 'cryptography'
        gspread_lib = 'gspread'
        oauth2client_lib = 'oauth2client'
        alive_progress = 'alive-progress'
        # pip installer module
        if hasattr(pip, 'main'):
            pip.main(['install', api_python_client])
            pip.main(['install', auth_httplib2])
            pip.main(['install', auth_oauthlib])
            pip.main(['install', cryptography_lib])
            pip.main(['install', gspread_lib])
            pip.main(['install', oauth2client_lib])
            pip.main(['install', alive_progress])
        else:
            pip._internal.main(['install', api_python_client])
            pip._internal.main(['install', auth_httplib2])
            pip._internal.main(['install', auth_oauthlib])
            pip._internal.main(['install', cryptography_lib])
            pip._internal.main(['install', gspread_lib])
            pip._internal.main(['install', oauth2client_lib])
        
        # run the setup module and install require dependecies        
        os.system('sudo python setup.py install')
       
        # all done
        sys.stdout.write('''\n\n''' + GREEN + ''' All Dependecies and libraries Succefully installed!!! ''' + '\n\n\n' + END)
        input(YELLOW+'''\n\n\nPRESS ['''+WHITE+ '''ENTER'''+YELLOW+'''] TO CONTINUE''' + END )
       
        # redirect to register module            
        register()

    except:
        # print('Something went wrong')
        raise SystemExit
        pass

# regiser_user
def register():
    os.system('clear')
    sys.stdout.write(

        GREEN + '''        
          ##********************## 
        ****|| '''+RED+'''  I SECURE YOU '''+GREEN+'''  ||****                      
         @@@@******************@@@@           
         ''' + YELLOW + '''  
             _________             
            (         )         _____
            ##        ##       ($$$$$$) 
            ##        ##      ($$(__)$$)      
           (+==========+)     ($$$$$$)    
           |     __     |     //   /        
           |    (  )    |    // --/      
           |     ||     |   // --/      
           |     ||     |  // __/     
           +============+  \__/           ''' + END)
    
    print('\n\n {0}[{1}Q{0}]{1} Quit'.format(YELLOW, END) + '\n')
    
    uname = input(GREEN+'''\n\n\n ENTER THE USERNAME ''' +YELLOW+ ''' >>> ''' +END )
    upass = getpass.getpass(GREEN+'''\n\n\n ENTER THE PASSWORD ''' +YELLOW+ ''' >>> ''' +END )
    

    write_key()
    key = load_key()
    
    # initialize the Fernet class
    f = Fernet(key)

    # cipher text
    uname = str(uname).encode()
    upass = str(upass).encode()

    # encrypt and username and password
    encrypted_1 = f.encrypt(uname)
    encrypted_2 = f.encrypt(upass)

    # type-casting byte to str
    encrypted_1 = str(encrypted_1)
    encrypted_2 = str(encrypted_2)

    # remove starting byte 'b' from key
    encrypted_1 = encrypted_1[1:]
    encrypted_2 = encrypted_2[1:]

    # store into the file
    with open('data/user_secret.txt', 'w') as secret_file:
        secret_file.write(encrypted_1)
        secret_file.write('\n')    # dummy space for the new line
        secret_file.write(encrypted_2)
    
    pp()

# write the key in and store
def write_key():
    key = Fernet.generate_key()
    with open('data/key.key', 'wb') as key_file:
        key_file.write(key)

# load the key from file
def load_key():
    return open('data/key.key', 'rb').read()


# last greetings  
def pp():
    clear()
    sys.stdout.write('\n\n' + GREEN + ''' Thank You for using PassManager.''' + MEGENTA + ''' KEEP CODING; & HACKING :D !!!''' + '\n\n\n' + END)
    sys.stdout.write('\n\n' + GREEN + ''' PRESS ''' + WHITE + '''[Q]''' + GREEN+ '''\n\n run the command ''' + BLUE + '''\tsudo python3 PassManager.py ''' + END)
    time.sleep(1)
    print('\n\n\n') # for the new line
    raise SystemExit
    sys.exit(0)

# main funtion
def main():
    clear()
    warn()
    input(YELLOW+'''\n\n\nPRESS ['''+WHITE+ '''ENTER'''+YELLOW+'''] TO CONTINUE''' + END )
    clear()
    heading()
    try:

        while True:
            print('\n')
            # header
            header = ('{0}root{1}> {2}'.format(YELLOW, WHITE, END))
            choise = input(header)
            
            # REINSTALL
            if choise.upper() == 'I' or choise.upper() == 'INSTALL':
                clear()
                #time.sleep(1)
                install()

            # QUIT
            if choise.upper() == 'Q' or choise.upper() == 'QUIT':
                clear()
                pp()
                print('\n')
                #time.sleep(1)
                raise SystemExit
            
            # exit
            if choise.upper() == 'EXIT' or choise.upper() == 'CLOSE':
                clear()
                pp()
                #time.sleep(1)
                raise SystemExit

    # Exception occurs
    except KeyboardInterrupt:
        clear()
        pp()
        time.sleep(1)
        sys.exit(0)


# i like this function 
if __name__ == "__main__":

    # execute the main()
    main()
