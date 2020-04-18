import codecs
def readpass():
    filee=open("filee.txt","rb").read()

    email=codecs.decode(filee,'hex')
    email=email.decode('utf-8')
    
    filee=open("filep.txt","rb").read()

    password=codecs.decode(filee,'hex')
    password=password.decode('utf-8')
    
    return (email,password)