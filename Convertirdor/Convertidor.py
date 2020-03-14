# Required libraries

import os
import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# window settings

root = Tk()
root.title('Conversor de archivos de importación.')
root.config(width="380", height="320")
#root.resizable(False,False)

# Frame settings

#File selection
def open():
    root.filename =  filedialog.askopenfilename(initialdir = "/Escritorio",title = "Seleccione el archivo", filetypes = (("Archivos xlsx","*.xlsx"),("Todos los archivos","*.*")))
    # Get the path of the file

    path = os.path.abspath(root.filename)
    directory, file = os.path.split(path)

    # set the working directory using the path of the file

    os.chdir(directory)

    # File convertion

    df = pd.read_excel(root.filename) # File reading

    csv_File = file[:-5] # Gets the name of the file

    df.to_csv(csv_File + '.csv', index=False) #  Creates the name of the file

    messagebox.showinfo( "Mensaje", "Archivo " + csv_File + ".csv" +" generado correctamente." )
    
# frame content
image = PhotoImage(file="reference_image.png")
imageLabel = Label(root, image=image)
imageLabel.pack()
imageLabel.place(x=100, y=100)
instructionLabel = Label(root, text="Seleccione el archivo a convertir.")
instructionLabel.pack()
instructionLabel.place(x=20, y=100)
select_btn = Button(root, text="Seleccionar", command=open)# Selecction button
select_btn.pack()

root.mainloop()  # Keeps the window open until the window is closed

# Icons attribution
""" 
Thank you for allow our proyects to be prettier.
Icons made by <a href="https://www.flaticon.com/authors/roundicons" title="Roundicons">Roundicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

"""

