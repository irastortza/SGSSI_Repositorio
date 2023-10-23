## Enuntziatua

Realizar un programa que, tomando como entrada un fichero de texto (con la forma que caracteriza a los candidatos de nuestra cadena de bloques) y un directorio que contiene ficheros de texto, obtiene como salida:
La relación de ficheros contenidos en el directorio que cumplen (con respecto al fichero de entrada) las condiciones establecidas en la Actividad 3 del Lab05. Cada fichero debe tener asociada la longitud del prefijo de 0’s de su resumen SHA-256.
El fichero, de entre los que contiene el directorio y cumplen las condiciones marcadas, cuyo resumen SHA-256 comienza por la secuencia de 0’s más larga. En caso de empate, utiliza un criterio de tu elección, para seleccionar uno de los empatados

## Konpilazioa

python3 programa_validador.py <nombre_documento_de_referencia> <nombre_carpeta>

O si no:

python3 programa_validador.py

