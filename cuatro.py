#Crear menú empanadas
contador=0
empanadas=[]
print("1. Agregar empanadas")
print("2. Mostrar empanadas")
print("3. Salir")

while(contador !=3):
    empanada={}
    ingredientes=[]
    contador=int((input("Digite la opción: ")))
    if (contador==1):
        empanada['Nombre']=input("Ingrese el nombre")
        for k in range (3):
            ingredientes.append(input(f"Digite el ingrediente: {k+1}"))
        empanada['Ingredientes']=ingredientes
        empanada['Precio']=int(input("Digite el precio: "))
        empanadas.append(empanada)
        print ("agregando empanada")
    elif (contador==2):
        print("Mostrando empanadas")
        print(empanadas)
    elif(contador==3):
        print("Saliendo ...")
        break
    else:
        print("Opción inválida")