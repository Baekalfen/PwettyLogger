#
#  Created by Mads Ynddal on 08/09/14.
#  Licence: Public Domain
#  Credit me if you want to...
#

# TODO: Add file logging

import sys
import time

class colors:
    OK    = '\033[95m'
    BLUE  = '\033[94m'
    GREEN = '\033[92m'
    WARN  = '\033[93m'
    FAIL  = '\033[91m'
    END   = '\033[0m'

logWidth = 80
logWidth -= 8
postMsgWidth = 10
lineNumbers = True
preMessage = None#lambda: "\n[ %s%s%s ]\n"%(colors.GREEN,time.strftime('%X %x %Z'),colors.END)

def log(colorCode,errorCode,text,task=None):
    messages = [text[i:i+logWidth-postMsgWidth] for i in range(0, len(text), logWidth-postMsgWidth)]
    if str(type(preMessage)).find('function') != -1:
        sys.stdout.write(preMessage())
    elif preMessage:
        sys.stdout.write(preMessage)

    for i,message in enumerate(messages):
        sys.stdout.write(message.ljust(logWidth-postMsgWidth))
        if i!=len(messages)-1:
            if lineNumbers:
                addPostMessage(str(i+1),colors.GREEN)
            else:
                sys.stdout.write('\n')
    sys.stdout.flush()

    if task:
        task()
    addPostMessage(errorCode,colorCode)

def addPostMessage(postMsg,colorCode):
    postMsg = postMsg[:postMsgWidth-2]
    if len(postMsg)%2 == 1:
        postMsg+=" "
    _postMsgWidth = postMsgWidth - len(postMsg)
    pad = ' '*(_postMsgWidth/2-1)
    sys.stdout.write("[%s%s%s%s%s]\n"%(pad,colorCode,postMsg,colors.END,pad))

if __name__ == "__main__":
    log(colors.OK,'O2','kdof')
    log(colors.OK,'44OK','ksddof')
    log(colors.OK,'fs2K','kdodsfff')
    log(colors.OK,'OdK22422347y233','sdfdsfdsfsdfskdof')
    log(colors.OK,'OK333223','kdosfddsfsdfsdfsdfsdkladjeioqwjiurhj2uir ign4tuir 4sdfjisudfsdioj'*9)
    log(colors.OK,'dseesf','sdfsdfdshrttrh4543',lambda:time.sleep(1))
