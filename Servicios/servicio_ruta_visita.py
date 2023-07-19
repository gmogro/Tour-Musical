import json
from Entidades.ruta_visita import RutaVisita

class ServicioRutaVisita:

    def __init__(self):
        rutas = []
        try:
            with open("Persistencia/RutaVisita.json","r") as file:
                rutas_json = json.load(file)
            for data in rutas_json:
                rutas.append(RutaVisita.from_json(data))
        except Exception as error:
            with open("Persistencia/RutaVisita.json","w") as file:
                json.dump(rutas, file, indent=4)
        finally:
            self.rutas = rutas

    def crearRutaVisita(self,id,nombre,destinos = None):
        id = len(self.rutas) + 1 
        ruta = RutaVisita(id,nombre,destinos)
        self.rutas.append(ruta)
    
    def eliminarRutaVisita(self,ruta):
        self.rutas.remove(ruta)
    
    def buscarRutaVisita(self,id_ruta):
        for ruta in self.rutas:
            if ruta.id == id_ruta:
                return ruta
        return None
    
    def modificar(self,id_ruta,nombre,destinos = None):
        ruta = self.buscarRutaVisita(id_ruta)
        if not(ruta is None):
            ruta.nombre = nombre
            ruta.destinos = destinos
        else:
            print("que no se encuentra la Ruta")
    
    def finalizar(self):
        with open('Persistencia/RutaVisita.json', 'w') as f:
            rutas = []
            for ruta in self.rutas:
                rutas.append(ruta.to_json())
            json.dump(rutas, f, indent=4)
