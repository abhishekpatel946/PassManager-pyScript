# --*-- coding: utf-8 --*--
# Copyright 2020 PassManager
# Written by: * Abhishek patel - abhishekpatel946
# https://github.com/abhishekpatel946/
# Licesed <exists>

import os
import sys
import time
import getpass
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from cryptography.fernet import Fernet
from alive_progress import alive_bar

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
            |     __     |     //   /            ''' + WHITE + ''' Use it just for ''' + RED + '''WORK''' + WHITE + ''' or ''' + RED + '''EDUCATIONAL''' + WHITE + '''   purpose ! ''' + RED + '''
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
    print('\n {0}[{1}L{0}]{1} LOGIN'.format(YELLOW, END) + ' {0}[{1}A{0}]{1} ABOUT'.format(YELLOW, END) + ' {0}[{1}C{0}]{1} CREDITS'.format(YELLOW, END) + ' {0}[{1}U{0}]{1} UPDATE'.format(YELLOW, END) + ' {0}[{1}Q{0}]{1} Quit'.format(YELLOW, END) + '\n')                               
    
# last greetings  
def pp():
    sys.stdout.write('\n\n' + GREEN + ''' Thank You for using PassManager, KEEP CODING; & HACKING :D !!!''' + '\n\n\n' + END)

# about section3
def about():
    clear()
    warn()
    sys.stdout.write('\n'
        + YELLOW + '''
            PassManager is a simple pyScript that store your all Credentials & Passwords on 
            google as a ENCRYPTED file such that no one can access or Decrypt your CREDENTIALS.
	    On saving passwords, it gets stored on your Google account.
            It is quite simple to add delete & search CREDENTIALs easily with PassManager.
            It is a open source python script.  
	    
            You can contribute to this script & donate for help.	
	'''
        + BLUE + 
        '\n\t\t\t' + ''' https://github.com/abhishekpatel946/ ''' + END + '\n\n\n' )
    # heading()
    sys.exit(0)

# credit section
def credit():
    clear()
    warn()
    sys.stdout.write('\n\n'
        + GREEN + ''' Credits ''' + '\n' 
        + YELLOW + ''' Abhishek Patel ''' + WHITE + '''[''' + BLUE +''' https://github.com/abhishekpatel946/''' + WHITE + ''' ] ''' + END + '\n\n' )
    # heading()
    sys.exit(0)

# option;s
def option():
     print('\n {0}[{1}1{0}]{1} Add Credential '.format(BLUE, WHITE) + '\n' + ' {0}[{1}2{0}]{1} Show All Credential'.format(BLUE, WHITE) + '\n' + ' {0}[{1}3{0}]{1} Delete Credential'.format(BLUE, WHITE) + '\n' + ' {0}[{1}4{0}]{1} unHide Credential'.format(BLUE, WHITE) + '\n' + ' {0}[{1}5{0}]{1} Link'.format(BLUE, WHITE) + '\n' + ' {0}[{1}U{0}]{1} Update'.format(BLUE, WHITE) + '\n' + ' {0}[{1}Q{0}]{1} Quit'.format(BLUE, WHITE) + '\n')

# bringing the values from the file
def file(file_contents):
    file_value = open('data/user_secret.txt', 'r+')
    f = file_value.readlines()
    for x in f:
        file_contents.append(x)
    return file_contents

# matching with the user values
def auth(file_contents, username, password):
    # initialize cypto
    cryptInitial()

    # decrypt the encrypted text
    uname = str(file_contents[0]).rstrip()
    uname = uname.encode()
    uname = f.decrypt(uname)
    upass = str(file_contents[1]).rstrip()
    upass = upass.encode()
    upass = f.decrypt(upass)
    
    # change the user input string to byte
    username = username.encode()
    password = password.encode()

    # matching the username && password
    if username == uname and password == upass:
        option()
    else:
        print(RED + '\t\n INVALID CREDENTIALS ' + END)
        time.sleep(2)
        heading()

# generate a key and save it into a file
def write_key():
    key = Fernet.generate_key()
    with open('data/key.key', 'wb') as key_file:
        key_file.write(key)

# load the key from the current directory named 'key.key'
def load_key():
    return open('data/key.key', 'rb').read()

# intiaization
def cryptInitial():
    # global declaration
    global key 
    key = load_key()
     # initialize the Fernet class
    global f 
    f = Fernet(key)

    return key, f

# Enrypt the data
def Encryption(data1, data2):
    # define globally
    global encrypted_1
    global encrypted_2
    cryptInitial()
    # cipher text
    data_1 = str(data1).encode()
    data_2 = str(data2).encode()
    # enrypt the cipher text
    encrypted_1 = f.encrypt(data_1)
    encrypted_2 = f.encrypt(data_2)

    return encrypted_1, encrypted_2

# Decrypt the data
def Depcryption(data1):
    #  defines globally
    global decrypted_1
    cryptInitial()
    # decrypt the encrypted text
    decrypted_1 = f.decrypt(str(data1))
    # print the value
    print(decrypted_1)


# main funtion
def main():
    clear()
    warn()
    input(YELLOW+'''\n\n\nPRESS ['''+WHITE+ '''ENTER'''+YELLOW+'''] TO CONTINUE''' + END )

    try:
        # progress bar
        with alive_bar(10, bar='blocks') as bar:
            # secret data for sheet
            scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']
            creds = ServiceAccountCredentials.from_json_keyfile_name('data/client_secret.json', scope)
            client = gspread.authorize(creds)
            sheet = client.open('pySheet').sheet1
            for i in range(10):       
                time.sleep(0.1)
                bar()
        
        # heading
        heading()
        
        while True:
            
            header = ('{0}root{1}> {2}'.format(YELLOW, WHITE, END))
            choise = input(header)
            
            # insert credentials
            if choise == '1':
                # getting the last row of the sheet
                list_of_all = sheet.get_all_values()
                lastRow = len(list_of_all)+1
                # taking the input form user
                print('\n {0}Enter the details like:- {1}title, username, password \n'.format(GREEN, WHITE))
                inputList = list(input().split(' '))
                # encryption
                Encryption(inputList[1], inputList[2])
                # inserting into sheet
                sheet.insert_row([inputList[0], encrypted_1, encrypted_2], lastRow)
                # show the option
                time.sleep(1)
                option()

            # access credentials [only id;s]
            if choise == '2':
                list_of_all = sheet.get_all_values()
                for value in list_of_all:
                    print(value[0])  
                # show the option
                time.sleep(1)
                option()

            # delete credentials 
            if choise == '3':
                list_of_all = sheet.get_all_values()
                for value in list_of_all:
                    print(value[0])  
                cell_id = input('\n {0}Type the {1}id {0}which you want to delete : {2}'.format(GREEN, WHITE, END))
                cell_list = sheet.findall(cell_id)
                for cell in cell_list:
                   cell_row = cell.row
                # delete that row which is selected by the user
                sheet.delete_row(cell_row)
                # show the option
                time.sleep(1)
                option()

            # visible the encrypted credential;s
            if choise == '4':
                list_of_all = sheet.get_all_values()
                for value in list_of_all:
                    print(value[0])  
                cell_id = input('\n {0}Type the {1}id {0}which you want to show : {2}'.format(GREEN, WHITE, END))
                print('')
                cell_list = sheet.findall(cell_id)
                for cell in cell_list:
                   cell_row = cell.row
                # get the data
                for i in range(1,4):
                    # print(sheet.cell(cell_row, i).value)
                    if i==1:
                        print(sheet.cell(cell_row, i).value)
                    else:
                        Depcryption(sheet.cell(cell_row, i).value)
                # to show the option
                option()

            # pySheet link
            if choise == '5': 
                #print(GREEN + '\n https://docs.google.com/spreadsheets/u/0/d/1oFjNyhuPtjUex2YTMuYY8oWm6n2o_EW3G_iw86prOqk/edit' + END)
                option()

            if choise.upper() == 'Q' or choise.upper() == 'QUIT':
                clear()
                pp()
                time.sleep(1)
                raise SystemExit
            
            # login section
            if choise == 'L' or choise.upper() == 'L':
                # username = input(GREEN + '\nUsername: ' + END)
                # password = getpass.getpass(GREEN + 'Password: ' + END)
                uname = input(GREEN+'''\n\n\n ENTER THE USERNAME ''' +YELLOW+ ''' >>> ''' +END )
                upass = getpass.getpass(GREEN+'''\n\n\n ENTER THE PASSWORD ''' +YELLOW+ ''' >>> ''' +END )
                auth(file_contents, uname, upass)
           
           # about section
            if choise ==  'A' or choise.upper() == 'A':
                heading()
                about()
                # warn()
           
            # credit section
            if choise == 'C' or choise.upper() == 'C':
                heading()
                credit()
                # warn()

            # update the script from GIT
            if choise == 'u' or choise == 'U' or choise.upper() == 'UPPER':
                os.system('python3 updater.py')
            
            # exit
            if choise.upper() == 'EXIT' or choise.upper() == 'CLOSE':
                clear()
                pp()
                time.sleep(1)
                raise SystemExit

    # Exception occurs
    except KeyboardInterrupt:
        clear()
        pp()
        time.sleep(1)
        sys.exit(0)


# i like this function 
if __name__ == "__main__":

    # RW on file
    file_contents = []
    file(file_contents)

    # execute the main()
    main()
