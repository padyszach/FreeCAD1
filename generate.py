import FreeCAD as App
import Mesh
import os

# sciezka do pliku FCStd
file_path = os.path.abspath("3.FCStd")

# Otworz dokument
doc = App.openDocument(file_path)

# Pobierz Spreadsheet
sheet = doc.getObject("Spreadsheet")

# Zmien parametry
sheet.set("thickness", "10 mm")
sheet.set("hole_diameter", "40 mm")

# Przebuduj model
doc.recompute()

# Eksport STL
output_path = os.path.abspath("bracket.stl")
Mesh.export([doc.Body], output_path)

print("Test dziala")
