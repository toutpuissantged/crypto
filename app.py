from cryptography.fernet import Fernet

def fileopen(dir,mode,data=b''):
    read_mode=['rb','r','r+','rb+']
    write_mode=['wb','w','wb+','w+']
    fo=open(dir,mode)
    if mode in read_mode : data=fo.read()
    elif mode in write_mode: fo.write(data)
    fo.close()
    return data

def keysave(mode,data=b''):
    mode_list=['r','w']
    open_mode=mode+'b+'
    if mode in mode_list: pass
    else: return 0
    reponse=fileopen('key.txt',open_mode,data)
    return reponse

def encrypt(file):
    key = Fernet.generate_key()
    data=fileopen(file,'rb')
    keysave('w',key)
    f = Fernet(key)
    token = f.encrypt(data)
    fileopen(file,'wb',token)
    return 0

def decrypt(file):
    data=fileopen(file,'rb')
    key=keysave('r')
    f = Fernet(key)
    token = f.decrypt(data)
    fileopen(file,'wb',token)
    return 0

encrypt('mydata')
#decrypt('mydata')
print("finish")