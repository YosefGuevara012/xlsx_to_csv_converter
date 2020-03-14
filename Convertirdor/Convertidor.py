# Required libraries

import os
import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# Global variables

x_pad=10
y_pad=5
btn_h_size=1
btn_w_size=10

# window settings

root = Tk()
root.title('Conversor .xlsx a .csv')
#root.geometry("320x200")
root.resizable(False, False)

# global path variables

filename=""
filename_text = StringVar()
filename_text.set("Archivo no seleccionado")
mydestinaton_File = StringVar()

#Funtions Definition
def select():
    # this funtion get the path of the source file
    global filename, filename_text
    root.filename =  filedialog.askopenfilename(initialdir = "/Escritorio",title = "Seleccione el archivo", filetypes = (("Archivos xlsx","*.xlsx"),("Todos los archivos","*.*")))
    filename = root.filename
    filename_text.set(os.path.abspath(filename))


def convert():
    # this funtion converts the file
    global directory
    # Get the path of the file

    path = os.path.abspath(filename)
    directory, file = os.path.split(path)

    # set the working directory using the path of the file

    os.chdir(directory)

    # File convertion

    df = pd.read_excel(root.filename) # File reading

    csv_File = file[:-5] # Gets the name of the file

    df.to_csv(csv_File + '.csv', index=False) #  Creates the name of the file
    
    mydestinaton_File.set(directory + "\\" + csv_File + '.csv')

    messagebox.showinfo( "Mensaje", "Archivo " + csv_File + ".csv" +" generado correctamente." )



# image settings

image = PhotoImage(file="reference_image.png")
imageLabel = Label(root, image=image)
imageLabel.grid(row="0", column="0", padx=15, pady=y_pad, columnspan=2)

# Buttons settings

## Select button
instructionLabel = Label(root, text="Seleccione el archivo a convertir.")
instructionLabel.grid(row="1", column="0", sticky="e", padx=x_pad, pady=y_pad)
select_btn = Button(root, text="Seleccionar", height=btn_h_size, width=btn_w_size, command=select)
select_btn.grid(row="1", column="1", padx=x_pad, pady=y_pad)

## Orign path label

sourcePathLabel = Label(root, textvariable=filename_text)
sourcePathLabel.grid(row="2",column="0", sticky="e",padx=x_pad, pady=y_pad)
convertion_btn = Button(root, text="Convertir", height=btn_h_size, width=btn_w_size, command=convert)
convertion_btn.grid(row="2",column="1",padx=x_pad, pady=y_pad)

## Destination path label
destinationPathLabel = Label(root, textvariable=mydestinaton_File)
destinationPathLabel.grid(row="3",column="0",padx=x_pad, pady=y_pad, columnspan=2)


# Keeps the window open until the window is closed
root.mainloop()  

# Icons attribution
""" 
Thank you for allow our proyects to be prettier.
Icons made by <a href="https://www.flaticon.com/authors/roundicons" title="Roundicons">Roundicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

"""

