import pyaudio
import wave
import tkinter as tk

def play_sound(filename):           #recebe o nome do arquivo de som
    chunk = 1024                    #tamanho do bloco de audio (1024 é comumente utilizado)
    wf = wave.open(filename, 'rb')  #usa a biblioteca wave para abrir o som
    p = pyaudio.PyAudio()           #cria a instancia da biblioteca pyaudio

    #usa o metodo open do objeto open
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), 
                    # Configurando o formato de audio,
                    # A função get_format_from_width() é um método da classe PyAudio que recebe como argumento a largura
                    # dos dados de áudio em bytes (obtida através do método getsampwidth() do objeto wf, que representa
                    # o arquivo WAV). Essa função retorna o formato correspondente ao número de bytes especificado. 

                    channels=wf.getnchannels(),   
                    # Ele define como o áudio será reproduzido, se será mono ou estéreo,
                    # O método getnchannels() é um método do objeto wf, que representa o arquivo WAV.
                    # Ele retorna o número de canais do áudio, ou seja, quantos canais de áudio estão presentes no arquivo.
                    # Os canais podem representar diferentes fontes sonoras, como áudio mono (1 canal) ou áudio estéreo (2 canais).

                    # Portanto, ao atribuir channels=wf.getnchannels(), estamos obtendo o número de canais do arquivo WAV
                    # e passando-o como argumento para configurar o número de canais do stream de áudio.              
                            
                    rate=wf.getframerate(),
                    # Configurando a taxa de amostragem,
                    # No código fornecido, a taxa de amostragem do arquivo WAV é obtida usando a função getframerate() do
                    # objeto wf (wave file). Essa taxa é então atribuída à variável rate, que será usada para configurar o fluxo
                    # de áudio durante a reprodução.
                    # Ao abrir o fluxo de áudio com p.open(), o parâmetro rate é definido com o valor retornado
                    # por wf.getframerate(). Isso garante que o fluxo de áudio seja configurado corretamente para reproduzir
                    # o áudio na taxa de amostragem adequada, garantindo uma reprodução fiel do áudio do arquivo WAV.

                    output=True) # No trecho de código output=True, o parâmetro output é usado ao abrir o fluxo de áudio
                                 # com p.open() para indicar que o fluxo será usado para reprodução de áudio.
                                 # O parâmetro output define se o fluxo será de entrada (captura de áudio) ou de
                                 # saída (reprodução de áudio). Quando definido como True, indica que o fluxo será de saída,
                                 # ou seja, o áudio será reproduzido.

    data = wf.readframes(chunk)
    #le o chunk(frame de audio) e armazina na variavel 'data'

    while data:  #loop para reproduzir o audio frame a frame enquanto possuir frame(data)  #enquanto data for verdadeira (diferente de vazio)
        stream.write(data)     # escreve o frame de audio
        data = wf.readframes(chunk)  #atualiza a variavel 'data'

    stream.stop_stream()  # metodo de para para o stream de audio
    stream.close()  # fecha o stream de audio

    p.terminate()   # encessa a instacia para liberar recursos

def button_click(filename):
    play_sound(filename)

# Crie a interface gráfica usando tkinter
root = tk.Tk()

# Crie botões para cada som
button1 = tk.Button(root, text="Som 1", command=lambda: button_click("som1.wav"))
button1.pack()

button2 = tk.Button(root, text="Som 2", command=lambda: button_click("som2.wav"))
button2.pack()

# Inicie o loop principal do tkinter
root.mainloop()