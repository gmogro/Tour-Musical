class Evento:
    def __init__(self,id,nombre,artista,genero,
    id_ubicacion,hora_inicio,descripcion,imagen):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.descripcion = descripcion
        self.imagen = imagen

def __str__(self):
    return f"{self.nombre}"

def to_json(self):
    return {
        "id": self.id,
        "nombre": self.nombre
    }

@classmethod
def from_json(self,data):
    return "devolve un evento"