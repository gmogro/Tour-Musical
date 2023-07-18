import json
from Entidades.evento import Evento

class ServicioEventos:

    def __init__(self):
        eventos = []
        with open("Persistencia/Evento.json","r") as file:
            eventos_json = json.load(file)
            print(eventos_json)
            
        for data in eventos_json:
            eventos.append(Ubicacion.from_json(data))
        self.eventos = eventos

    

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
    
    

    

    
    



        