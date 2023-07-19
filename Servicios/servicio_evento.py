import json
from Entidades.evento import Evento

class ServicioEventos:

    def __init__(self):
        eventos = []
        try:
            with open("Persistencia/Eventos.json","r") as file:
                eventos_json = json.load(file)
                print(eventos_json)
            for data in eventos_json:
                eventos.append(Evento.from_json(data))
        except Exception as error:
            with open("Persistencia/Eventos.json","w") as file:
                json.dump(eventos, file, indent=4)
        finally:
            self.eventos = eventos

    def crearEvento(self,nombre,artista,genero,
        id_ubicacion,hora_inicio,descripcion,imagen):
        id = len(self.eventos) + 1 
        evento = Evento(id,nombre,artista,genero,
            id_ubicacion,hora_inicio,descripcion,imagen)
        self.eventos.append(evento)
    
    def eliminarEvento(self,evento):
        self.eventos.remove(evento)
    
    def buscarEvento(self,id_evento):
        for evento in self.eventos:
            if evento.id == id_evento:
                return evento
        return None
    
    def modificar(self,id_evento,nombre,artista,genero,
        id_ubicacion,hora_inicio,descripcion,imagen):
        evento = self.buscarEvento(id_evento)
        if not(evento is None):
            evento.nombre = nombre
            evento.artista = artista
            evento.genero = genero
            evento.id_ubicacion = id_ubicacion
            evento.hora_inicio = hora_inicio
            evento.descripcion = descripcion
            evento.imagen = imagen
        else:
            print("que no se encuentra el Evento")
    
    def finalizar(self):
        with open('Persistencia/Eventos.json', 'w') as f:
            eventos = []
            for evento in self.eventos:
                eventos.append(evento.to_json())
            json.dump(eventos, f, indent=4)
    
    

    

    
    



        