import tkinter as tk
import sounddevice as sd
import soundfile as sf

def button_click(filename):
    data, fs = sf.read(filename, dtype='float32') #funcao read da biblioteca soundfile para ler dados do arquivo de audio
    sd.play(data, fs, blocking=False) #funcao play da biblioteca sounddevice para reproduzir o audio

# Crie a interface gráfica usando tkinter
root = tk.Tk()

# Crie botões para reproduzir diferentes áudios
button1 = tk.Button(root, text="Efeito 1", command=lambda: button_click("songs/cavalo.wav"))
button1.pack()

button2 = tk.Button(root, text="Efeito 2", command=lambda: button_click("efeito2.wav"))
button2.pack()

button3 = tk.Button(root, text="Efeito 3", command=lambda: button_click("efeito3.wav"))
button3.pack()

# Inicie o loop principal do tkinter
root.mainloop()