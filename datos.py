import csv

def guardar (filename,datos):
        
    with open (filename + ".csv", "w", newline = "", encoding='utf-8') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(["nombre", "edad", 'annios'])
        
#arreglo
        # for d in datos:
        #     escritor_csv.writerow([d[0], d[1]])
#diccionario
        for d in datos:
            escritor_csv.writerow([d["nombre"], d["edad"], d['annio']])


# veterinaria = [
#     {"nombre" : "spike", "edad" : 5},
#     {"nombre" : "spike2", "edad" : 10},
#     {"nombre" : "spike3", "edad" : 25},
#     {"nombre" : "spike4", "edad" : 30}
# ]


# guardar("mascotas", veterinaria)