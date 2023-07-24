import customtkinter
import os
from PIL import Image
from CTkTable import *

class EventoGui(customtkinter.CTkFrame):

    def __init__(self,root,corner_radius):
        header = ["NOMBRE","ARTISTA","UBICACION","INICIO","DESCRIPCION","OPCIONES"]
        value = [header,
         [1,2,3,4,5,6],
         [1,2,3,4,5,6],
         [1,2,3,4,5,6],
         [1,2,3,4,5,6]]
        super().__init__(root,corner_radius)
        self.grid_columnconfigure(0, weight=1)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.evento_large_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "eventos.png")), size=(500, 150)) #imagen en el medio de la app
        self.evento_frame_large_image_label = customtkinter.CTkLabel(self, text="", image=self.evento_large_image)
        self.evento_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        
        self.frame_table = customtkinter.CTkFrame(self,corner_radius=0)
        self.frame_table.grid(row=1, column=0, sticky="nsew")
        self.frame_table.grid_columnconfigure(0, weight=1)

        self.frame_filter = customtkinter.CTkFrame(self.frame_table,corner_radius=0)
        self.frame_filter.grid(row=0, column=0, sticky="nsew")
        self.filter_input = customtkinter.CTkEntry(self.frame_filter,width=300,placeholder_text="Buscar")
        self.filter_input.grid(row=0,column=0,padx=10,pady=10)
        self.filter_boton = customtkinter.CTkButton(self.frame_filter,text="Buscar")
        self.filter_boton.grid(row=0,column=1,padx=10,pady=10)

        self.boton_editar = customtkinter.CTkButton(self.frame_filter,text="EDITAR",fg_color="#02b0db",hover_color="#60d3f0")
        self.boton_eliminar = customtkinter.CTkButton(self.frame_filter,text="ELIMINAR",fg_color="red",hover_color="#e84351")
        self.boton_ver = customtkinter.CTkButton(self.frame_filter,text="VER",fg_color="green",hover_color="#3bed44")
        self.boton_editar.grid(row=0,column=2,padx=10,pady=10)
        self.boton_eliminar.grid(row=0,column=3,padx=10,pady=10)
        self.boton_ver.grid(row=0,column=4,padx=10,pady=10)

        self.table = CTkTable(self.frame_table,  row=6, column=6, values=value)
        self.table.grid(row=1, column=0,padx=20, pady=20,sticky="nsew")
