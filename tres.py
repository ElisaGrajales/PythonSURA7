#Crear un menu de dos opciones

contador=0

pueblos=[]

print("Enamorate de Antioquia")

print("***MENU***")

print("1. Agregar Pueblos")

print("2. Mostrar Rutas")

print("3. Salir")

while (contador !=3):

    pueblo={}

    contador= int(input("Digita una opción: "))

    if(contador==1):

        print("Agregando Pueblo")

        pueblo['Nombre']= input ("Ingrese el pueblo al que viajas: ")

        pueblo['Distancia']=int(input ("A que distacia se encuentra el pueblo: "))

        pueblo['Poblacion']= int(input ("Con cuanta poblacion cuenta el pueblo: "))

        pueblos.append(pueblo)

    elif(contador==2):

        print("Mostrando pueblos")

        print(pueblos)

    elif(contador==3):

        print("Saliendo ...")

        break

    else:

        print("Opcion invalida")
