import hashlib
import os

documento = input("Inserta el nombre del documento: ")
with open (documento,"rb") as f:
    enbytes = f.read()

nombre = "".join(documento.split('.')[:-1]) + "_sha_1_digito." + documento.split('.')[-1]

if documento[0] == '.':
	nombre = '.' + nombre

sha= "1"
while sha[0] != "0":
    prefijo = os.urandom(4).hex()
    texto = enbytes.decode('utf-8') + str(prefijo) + "\31\t100"
    sha = hashlib.sha256(texto.encode('utf-8')).hexdigest()

with open (nombre,"w", newline='') as f2:
    f2.write(texto)

print("El codigo SHA-256 es: " + sha)
