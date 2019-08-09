#System Libs
import json
import time

#Custom Libs
import pyotp
import telepot
from telepot.loop import MessageLoop

#Config
import config
import FileWork as fw

class password():
    '''
    Your password store
    '''
    def __init__(self):
        self.password = None

    def setPass(self, pwd):
        self.password = pwd

    def getPass(self):
        return self.password

def getTime():
    time_last = int(time.strftime("%S"))
    if time_last>=30:
            time_last = time_last - 30
    time_last = 30 - time_last
    return ("(You have %s seconds left) " % str(time_last))

def NullPass():
    pwd.setPass(None)

def botSendAdmin(msg):
    '''
    Sending message to admin chat id
    '''
    bot.sendMessage(config.admin_id, msg)

def generateCodes(secure_code):
    '''
    Generate 2FA Codes
    '''
    totp = pyotp.TOTP(secure_code)
    return totp.now()

def getCodes(checkName= None):
    '''
    If checkName is None sending list of (Name of Service + 2fa code)
    Else sending only 1 item with name 'checkName' + 2fa code for this service
    '''
    if pwd.getPass() != None:
        try:
            codes = fw.OpenJson("codes", pwd.getPass() )
            for code in codes:
                if checkName==code:
                    return generateCodes( codes[code] )
                if checkName == None:
                    botSendAdmin(getTime + code +  " token is:")
                    botSendAdmin( generateCodes( codes[code] ) )
                    time.sleep(1)
        except Exception as e:
            botSendAdmin("List of 2FA doesn't exist " + str(e))
            return None
    else:
        botSendAdmin("Password Null")

def addCodes(name, secure_code):
    '''
    Add codes to codes.enc
    '''
    if pwd.getPass() != None:
        try:
            codes = fw.OpenJson("codes", pwd.getPass())
        except:
            codes = dict()
        codes[name] = secure_code 
        fw.SaveJson("codes", codes, pwd.getPass())
    else:
        botSendAdmin("Password Null")


def checkCorrectly(secure_code):
    '''
    If length secure_code > 4 and generateCodes return valid value
    '''
    try:
        if len(secure_code) > 4 and (generateCodes(secure_code) != None ) :
            return True
        else:
            return False        
    except:
        return False


def parseMsg(msg):

            command = msg.split(" ")
            if ( len(command) == 1 ):
                if command[0] == '/get':
                    getCodes()
                elif command[0] == '/null':
                    NullPass()
                    botSendAdmin("Succeful Null-ed")
                else:
                    botSendAdmin("Incorrect input")

            else:
                if command[0] == '/add':
                    if (checkCorrectly( command[2]) and (getCodes(checkName= command[1] )==None ) ):
                        addCodes(name= command[1], secure_code= command[2])
                        botSendAdmin("Successful add %s" % command[1])
                    else:
                        botSendAdmin("Incorrect 2FA format or/and this name already used")
                        
                elif command[0] == "/get":
                    code = getCodes(checkName= command [1])
                    if code != None:
                        botSendAdmin(getTime + command[1] + " token is" )
                        botSendAdmin( getCodes(checkName= command [1]) )
                    else:
                        botSendAdmin("There is no service with this name.")

                elif command[0] == '/del':                   
                    botSendAdmin("This function now unviable.")

                elif command[0] == '/pass':
                    pwd.setPass(command[1])
                    botSendAdmin("Succeful!")
                    


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print("Chat id: %s" % str(chat_id) )
    if chat_id == config.admin_id:
        parseMsg(msg['text'])

pwd = password()
isNotConn = True
while isNotConn:
    try:
        bot = telepot.Bot(config.token)
        MessageLoop(bot, handle).run_as_thread()
        isNotConn = False
    except Exception as e:
        print(str(e))
        time.sleep(10)
        isNotConn = True

while 1:
    time.sleep(10)
