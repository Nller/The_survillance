import tkinter as tk

def dummy_function():
    pass

root = tk.Tk()
root.geometry("800x450")
root.title("Aplicación Tkinter")

# Añadiendo los textos descriptivos pegados a la izquierda
tk.Label(root, text="Modo:").place(relx=0.05, rely=0.06, anchor=tk.W)
tk.Label(root, text="Luces:").place(relx=0.05, rely=0.21, anchor=tk.W)
tk.Label(root, text="Frenos:").place(relx=0.05, rely=0.36, anchor=tk.W)
tk.Label(root, text="Cámaras:").place(relx=0.05, rely=0.51, anchor=tk.W)
tk.Label(root, text="GPS:").place(relx=0.05, rely=0.66, anchor=tk.W)
# Añadiendo los botones para cada fila, centrando los botones en el frame
frames = [tk.Frame(root) for _ in range(6)]

# btn_Modo1 = tk.Button(frames[0], text="Modo 1", command=dummy_function).pack(side=tk.LEFT, padx=5)
# btn_Modo2 = tk.Button(frames[0], text="Modo 2", command=dummy_function).pack(side=tk.LEFT, padx=5)
mode_buttons = [tk.Button(frames[0], text=text, width=10, height=1) for text in ["Modo 1", "Modo 2"]]
mode_labels = [tk.Label(frames[0], text="", bg="green", height=1) for _ in range(len(mode_buttons))]
mode_labels[1].config(bg = "red")

for idx, (btn, label) in enumerate(zip(mode_buttons, mode_labels)):
    btn.grid(row=0, column=idx, padx=20, pady=5, sticky="ew")
    label.grid(row=0, column=idx, padx=10, pady=5, sticky="w")

btn_Light_ON = tk.Button(frames[1], text="Activar luces", command=dummy_function, width=20, height=1).grid(row=0, column=idx, padx=10, pady=5, sticky="ew")
light_label = tk.Label(frames[1], text="", bg="green", height=1).grid(row=0, column=idx, padx=0, pady=5, sticky="w")

btn_Breaks_ON = tk.Button(frames[2], text="Activar frenos", command=dummy_function, width=20, height=1).grid(row=0, column=idx, padx=10, pady=5, sticky="ew")
break_label = tk.Label(frames[2], text="", bg="red", height=1).grid(row=0, column=idx, padx=0, pady=5, sticky="w")
# btn_CAM1 = tk.Button(frames[3], text="CAM1", command=dummy_function).pack(side=tk.LEFT, padx=5)
# btn_CAM2 = tk.Button(frames[3], text="CAM2", command=dummy_function).pack(side=tk.LEFT, padx=5)
# btn_CAM3 = tk.Button(frames[3], text="CAM3", command=dummy_function).pack(side=tk.LEFT, padx=5)

cam_buttons = [tk.Button(frames[3], text=text, width=10, height=1) for text in ["CAM1", "CAM2", "CAM3"]]
cam_labels = [tk.Label(frames[3], text="", bg="green", height=1) for _ in range(len(cam_buttons))]
cam_labels[1].config(bg = "red")
cam_labels[2].config(bg = "red")

for idx, (btn, label) in enumerate(zip(cam_buttons, cam_labels)):
    btn.grid(row=0, column=idx, padx=20, pady=5, sticky="ew")
    label.grid(row=0, column=idx, padx=10, pady=5, sticky="w")

btn_Posicion= tk.Button(frames[4], text="Posición", command=dummy_function, width=20, height=1).grid(row=0, column=idx, padx=10, pady=5, sticky="ew")
Posicion_label = tk.Label(frames[4], text="", bg="#5F9EA0", height=1).grid(row=0, column=idx, padx=0, pady=5, sticky="w")
# Centrando los frames en la pantalla y ajustando verticalmente
for i, frame in enumerate(frames[:-1]):
    frame.place(relx=0.5, rely=0.1 + 0.15 * i, anchor=tk.CENTER)

# Añadiendo separadores entre los Frames
separators = [tk.Frame(root, height=2, bd=1, bg='grey', relief=tk.SUNKEN) for _ in range(len(frames))]
for i, separator in enumerate(separators):
    separator.place(relx=0.5, rely=0.01 + 0.15 * i, anchor=tk.CENTER, relwidth=1.0)

# Botón de cierre en la parte inferior
tk.Button(frames[-1], text="Cerrar menú", command=dummy_function).pack(side=tk.LEFT)
frames[-1].place(relx=0.5, rely=0.88, anchor=tk.CENTER)

root.mainloop()
