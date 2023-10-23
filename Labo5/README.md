## Programas creadoras de códigos SHA

El programa sha_1_digito.py crea códigos SHA para cualquier fichero de que empiecen con un 0. 

El programa sha_2_digito.py hace lo mismo pero garantiza que los códgios tengan al menos dos ceros seguidos. 

## Comparador de ficheros

El programa verifica que los ficheros tienen la misma estructa y que el segundo fichero cumple una serie de condiciones. Enunciado:

Realizar un programa que, tomando como entrada dos ficheros de texto, obtenga como salida el resultado de comprobar estas dos condiciones: El segundo de los dos ficheros de texto de entrada comienza exactamente por los mismos contenidos que el primero, seguido por una línea con las características especificadas para las actividades anteriores. El resumen SHA-256 del segundo fichero en versión hex: tiene como prefijo una secuencia de 0’s Probar el funcionamiento tomando como entrada el fichero SGSSI-23.CB.02.txt.y el resultante de la prueba realizada en la actividad 2.

## Ejecucción:

Todos los programas se ejecutan de la siguiente manera: 

python3 <nombre_programa>

En el caso del tercer programa, puede recibir los parametros de la línea de comandos:

python3 sha_comparador.py <documento_modelo> <documento_2>
