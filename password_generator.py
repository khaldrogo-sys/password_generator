import tkinter as tk
from tkinter import simpledialog
import pyperclip
import keyboard
import subprocess

# Funktion zum Generieren eines Passworts
def generate_password(length):
    result = subprocess.run(['PwTech.com', '--gen', '1', '--length', str(length)], capture_output=True, text=True)
    output = result.stdout.strip()
    password = output.splitlines()[-1]  # Nimmt die letzte Zeile als Passwort an
    return password

# Funktion zum Öffnen des Eingabefensters
def open_input_dialog():
    print("Hotkey wurde gedrückt")
    root = tk.Tk()
    root.withdraw()  # Versteckt das Hauptfenster
    length = simpledialog.askinteger("Passwortgenerator", "Geben Sie die gewünschte Länge des Passworts ein:")
    if length:
        password = generate_password(length)
        pyperclip.copy(password)
        print("Passwort generiert und in die Zwischenablage kopiert:", password)
    root.destroy()

# Funktion zum Einfügen des Passworts
def paste_password():
    password = pyperclip.paste()
    keyboard.write(password)

# Hotkeys definieren
keyboard.add_hotkey('ctrl+shift+s', open_input_dialog)
keyboard.add_hotkey('ctrl+shift+v', paste_password)

print("Das Skript läuft. Drücken Sie Ctrl+Shift+S, um ein Passwort zu generieren, und Ctrl+Shift+V, um es einzufügen.")
keyboard.wait('esc')  # Warten bis die ESC-Taste gedrückt wird, um das Skript zu beenden
