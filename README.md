# 2FA-Telegram
## What is it?
This simple telegram bot written in Python will help you access the 2FA codes.
All your keys for generating 2FA are stored in an encrypted file (used Fernet symmetric encryption.
## Setup
#### 1. Dependencies
Firstly you need to install dependencies ([telepot](https://github.com/nickoala/telepot), [pyotp](https://github.com/pyauth/pyotp),  [cryptography](https://github.com/pyca/cryptography)) using:

    pip3 install -r requirements.txt

#### 2. Registration
Send a message [BotFather](https://telegram.me/botfather) and register a bot. I recommend using the bot's name as random as possible 
>for example: mhdpjuh7wgdhumy9z2_bot

#### 3. Config file
Now you need to create a file **`config.py`** like this:

    token = "1234567:XXXXXXXXXXXXX"

Run the bot and write him any message. A message will appear in the console like this: `"Chat id: 98765432"`. 
Now place this id to the config file. As a result, the file should look like this:

    token = "1234567:XXXXXXXXXXXXX"
    admin_id = 98765432

## Usage
#### 1. /pass
**/pass** - This command sets a password to the repository.

Using like 
> /pass 1a2b3c4d5e6

I recommend resetting the password variable after using the bot:
> /pass null

You need to re-enter the password for the next use after this command.
It's help you to secure store your 2FA-keys.

**Attention! Every time before use `/add` and `/get` you need send password from key-store to bot**

#### 2. /add
**/add** - This command add service to the repository.
> /add [service_name] [key]

For example:
> /add PyOTP_Test JBSWY3DPEHPK3PXP

#### 3. /get
**/get** - This command return 2FA-code to the repository.
> /get [service_name]

`/get`  without args return full list of service_name + 2FA-code 

Example:
> /get PyOTP_Test

#### 4. Delete or change password
For security reasons, you can not remove the service through the bot (this is a feature). To delete (or receive data without telegram bot, or change local key-store password) use `CodesEditor.py` local.

>python3 `CodesEditor.py`

## Thanks
I want to thank the developers of these beautiful libraries:
[telepot](https://github.com/nickoala/telepot), [pyotp](https://github.com/pyauth/pyotp),  [cryptography](https://github.com/pyca/cryptography).
