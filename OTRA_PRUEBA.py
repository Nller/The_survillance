import tkinter as tk
from tkinter import ttk, filedialog
import cv2
import numpy as np
from PIL import Image, ImageTk
import subprocess

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #Se abre la aplicacion
        #self.title("Aplicación")
        self.overrideredirect(1)  # Elimina la barra de título
        self.geometry("850x480")


        ##########################PARA EL VIDEO#######################
        # Frame del video
        self.Inicio_frame = ttk.Frame(self)
        self.Inicio_frame.pack(fill="both", expand=True)

        # Entrada para la ruta del video
        self.vid_path = tk.StringVar()
        
        # Canvas para el video
        self.canvas = tk.Canvas(self.Inicio_frame, width=850)
        self.canvas.pack(fill="both", expand=True, anchor = 'center')
        ##############################################################
        
        ##########################PARA EL MENU########################
        self.menu_button = tk.Button(self.Inicio_frame, text="Volver", command=self.show_menu,width=10)
        self.menu_button.pack(pady=20)
        tk.Label(self.Inicio_frame, text="Latitud = 37.82 °").place(relx=0.05, rely=0.88, anchor=tk.W)
        tk.Label(self.Inicio_frame, text="Longitud = 141.36 °").place(relx=0.05, rely=0.92, anchor=tk.W)
        tk.Label(self.Inicio_frame, text="Altitud = 1201.5 m").place(relx=0.05, rely=0.96, anchor=tk.W)

        tk.Label(self.Inicio_frame, text="Velocidad = 134.21 km/h").place(relx=0.80, rely=0.88, anchor=tk.W)
        tk.Label(self.Inicio_frame, text="Dirección = 271.83 °").place(relx=0.80, rely=0.92, anchor=tk.W)

        #self.exit_button = tk.Button(self.Inicio_frame, text="Salir", command=self.on_exit)
        #self.exit_button.pack(pady=10)  # Espaciado vertical

        self.select_video()
        self.update_video()

        ################################# Pestaña de menú ######################################
        self.menu_frame = ttk.Frame(self)
        self.menu_frame.pack(anchor='n', expand=True)
        self.menu_frame.pack_forget()

        self.button_frame = ttk.Frame(self.menu_frame)
        self.button_frame.pack(expand=True, anchor='n')  # Alinea el button_frame a la parte superior

        self.mode_buttons = [tk.Button(self.button_frame, text=text) for text in ["Modo 1", "Modo 2"]]
        self.mode_labels = [tk.Label(self.button_frame, text="", bg="green") for _ in range(len(self.mode_buttons))]
        for idx, (btn, label) in enumerate(zip(self.mode_buttons, self.mode_labels)):
            btn.grid(row=0, column=idx, padx=5, pady=5, sticky="ew")
            label.grid(row=0, column=idx, padx=0, pady=5, sticky="w")

        self.separator1 = ttk.Separator(self.button_frame, orient='horizontal')
        self.separator1.grid(row=1, columnspan=len(self.mode_buttons), sticky='ew', pady=5)  # Ajusta columnspan y sticky

        self.lights_button = ttk.Button(self.button_frame, text="Activar Luces", command=self.toggle_lights)
        self.lights_button.grid(row=2, columnspan=len(self.mode_buttons), padx=5, pady=5, sticky="ew")
        self.lights_label = tk.Label(self.button_frame, text="", bg="green")
        self.lights_label.grid(row=2, column=len(self.mode_buttons), padx=5, pady=5, sticky="w")

        self.separator2 = ttk.Separator(self.button_frame, orient='horizontal')
        self.separator2.grid(row=3, columnspan=len(self.mode_buttons), sticky='ew', pady=5)  # Ajusta columnspan y sticky

        self.brakes_button = tk.Button(self.button_frame, text="Activar Frenos", command=self.toggle_brakes)
        self.brakes_button.grid(row=4, columnspan=len(self.mode_buttons), padx=5, pady=5, sticky="ew")
        self.brakes_label = tk.Label(self.button_frame, text="", bg="green")
        self.brakes_label.grid(row=4, column=len(self.mode_buttons), padx=5, pady=5, sticky="w")

        self.separator3 = ttk.Separator(self.button_frame, orient='horizontal')
        self.separator3.grid(row=5, columnspan=len(self.mode_buttons), sticky='ew', pady=5)  # Ajusta columnspan y sticky

        self.cam_buttons = [tk.Button(self.button_frame, text=text) for text in ["CAM1", "CAM2", "CAM3"]]
        self.cam_labels = [tk.Label(self.button_frame, text="", bg="green") for _ in range(len(self.cam_buttons))]
        
        for idx, (btn, label) in enumerate(zip(self.cam_buttons, self.cam_labels)):
            btn.grid(row=6, column=idx, padx=5, pady=5, sticky="ew")
            label.grid(row=6, column=idx, padx=5, pady=5, sticky="w")




        self.close_menu_button = tk.Button(self.button_frame, text="Cerrar Menú", command=self.close_menu)
        self.close_menu_button.grid(row=7, column=0, pady=20)


    #######################################################################################
    ################################ METODOS AUXILIARES####################################
    #######################################################################################
    def select_mode(self, mode):
        print(f'Se ha seleccionado {mode}')

    def select_video(self):
        file_path = "video_1.mp4"
        if file_path:
            self.vid_path.set(file_path)
            self.vid = cv2.VideoCapture(file_path)
            self.update_video()

    def update_video(self):
        ret, frame = self.vid.read()
        if not ret:
            self.image = ImageTk.PhotoImage(Image.open("mapa_gps.png").resize((850, 480)))
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
            return
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        self.photo = ImageTk.PhotoImage(image=image)
        
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.after(10, self.update_video)

    def show_menu(self):
        self.menu_frame.pack(fill="both", expand=True)
        self.Inicio_frame.pack_forget()
        self.geometry("850x480")

    def close_menu(self):
        self.Inicio_frame.pack(fill="both", expand=True)
        self.menu_frame.pack_forget()
    
    def toggle_lights(self):
        self.lights_button.configure(bg="green")
        self.lights_label.configure(bg="green")

    def toggle_brakes(self):
        if self.brakes_button.cget("style") == "TButton":
            self.brakes_button.config(style="TButton", background="green")
            self.brakes_label.configure(bg="green")
        else:
            self.brakes_button.config(style="TButton")
            self.brakes_label.configure(bg="")
    
    def on_exit(self):
            self.destroy()  # Cierra la aplicación
            subprocess.run(['lxpanelctl', 'restart'])  # Intenta reiniciar el panel
            subprocess.run(['pcmanfm', '--desktop', '--profile', 'LXDE-pi'])  # Intenta reiniciar el gestor de archivos y el escritorio

if __name__ == "__main__":
    app = App()
    app.mainloop()

