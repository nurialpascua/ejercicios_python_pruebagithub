f1 = open("diario1.txt", "r")
print (f1.read())
f1.close
with open("diario1.txt", "a") as f:
    f.write("Este es el texto que se añadirá al final del archivo.\n")
print(f1.read())