import hashlib
import sys

documento = input("Inserta el nombre del primer documento: ")
documento2 = input("Inserta el nombre del segundo documento: ")
with open (documento,"rb") as f:
    enbytes = f.read()
    hash = hashlib.sha256(enbytes).hexdigest()
    
with open (documento,"rb") as f:
    enlineas = f.readlines()

segundoDoc = open(documento2,"rb")
lines = segundoDoc.readlines()

sha2 = lines[-1].decode('utf-8')

if hash == sha2 and len(lines)-1 == len(enlineas):
	for i in range(len(enlineas)):
		if lines[i].decode('utf-8') != enlineas[i].decode('utf-8'):
			print("False: contenido diferente")
			sys.exit(0)
	print("True")

else:
    print("False: SHA o num. lineas")

