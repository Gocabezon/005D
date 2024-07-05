from datos import guardar
import random


mascotas = ["spike", "cachupin", "copicopi", "terminator"]
edades = [5,3,2,6]



#arreglo
#veterinaria = [
 #   ["spike", 5],
  #  ["cachupin", 3],
   # ["copicopi", 2],
    #["terminator", 6],
#]


# Diccionario
#veterinaria = [
 #   {
  #      "nombre" : "spike"
   #     "edad": 5
  #  },
   # {
    #    "nombre" : "cachupin"
    #    "edad": 3
  #  },
   # {
    #    "nombre" : "copicopi"
     #   "edad": 2
 #   },
  #  {
   #     "nombre" : "terminator"
    #    "edad": 6
#    },
#]


#"""veterinaria = []
#for posicion,mascota in enumerate(mascotas):
#    item: [mascota, edades [posicion]]
#    veterinaria.append(item)

#for i in range (len(mascotas)):
#    item[mascotas[i], edades [i]]
#"""


#diccionario
veterinaria = []
def convertir_diccionario():
    for i in range(len(mascotas)):
        
        mascotanombre = mascotas[i]
        edadmascota = edades[i]
        item =  { 
            "nombre" : mascotanombre ,
            "edad" : edadmascota,
            'annio' : random.randrange(1995, 2023) 
            }
        veterinaria.append(item)

convertir_diccionario()

guardar("v1", veterinaria)

def masjoven():
    mascota_joven = veterinaria[0]
    for mascota in veterinaria:
        if mascota_joven['annio'] < mascota['annio']:
            mascota_joven = mascota
    return mascota_joven
    # for i in range(len(veterinaria)):
    #     if veterinaria[i]["edad"] < edadcomparar:
    #         edadcomparar = veterinaria[i]["edad"]
    #         nombremasjoven = veterinaria[i]["nombre"]
    


def masviejo():
    mascota_viejo = veterinaria[0]
    for mascota in veterinaria:
        if mascota_viejo['annio'] > mascota['annio']:
            mascota_viejo = mascota
    return mascota_viejo
    # edadcomparar = 0
    # for i in range(len(veterinaria)):
    #     if veterinaria[i]["edad"] > edadcomparar:
    #         edadcomparar = veterinaria[i]["edad"]
    #         nombremasviejo = veterinaria[i]["nombre"]
    # print(f"el mas viejo es {nombremasviejo} con {edadcomparar} años")

def sumaedades():
    edadtotal=0
    for i in range(len(veterinaria)):
        edadtotal = edadtotal + veterinaria[i]["edad"]

    print(f"La suma de las edades es de {edadtotal}")



masjoven()


masviejo()


sumaedades()
def menu():
    print("**** MENU ****")
    print("****  ****")
    print("****  ****")
    print("****  ****")


menu()