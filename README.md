# FreeCAD1
Generator wariantów części 3D
🛠 Wymagania
Najnowsza wersja Python :)
Zainstalowany FreeCAD (wersja 0.21 lub nowsza)
Dostęp do FreeCADCmd
Python wbudowany w FreeCAD (uruchamianie przez FreeCADCmd)
📂 Struktura projektu
FreeCAD1/
3.FCStd          # Parametryczny model CAD<br>
generate.py          # Skrypt automatyzujący<br>
bracket.stl          # Wygenerowany plik wynikowy<br>
config.json      # parametry do modyfikacji<br>
README.md<br>
⚙️ Parametry modelu
Model wykorzystuje arkusz Spreadsheet w FreeCAD z aliasami:
thickness – grubość elementu
hole_diameter – średnica otworu
Parametry są powiązane ze szkicem oraz operacjami bryłowymi (Pad / Pocket).
▶️ Jak uruchomić projekt
Wprowadź twoje parametry w pliku .json
W terminalu przejdź do folderu projektu i wykonaj:
FreeCADCmd generate.py
Po uruchomieniu:
model zostanie otwarty,
parametry zostaną zmodyfikowane w skrypcie,
geometria zostanie przeliczona,
wygenerowany zostanie plik STL.

