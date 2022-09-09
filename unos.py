#Variable con elementos del mismo tipo
#Array
##Usar nombres largos para las variables 
#
numerospares=[]
#Generar un ciclo while que de diez vueltas para 
#variable centinela o contador
i=0
while(i<10):
    numero=(int(input("Digite un número par: ")))
    if(numero%2==0):
#Propiedad append para las listas
        numerospares.append(numero)
        i=i+1

for k in numerospares: 
    print(k)