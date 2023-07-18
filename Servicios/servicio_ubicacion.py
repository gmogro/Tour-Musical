import json
from Entidades.ubicacion import Ubicacion

class ServicioUbicacion:

    def __init__(self):
        ubicaciones = []
        with open("Persistencia/Ubicacion.json","r") as file:
            ubicaciones_json = json.load(file)
            print(ubicaciones_json)
            
        for data in ubicaciones_json:
            ubicaciones.append(Ubicacion.from_json(data))
        self.ubicaciones = ubicaciones

    

    #CRUD ABM
    def crearUbicacion(self):
        id = len(self.ubicaciones) + 1 
        nombre = input("Ingrese el nombre : ")
        direccion = input("Ingrese la direccion : ")
        coordenadas = []
        for i in range(2):
            coordenadas.append(input("Ingrese la coordenada : "))
        ubicacion = Ubicacion(id,nombre,direccion,coordenadas)
        self.ubicaciones.append(ubicacion)
    
    def eliminarUbicacion(self,ubicacion):
        self.ubicaciones.remove(ubicacion)
    
    def buscarUbicacion(self,id_ubicacion):
        for ubicacion in self.ubicaciones:
            if ubicacion.id == id_ubicacion:
                return ubicacion
        return None
    
    def modificar(self,id_ubicacion):
        ubicacion = self.buscarUbicacion(id_ubicacion)
        if not(ubicacion is None):
            nombre = input("Ingrese el nombre : ")
            direccion = input("Ingrese la direccion : ")
            coordenadas = []
            for i in range(2):
                coordenadas.append(input("Ingrese la coordenada : "))
            ubicacion.nombre = nombre
            ubicacion.direccion = direccion
            ubicacion.coordenadas = coordenadas
        else:
            print("que no se encuentra la Ubicacion")
    
    def finalizar(self):
        with open('Persistencia/Ubicacion.json', 'w') as f:
            lista = []
            for ubicacion in self.ubicaciones:
                lista.append(ubicacion.to_json())
            json.dump(lista, f, indent=4)


    

    
    



        