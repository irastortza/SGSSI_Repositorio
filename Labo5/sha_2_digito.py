import hashlib
import os
import time

documento = input("Inserta el nombre del documento: ")
with open (documento,"rb") as f:
    enbytes = f.read()

nombre = "".join(documento.split('.')[:-1]) + "_sha_2_digito." + documento.split('.')[-1]

if documento[0] == '.':
	nombre = '.' + nombre

sha= "1"
reloj1=time.time()
reloj2=reloj1
max0=[0,"",""]
while reloj2 - reloj1 < 60:
    prefijo = os.urandom(4).hex()
    texto = enbytes.decode('utf-8') + str(prefijo) + "\31\t100"
    sha = hashlib.sha256(texto.encode('utf-8')).hexdigest()
    zeroak=0
    for i in sha:
        if i != "0":
            break
        zeroak+=1
    if zeroak > max0[0]:
        max0[0]=zeroak
        max0[1]=sha
        max0[2]=texto
        print("Número de ceros en el código: ",zeroak)
    reloj2=time.time()

with open (nombre,"w", newline='') as f2:
    f2.write(max0[2])

print("El codigo SHA-256 es: " + max0[1])
