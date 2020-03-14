# Required libraries

from tkinter import filedialog
from tkinter import *
import os
import pandas as pd

# Abosulte route of the document

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/Escritorio",title = "Seleccione el archivo", filetypes = (("Archivos xlsx","*.xlsx"),("Todos los archivos","*.*")))

path = os.path.abspath(root.filename)
dir = os.path.dirname(path)

os.chdir(dir)


# Convertion of the file

df = pd.read_excel(root.filename)
df.to_csv('Archivo_para_importar.csv', index=False) 

print('El archivo para la importación se ha generado exitosamente, se llama Archivo_para_importar.csv.')






