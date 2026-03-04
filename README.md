# FreeCAD1<br>
Generator wariantów części 3D<br>
🛠 Wymagania<br>
Najnowsza wersja Python :)<br>
Zainstalowany FreeCAD (wersja 0.21 lub nowsza)<br>
Dostęp do FreeCADCmd<br>
Python wbudowany w FreeCAD (uruchamianie przez FreeCADCmd)<br>
📂 Struktura projektu<br>
FreeCAD1/<br>
3.FCStd          # Parametryczny model CAD<br>
generate.py          # Skrypt automatyzujący<br>
bracket.stl          # Wygenerowany plik wynikowy<br>
config.json      # parametry do modyfikacji<br>
README.md<br>
⚙️ Parametry modelu<br>
Model wykorzystuje arkusz Spreadsheet w FreeCAD z aliasami:<br>
thickness – grubość elementu<br>
hole_diameter – średnica otworu<br>
Parametry są powiązane ze szkicem oraz operacjami bryłowymi (Pad / Pocket).<br>
▶️ Jak uruchomić projekt<br>
Wprowadź twoje parametry w pliku .json<br>
W terminalu przejdź do folderu projektu i wykonaj:<br>
FreeCADCmd generate.py<br>
Po uruchomieniu:<br>
model zostanie otwarty,<br>
parametry zostaną zmodyfikowane w skrypcie,<br>
geometria zostanie przeliczona,<br>
wygenerowany zostanie plik STL.<br>

