import hashlib
import sys
import os


def comparador (documento,documento2):
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
        return -1, None #Ficheros no abiertos

    if len(lines) == len(enlineas)+1:
        for i in range(len(enlineas)-1):
            if lines[i].decode('utf-8') != enlineas[i].decode('utf-8'):
                return -2, None
        ultima_linea2=lines[-1].decode('utf-8').split("\t")
        if len(ultima_linea2) == 3:
            if len(ultima_linea2[0]) == 8:
                try:
                    int(ultima_linea2[0],16)
                except ValueError:
                    return -2, None
            else:
                return -2, None
            if len(ultima_linea2[1]) != 2 or not ultima_linea2[1].isalpha():
                return -2, None
            if ultima_linea2[2] != "100":
                return -2, None
            if (sha2[0] == "0" and sha2[1] == "0"):
                return 0, sha2
            else:
                return -2, None
        else:
            return -2, None
    else:
        return -2, None
 
def cuentaceros (sha):
    kont=0
    for i in sha:
        if sha == '0':
            kont+=1
        else:
            break
    return (kont)
   
if len(sys.argv) == 3:
     documento = sys.argv[1]
     carpeta = sys.argv[2]
else:
     documento = input("Inserta el nombre del fichero: ")
     carpeta = input("Inserta el nombre de la carpeta: ")
 
try:
    ficheros = os.listdir(carpeta)
    
    ceros = { }
    for i in ficheros:
       path = "./" + carpeta + "/" + i
       comp, cero = comparador(documento,path)
       if comp == 0:
           ceros[path]=cuentaceros(cero)
       elif comp == -1:
           print("Error al abrir el fichero: " + path)
    
    try:
    	maximo_ceros = max(ceros.values())
    except ValueError:
    	print("La carpeta está vacia o no tiene ficheros válidos")
    	sys.exit(1)
    empatados = [k for k, v in ceros.items() if v == maximo_ceros]

    print("Ficheros que cumplen las condiciones: ")
    for i in ceros.keys(): 
        print(i)

    if len(empatados) >= 1:
        print ("\tElegido: " + empatados[0])
    else:
        print("No se ha podido elegir ningun fichero.")

except FileNotFoundError:
    print("Fichero no admitido")

except  NotADirectoryError:
    print("Carpeta no admitida")
