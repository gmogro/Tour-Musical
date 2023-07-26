
class Usuario:

    def __init__(self,id,nombre,apellido,historial_eventos = None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        if historial_eventos is None:
            self.historial_eventos = []
        else:
            self.historial_eventos = historial_eventos
    
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"
    
    def to_json(self):
        return {
            "id":self.id,
            "nombre":self.nombre,
            "apellido" : self.apellido,
            "historial_eventos":self.historial_eventos
        }
        
    @classmethod
    def from_json(cls,data):
        id = data["id"]
        nombre = data["nombre"]
        apellido = data["apellido"]
        historial_eventos = data["historial_eventos"]
        return Usuario(id,nombre,apellido,historial_eventos)