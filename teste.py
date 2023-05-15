import tkinter as tk
import pyaudio

def play_sound():
    chunk = 1024
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)

    data = stream.read(chunk)

    while data:
        stream.write(data)
        data = stream.read(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()

def button_click():
    play_sound()

# Crie a interface gráfica usando tkinter
root = tk.Tk()

# Crie um botão para reproduzir o som
button = tk.Button(root, text="Reproduzir Som", command=button_click)
button.pack()

# Inicie o loop principal do tkinter
root.mainloop()
