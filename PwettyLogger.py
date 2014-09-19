#
#  Created by Mads Ynddal on 08/09/14.
#  GitHub: https://github.com/Baekalfen/PwettyLogger.git
#  Licence: Public Domain
#  Credit me if you want to...
#

import sys
import time
import atexit

class colors:
    OK    = '\033[95m'
    BLUE  = '\033[94m'
    GREEN = '\033[92m'
    WARN  = '\033[93m'
    FAIL  = '\033[91m'
    END   = '\033[0m'

logWidth = 80
statusMsgWidth = 10
lineNumbers = True
preMessage = None#lambda: "\n[ %s%s%s ]\n"%(colors.GREEN,time.strftime('%X %x %Z'),colors.END)
postMessage = None#lambda: time.strftime('%X %x')
logFile = None#"log.txt"

logWidth -= 1+len(postMessage()+' ' if postMessage else '')
if logFile:
    f = open(logFile, 'a')

def log(colorCode,errorCode,text,task=None):
    messages = [text[i:i+logWidth-statusMsgWidth] for i in range(0, len(text), logWidth-statusMsgWidth)]
    if str(type(preMessage)).find('function') != -1:
        write(preMessage())
    elif preMessage:
        write(preMessage)

    for i,message in enumerate(messages):
        write(message.ljust(logWidth-statusMsgWidth))
        if i!=len(messages)-1:
            if lineNumbers:
                addPostMessage(str(i+1),colors.GREEN)
            else:
                write('\n')

    if task:
        task()
    addPostMessage(errorCode,colorCode)

def addPostMessage(postMsg,colorCode):
    postMsg = postMsg[:statusMsgWidth-2]
    if len(postMsg)%2 == 1:
        postMsg+=" "
    _statusMsgWidth = statusMsgWidth - len(postMsg)
    pad = ' '*(_statusMsgWidth/2-1)
    write(" [%s%s%s%s%s]"%(pad,colorCode,postMsg,colors.END,pad))
    if postMessage:
        write(' %s'%postMessage())
    write('\n')

def write(text):
    sys.stdout.write(text)
    sys.stdout.flush()
    if logFile:
        f.write(text)

def closeFile():
    f.close()

if logFile:
    atexit.register(closeFile)

if __name__ == "__main__":
    log(colors.OK,'O2','kdof')
    log(colors.OK,'44OK','ksddof')
    log(colors.OK,'fs2K','kdodsfff',lambda:time.sleep(1))
    log(colors.OK,'OdK22422347y233','sdfdsfdsfsdfskdof')
    log(colors.OK,'OK333223','kdosfddsfsdfsdfsdfsdkladjeioqwjiurhj2uir ign4tuir 4sdfjisudfsdioj'*9)
    log(colors.OK,'dseesf','sdfsdfdshrttrh4543',lambda:time.sleep(1))
