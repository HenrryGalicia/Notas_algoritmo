def calcular_promedio(notas):
    # Convertir las notas a enteros y calcular el promedio
    notas_int = [int(nota) for nota in notas]
    promedio = sum(notas_int) / len(notas_int)
    return promedio

def guardar_promedios_en_archivo(entrada, archivo_salida):
    alumnos = entrada.split('|')
    promedios = {}

    for alumno in alumnos:
        datos_alumno = alumno.split(',')
        nombre = datos_alumno[0]
        notas = datos_alumno[1:]

        promedio = calcular_promedio(notas)
        promedios[nombre] = promedio

    # Guardar los promedios en el archivo de salida
    with open(archivo_salida, 'w') as archivo:
        for nombre, promedio in promedios.items():
            archivo.write(f"{nombre}={promedio}\n")

if __name__ == "__main__":
    entrada = "Juan,98,87,89,90|Jose,90,43,20,40|Pedro,70,80,89,90"
    archivo_salida = "promedios.txt"

    guardar_promedios_en_archivo(entrada, archivo_salida)
    print("Promedios guardados en el archivo:", archivo_salida)
