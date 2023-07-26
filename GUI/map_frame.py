import tkinter
import tkintermapview
import customtkinter
from PIL import Image,ImageTk
import os
from Servicios.servicio_ubicacion import ServicioUbicacion

class MapFrame(customtkinter.CTkFrame):

    def __init__(self,root,width,height):
        super().__init__(root,width,height)
        self.load_images()
        self.grid_columnconfigure(0, weight=1)
        self.map_widget = tkintermapview.TkinterMapView(self, width=900,height=500, corner_radius=0)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.map_widget.set_position(-24.72279803947432, -65.426856820208)
        self.map_widget.set_zoom(11)
        self.load_ubicaciones()
        
    def load_images(self):
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.centro_conveciones_image = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "centroConveciones.jpg")).resize((100, 70)))
    
    def load_ubicaciones(self):
        servicio_ubicacion = ServicioUbicacion()
        ubicaciones = servicio_ubicacion.get_ubicaciones()
        for ubicacion in ubicaciones:
            self.map_widget.set_marker( ubicacion.coordenadas[0],
                                        ubicacion.coordenadas[1], 
                                        text=ubicacion.nombre,
                                        text_color="#000000"
                                      )