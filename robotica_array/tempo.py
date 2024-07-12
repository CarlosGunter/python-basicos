def createArray():
  interations = int(10/0.01 + 1)
  array = [str(x/100) for x in range(interations)]
  print(array)

  file = open("array.txt", "w")
  file.write(', '.join(array))
  file.close()

if __name__ == '__main__':
  createArray()
  print("Arreglo creado")