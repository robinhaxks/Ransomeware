import os

from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "rans.py" or file == "thekey.key" or file =="dec.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)        
with open("thekey.key","rb") as key:
    seckey = key.read()

for file in files:
    with open(file,"rb") as thefile:
        cont = thefile.read()
    cont_de = Fernet(seckey).decrypt(cont)
    with open(file,"wb") as thefile:
        thefile.write(cont_de)
