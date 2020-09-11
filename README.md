# PassManager-pyScript

Copyright 2020 PassManager
Written by: * **Abhishek Patel** - (https://github.com/abhishekpatel946/PassManager-pyScript)

TOOL DESIGNED TO SAVE ALL YOUR PASSWORDS & CREDENTIALS SECURELY USIGN CRYPTOGRAPHY.

**Only download it here. Not available on other platforms. It's a open source you can download the code and modify at your side. .**

### Cloning:
```
git clone https://github.com/abhishekpatel946/PassManager-pyScript.git
```

### Running:
```
cd PassManager
```

```
sudo python3 install.py
```

```
sudo python3 PassManager.py
```

## Features 

- Save Passwords.
- Saves the encrypted form. 
- Google Sheet is used for store pass.
- You can access anywhere you want.
- Securly login by the user into the script

### Prerequisites

* python3
* pip
* cryptography.fernet
* gspread
* oauth2client

### Install requirements

* pip install cryptography
* pip install gspread
* pip install oauth2client

### Tested on:

+ Kali Linux - ROLLING

### Screenshot:
![Shot](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/Option-Login.png)

More in [Screens](Screens)



### Configure the PassManager and google-api;s

> **NOTE** 
> Please make sure you follow all the naming convension regarding the project_name, sheet_name, json_key_name and all the mention in the instructions.
> If you do something change here and then make sure you can also change into the script.

* Goto the [Google Sheet](https://docs.google.com/spreadsheets/u/0/) using this link and create a new sheet as same as below.


* Rename the sheet name as
```
**pySheet**
```
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture1.png)


* Goto the [Google_Console](https://console.developers.google.com/) and create a new project.
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture2.png)


* Click the hamburger **menu** -> **API;s & Services** -> **Library**.
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture3.png)


* Click the **Enable API;s and Services**.
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture4.png)


* Search **Google Drive API**.
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture5.png)


* and **Enable** the API.
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture6.png)


* Search **Google Sheet API**.
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture7.png)


* and **Enable** the API.
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture8.png)


* Click the **Manage** and redirected to this page.
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture9.png)


> **NOTE** 
> You're in the Google Sheet API.


* Click on **Credentials** -> **Create Credentials** -> **Service Account**.
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture10.png)


* Create a Service Account name as
```
PassManager-admin
```
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture11.png)


* **Role** -> **Project** -> **Editor**
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture12.png)


* Just leave as it is **Empty** and DONE!!!
> **NOTE**
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Pictur13.png)


* Click on **Service Account** -> **select Account** -> **select Three Vertical dot icon** -> **Create Key**.
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture14.png)


* Make sure you select the **JSON** and download the _PassManager-admin.json_ file.
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture15.png) 


* Download...
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture16.png)


* Save into the _dir_ **PassManager-pyScript/data/**


* Goto the **Google Sheet** and some change here...
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture17.png)


* First _RENAME_ the sheet as **pySheet**.
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture17.png)


* and _WRITE_ **TITLE, USERNAME, PASSWORD**.
> **NOTE** just add a row for heading.
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture18.png)


* Now, Open the **JSON** private key on any text editor and _COPY_ the **client_mail :** 
> **NOTE** Copied the client_mail only!
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture19.png)


* and _PASTE_ it here copied text into **Share** and sheet will be share your Service Account.
(https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture20.png)


* Now, open termianl run these commands
```
sudo python3 install.py
```
```
sudo python3 PassManager.py
```


### Contribute:
Send me more features if you want it :D

**I need your Help to become it to better.**


### License
**GNU General Public License v3.0**

### Contact:
**abhishekpatel946@gmail.com**

