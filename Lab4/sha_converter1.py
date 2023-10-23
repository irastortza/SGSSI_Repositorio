import hashlib

documento = input("Inserta el nombre del documento: ")
with open (documento,"rb") as f:
    enbytes = f.read()
    hash = hashlib.sha256(enbytes).hexdigest()

print("El codigo SHA-256 es: " + hash)