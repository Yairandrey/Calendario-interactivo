import tkinter as tk
from tkcalendar import Calendar

def print_time(root):
    print(f'Fecha seleccionada: {cal.selection_get()}')
    tk.Label(root, text=f'Fecha selecionada es: {cal.selection_get()}',font=('Verdana 17')).place(x=130,y=100)

root = tk.Tk()
root.config(background='#C0C0C0')
root.title("Calendario interactivo")

# Creo el calendario
cal = Calendar(root)
cal.pack(pady=25)

tk.Button(root,text="Seleccionar fecha", bg='black', fg='red',font=('Verdana 17'),command=lambda:print_time(root)).pack(pady=20)

root.mainloop()