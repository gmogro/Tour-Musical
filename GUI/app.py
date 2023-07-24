import tkinter
import tkintermapview
import customtkinter
import os
from PIL import Image,ImageTk
from GUI.ubicacion_gui import UbicacionGui
from GUI.evento_gui import EventoGui

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Tour Musical")
        self.geometry("960x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "guitarra.png")), size=(26, 26)) # logo en barra vertical
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "tituloapp.png")), size=(500, 150)) #imagen en el medio de la app
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")), #icono de la barra vertica
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.mapa_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "mapa.png")), #icono de la barra vertica
                                                 dark_image=Image.open(os.path.join(image_path, "mapa.png")), size=(20, 20))
        self.evento_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "evento.png")), #icono de la barra vertica
                                                     dark_image=Image.open(os.path.join(image_path, "evento.png")), size=(20, 20))
        self.centro_conveciones_image = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "centroConveciones.jpg")).resize((100, 70)))
        self.plane_circle_1_image = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "plane_circle_1.png")).resize((35, 35)))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Menu Musical", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20) #barra vertical

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew") #boton home

        self.ubicacion_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Ubicaciones",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.mapa_image, anchor="w", command=self.ubicacion_button_event)
        self.ubicacion_button.grid(row=2, column=0, sticky="ew") #boton frame 2

        self.evento_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Eventos",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.evento_image, anchor="w", command=self.evento_button_event)
        self.evento_button.grid(row=3, column=0, sticky="ew") #boton frame 3

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s") # swicht modo 

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        # creates frames
        self.ubicacion_frame = UbicacionGui(self,corner_radius=0)
        self.evento_frame = EventoGui(self,corner_radius=0)
        self.frame_map = customtkinter.CTkFrame(self.home_frame,width=900,height=500)
        self.frame_map.grid(row=1,column=0,padx=20,pady=20)
        # create map widget
        self.map_widget = tkintermapview.TkinterMapView(self.frame_map, width=900,height=500, corner_radius=0)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.map_widget.set_position(-24.828652046941816, -65.43439498465857)
        self.marker = self.map_widget.set_marker(-24.828652046941816, -65.43439498465857, text="Centro Conveciones", image=self.centro_conveciones_image)
        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.ubicacion_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.evento_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.ubicacion_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.ubicacion_frame.grid_forget()
        if name == "frame_3":
            self.evento_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.evento_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def ubicacion_button_event(self):
        self.select_frame_by_name("frame_2")

    def evento_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()