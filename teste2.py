import tkinter as tk
import sounddevice as sd
import soundfile as sf
import threading

def play_audio(filename):
    data, fs = sf.read(filename, dtype='float32')
    sd.play(data, fs, blocking=True)

def button_click(filename):
    audio_thread = threading.Thread(target=lambda: play_audio(filename))
    audio_thread.start()

# Crie a interface gráfica usando tkinter
root = tk.Tk()

# Crie botões para reproduzir diferentes áudios
button1 = tk.Button(root, text="Efeito 1", command=lambda: button_click("cavalo.wav"))
button1.pack()

button2 = tk.Button(root, text="Efeito 2", command=lambda: button_click("efeito2.wav"))
button2.pack()

button3 = tk.Button(root, text="Efeito 3", command=lambda: button_click("efeito3.wav"))
button3.pack()

# Inicie o loop principal do tkinter
root.mainloop()