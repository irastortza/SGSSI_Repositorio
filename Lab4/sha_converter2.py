import hashlib

documento = input("Inserta el nombre del documento: ")
with open (documento,"rb") as f:
    enbytes = f.read()
    hash = hashlib.sha256(enbytes).hexdigest()

nombre = "".join(documento.split('.')[:-1]) + "_con_el_sha." + documento.split('.')[-1]

if documento[0] == '.':
	nombre = '.' + nombre

with open (nombre,"w", newline='') as f2:
    f2.write(str(enbytes.decode('utf-8') + hash))

print("El codigo SHA-256 es: " + hash)
