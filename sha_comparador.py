import hashlib
import sys

if len(sys.argv) == 3:
	documento = sys.argv[1]
	documento2 = sys.argv[2]
else:
	documento = input("Inserta el nombre del primer documento: ")
	documento2 = input("Inserta el nombre del segundo documento: ")

try:
	with open (documento,"rb") as f:
		enlineas = f.readlines()
	with open(documento2,"rb") as f:
		enbytes = f.read()
		sha2 = hashlib.sha256(enbytes).hexdigest()
	
	segundoDoc = open(documento2,"rb")
	lines = segundoDoc.readlines()
	segundoDoc.close()
except:
	print("ERROR: no ha sido posible abrir los ficheros. ")

if len(lines) == len(enlineas)+1:
	for i in range(len(enlineas)-1):
		if lines[i].decode('utf-8') != enlineas[i].decode('utf-8'):
			print("False: contenido diferente")
			sys.exit(0)
	ultima_linea2=lines[-1].decode('utf-8').split("\t")
	if len(ultima_linea2) == 3:
		if len(ultima_linea2[0]) == 8:
			try:
				int(ultima_linea2[0],16)
			except ValueError:
				print("False: prefijo incorrecto")
				sys.exit(0)
		else:
			print("False: prefijo de tamaño diferente")
			sys.exit(0)
		if len(ultima_linea2[1]) != 4 or not ultima_linea2[1].isalpha():
			print("False: identificador incorrecto")
			sys.exit(0)
		if ultima_linea2[2] != "100":
			print("False: secuencia 100 incorrecta")
			sys.exit(0)
		if (sha2[0] == "0" and sha2[1] == "0"):
			print("True")
		else:
			print("False: no tiene secuencia de ceros en el SHA",sha2)
	else:
		print("False: última linea diferente")
		sys.exit(0)
else:
    print("False: estructura diferente")