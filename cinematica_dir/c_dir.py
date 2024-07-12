# Tarea 3. Robotica
# Programar las ecuaciones de cinemática directa de posición del robot planar
# de 2GDL de transformación que el usuario ingrese de los eslabones y el valor
# de los ángulos de articulacion para obtener la posición (x,y) del EF

import math

def calcX(eslabon1, angulo1, eslabon2, angulo2):
    x1 = eslabon1 * math.cos(math.radians(angulo1))
    x2 = eslabon2 * math.cos(math.radians(angulo1 + angulo2))
    return x1, x2, x1 + x2

def calcY(eslabon1, angulo1, eslabon2, angulo2):
    y1 = eslabon1 * math.sin(math.radians(angulo1))
    y2 = eslabon2 * math.sin(math.radians(angulo1 + angulo2))
    return y1, y2, y1 + y2

if __name__ == '__main__':
    eslabon1 = float(input("Longitud del primer eslabón: "))
    angulo1 = float(input("Valor del primer ángulo en grados: "))
    eslabon2 = float(input("Longitud del segundo eslabón: "))
    angulo2 = float(input("Valor del segundo ángulo en grados: "))
    x1, x2, x = calcX(eslabon1, angulo1, eslabon2, angulo2)
    y1, y2, y = calcY(eslabon1, angulo1, eslabon2, angulo2)
    print(f"x' = {x1:.2f}, x'' = {x2:.2f}")
    print(f"x' + x'' = {x:.2f}")
    print(f"y' = {y1:.2f}, y'' = {y2:.2f}")
    print(f"y' + y'' = {y:.2f}")
    print(f"La posición del extremo final del robot es: ({x:.2f}, {y:.2f})")
    input("Presiona Enter para continuar...")
