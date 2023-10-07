import tkinter as tk
import subprocess

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Mi Aplicación")
        self.geometry("300x200")  # Tamaño de la ventana
        
        btn1 = tk.Button(self, text="Opción 1", command=self.on_button_click)
        btn1.pack(pady=10)  # Espaciado vertical
        
        btn2 = tk.Button(self, text="Opción 2", command=self.on_button_click)
        btn2.pack(pady=10)  # Espaciado vertical
        
        exit_btn = tk.Button(self, text="Salir", command=self.on_exit)
        exit_btn.pack(pady=10)  # Espaciado vertical

    def on_button_click(self):
        pass  # No hacer nada por el momento

    def on_exit(self):
        self.destroy()  # Cierra la aplicación
        subprocess.run(['lxpanelctl', 'restart'])  # Intenta reiniciar el panel
        subprocess.run(['pcmanfm', '--desktop', '--profile', 'LXDE-pi'])  # Intenta reiniciar el gestor de archivos y el escritorio

# Crear y ejecutar la aplicación
app = App()
app.mainloop()
