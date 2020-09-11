# PassManager-pyScript

Copyright 2020 PassManager
Written by: **Abhishek Patel** - (https://github.com/abhishekpatel946/PassManager-pyScript)

>
> TOOL DESIGNED TO SAVE ALL YOUR PASSWORDS & CREDENTIALS > SECURELY USING CRYPTOGRAPHY.
>

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
<br>
<br>

* Goto the [Google Sheet](https://docs.google.com/spreadsheets/u/0/) using this link and create a new sheet as same as below.
<br>
<br>

* Rename the sheet name as _pySheet_

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture1.png)
<br>
<br>

* Goto the [Google_Console](https://console.developers.google.com/) and create a new project.

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture2.png)
<br>
<br>

* Click the hamburger **menu** -> **API;s & Services** -> **Library**.

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture3.png)
<br>
<br>

* Click the **Enable API;s and Services**.

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture4.png)
<br>
<br>

* Search **Google Drive API**.

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture5.png)
<br>
<br>

* and **Enable** the API.

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture6.png)
<br>
<br>

* Search **Google Sheet API** and **Enable** the API.

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture7.png)
<br>
<br>

* Click the **Manage** and redirected to this page.

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture8.png)
<br>

> **NOTE** 
> You're in the Google Sheet API.
<br>
<br>

* Click on **Credentials** -> **Create Credentials** -> **Service Account**.

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture9.png)
<br>
<br>

* Create a Service Account name as _PassManager-admin_

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture10.png)
<br>
<br>

* **Role** -> **Project** -> **Editor**

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture11.png)
<br>
<br>

> **NOTE**
> Just leave as it is **Empty** and DONE!!!

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture12.png)
<br>
<br>

* Click on **Service Account** -> **select Account** -> **select Three Vertical dot icon** -> **Create Key**.

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture13.png)
<br>
<br>

* Make sure you select the **JSON** and download the _PassManager-admin.json_ file.

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture14.png) 
<br>
<br>

* Download...

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture15.png)
<br>
<br>

* Save into the _dir_ **PassManager-pyScript/data/**
<br>
<br>

* Goto the **Google Sheet** and some change here...

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture16.png)
<br>
<br>

* First _RENAME_ the sheet as **pySheet**.

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture17.png)
<br>
<br>

* and _WRITE_ **TITLE, USERNAME, PASSWORD**.
> **NOTE** just add a row for heading.

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture18.png)
<br>
<br>

* Now, Open the **JSON** private key on any text editor and _COPY_ the **client_mail :** 
> **NOTE** Copied the client_mail only!

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture19.png)
<br>
<br>

* and _PASTE_ it here copied text into **Share** and sheet will be share your Service Account.

![Img](https://github.com/abhishekpatel946/PassManager-pyScript/blob/master/Screens/instructions_img/Picture20.png)
<br>
<br>

* Now, open terminal run these commands
```
sudo python3 install.py
```
```
sudo python3 PassManager.py
```
<br>
<br>

### Contribute:
Send me more features if you want it :D

**I need your Help to become it to better.**


### License
**GNU General Public License v3.0**

### Contact:
**abhishekpatel946@gmail.com**
