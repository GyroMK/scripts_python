# Nombre del archivo de entrada y salida
input_filename = 'C:\Users\sergi.carmona\Documents\scripts_python\Ai_made\ascii.py'
output_filename = 'C:\Users\sergi.carmona\Documents\scripts_python\Ai_made\ascii2.py'

# Abrir el archivo de entrada en modo lectura
with open(input_filename, 'r') as infile:
    # Leer todas las líneas del archivo
    lines = infile.readlines()

# Abrir el archivo de salida en modo escritura
with open(output_filename, 'w') as outfile:
    # Iterar sobre cada línea
    for line in lines:
        # Si la línea contiene la palabra "print", escribirla en el archivo de salida
        if 'print' in line:
            outfile.write(line)

print(f"Las líneas que contienen 'print' se han guardado en {output_filename}")