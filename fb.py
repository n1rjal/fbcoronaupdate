from fbchat import Client
from fbchat.models import *
from binarywritter import readpass
from getter import getdata

email,password=readpass()
client=Client(email,password)

if not client.isLoggedIn():
    client.login(email,password)

#section A GRP
grpid=3235866669820864


def sendmsg(x):
    #pubg army
    grpidp=2609050712525559
    for each in x:
        data=getdata()

        data=data[each]
        msg=""
        for key,value in data.items():
            msg=msg+key+" = "+value+"\n"

        client.send(Message(text=msg),thread_id=grpidp,thread_type=ThreadType.GROUP)

sendmsg(["usa","italy","nepal"])

client.logout()