import hashlib
import sys
import random
import time

abc = ['a','b','c','d','1','2','5','x','n','e']

def crea_string ():
	string = ''
	for i in range(random.randint(20,200)):
		string = string + abc[random.randint(0,9)]
	return string

momento=0
ciclos=0
while momento < 1000000000: #Un segundo
	string = crea_string()
	uno = time.time_ns()
	hash = hashlib.sha256(string.encode('utf-8')).hexdigest()
	dos = time.time_ns()
	momento = momento + (dos - uno)
	ciclos+=1
	if momento % 10000 == 0:
		print("Tiempo CPU: " + str(momento))

print("Número de SHAs calculados: " + str(ciclos))
