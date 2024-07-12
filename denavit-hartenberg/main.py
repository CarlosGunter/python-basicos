# Cinematica directa a travaz del metodo de Denavit-Hartenberg
import numpy as np

def DH(theta, d, a, alpha):
    # Almacena las matrices de transformacion homogenea por cada articulacion
    tn = np.array([])
    # Matriz de transformacion homogenea
    t = np.eye(4)
    # Conversion de grados a radianes
    theta = np.radians(theta)
    alpha = np.radians(alpha)
    # Loop para determinar la matriz de transformacion homogenea
    for i in range(0, len(theta)):
        # Matriz de transformacion homogenea
        ti = np.array([
            [
                np.cos(theta[i]),
                -np.sin(theta[i])*np.cos(alpha[i]),
                np.sin(theta[i])*np.sin(alpha[i]),
                a[i]*np.cos(theta[i])
            ],
            [
                np.sin(theta[i]),
                np.cos(theta[i])*np.cos(alpha[i]),
                -np.cos(theta[i])*np.sin(alpha[i]),
                a[i]*np.sin(theta[i])
            ],
            [0, np.sin(alpha[i]), np.cos(alpha[i]), d[i]],
            [0, 0, 0, 1]
        ])
        tn = np.append(tn, [ti])
        t = np.dot(t, ti)
    
    return t

def main():
    # Ingreso de datos
    n = input("Ingrese el numero de articulaciones: ")
    if not n.isdigit() or int(n) < 1:
        print("ERROR: Valor invalido, intente de nuevo.")
        main()
        return

    n = int(n)
    theta = np.zeros(n)
    d = np.zeros(n)
    a = np.zeros(n)
    alpha = np.zeros(n)

    i = 0
    while i < int(n):
        print(f'\nT [{i+1} - {i+2}]:')
        try:
            theta[i] = float(input(f"* Theta {i+1}: "))
            d[i] = float(input(f"* d{i+1}: "))
            a[i] = float(input(f"* a{i+1}: "))
            alpha[i] = float(input(f"* Alpha {i+1}: "))
            i += 1
        except ValueError:
            i -= i
            print("ERROR: Valor invalido, intente de nuevo.")

    t = DH(theta, d, a, alpha)
    print("\nMatriz de transformacion homogenea:")
    print(t)

if __name__ == "__main__":
    main()
    input("\n")