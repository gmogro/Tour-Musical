class RutaVisita:

    def __init__(self,id,nombre,destinos = None):
        self.id = id
        self.nombre = nombre
        if destinos is None:
            self.destinos = []
        else:
            self.destinos = destinos
    

    def __str__(self):
        return f"{self.nombre} - {self.destinos}"
    
    def to_json(self):
        return {
            "id":self.id,
            "nombre":self.nombre,
            "destinos" : self.destinos
        }
        
    @classmethod
    def from_json(self,data):
        id = data["id"]
        nombre = data["nombre"]
        destinos = data["destinos"]
        return RutaVisita(id,nombre,destinos)