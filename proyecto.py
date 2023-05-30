from IPython.display import Image
from playsound import playsound
import numpy as np
import scipy.fftpack as fourier
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
import soundfile as sf
import sounddevice as sd
import pyaudio as pa
import struct
from scipy import signal



def readFile(file):
    data = None
    try:
        data, fm = sf.read(file)
        info = sf.info(file)

    except (TypeError, sf.SoundFileError) as e:
        print("Error trying to read file.", str(e))
        raise 
    return data, fm, info

def playFile(file):
    try:
        #playsound(file)
        playsound(file)
    except (TypeError, Exception) as e:
        print("Error trying to play file.", str(e))

def plotAud(file):
    data, fm = sf.read(file)
    Aud = data
    L = len(Aud) 
    n = np.arange(0,L)/fm 
    playFile(file)
    plt.plot(n,Aud)
    plt.show() 
    
# Muestra por pantalla el plot del archivo de audio y su respectiva   
def plotFreq(file):
    data, fm = sf.read(file)
    Aud = data
    L = len(Aud) 
    n = np.arange(0,L)/fm   

    transf = fourier.fft(Aud)                        # Calculamos la FFt de la señal de audio
    Mag = abs(transf)                                   # Tomamos la Magnitud de la FFT
    Mag = Mag[0:L//2]                              # Tomamos la mitad de los datos (recordar la simetría de la transformada)

    ang = np.angle(transf)
    F = fm*np.arange(0, L//2)/L
    
    plt.figure(figsize=(10, 6))
    plt.plot(F, Mag)
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud FFT')
    plt.title('Dominio de Frecuencias')
    plt.grid(True)
    plt.show()


# plot en tiempo real: 
def plotRealTimeSpectrum(file):
    data, fm, info = readFile(file)
    duration = len(data) / fm

    # Reproduce el archivo de audio
    def audioCallback(indata, frames, time, status):
        # Calcula la transformada de Fourier de la señal de audio
        fft_data = np.fft.fft(indata[:, 0])
        frequencies = np.fft.fftfreq(len(indata[:, 0]), 1/fm)
        magnitudes = np.abs(fft_data)

        # Limpia el plot anterior y dibuja el espectro de frecuencias actualizado
        plt.clf()
        plt.subplot(2, 1, 1)
        plt.plot(np.arange(len(indata[:, 0])) / fm, indata[:, 0])
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Amplitud')
        plt.title('Señal de Audio en Tiempo Real')

        plt.subplot(2, 1, 2)
        plt.plot(frequencies, magnitudes)
        plt.xlabel('Frecuencia (Hz)')
        plt.ylabel('Amplitud FFT')
        plt.title('Espectro de Frecuencias en Tiempo Real')

        plt.tight_layout()
        plt.grid(True)
        plt.pause(0.001)

    # Configura el dispositivo de audio para la reproducción
    sd.default.samplerate = fm
    sd.default.channels = 1

    # Reproduce el archivo de audio y muestra el espectro y la señal en tiempo real
    with sd.InputStream(callback=audioCallback):
        print(f"Reproduciendo archivo: {file}")
        sd.play(data, blocking=True)

    plt.close()    

def applyLowpassFilter(file, cutoff_freq, filter_order=4):
    data, fm, info = readFile(file)
    duration = len(data) / fm

    # Diseña el filtro paso bajo
    nyquist_freq = 0.5 * fm
    normalized_cutoff_freq = cutoff_freq / nyquist_freq
    b, a = signal.butter(filter_order, normalized_cutoff_freq, btype='low')

    # Reproduce el archivo de audio con el filtro aplicado y muestra el espectro en tiempo real
    def audioCallback(indata, frames, time, status):
        # Aplica el filtro paso bajo a la señal de audio
        filtered_data = signal.lfilter(b, a, indata[:, 0])

        # Calcula la transformada de Fourier de la señal filtrada
        fft_data = np.fft.fft(filtered_data)
        frequencies = np.fft.fftfreq(len(filtered_data), 1/fm)
        magnitudes = np.abs(fft_data)

        # Limpia el plot anterior y dibuja el espectro de frecuencias actualizado
        plt.clf()
        plt.subplot(2, 1, 1)
        plt.plot(np.arange(len(indata[:, 0])) / fm, indata[:, 0])
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Amplitud')
        plt.title('Señal de Audio en Tiempo Real')

        plt.subplot(2, 1, 2)
        plt.plot(frequencies, magnitudes)
        plt.xlabel('Frecuencia (Hz)')
        plt.ylabel('Amplitud FFT')
        plt.title('Espectro de Frecuencias en Tiempo Real')

        plt.tight_layout()
        plt.grid(True)
        plt.pause(0.001)

    # Configura el dispositivo de audio para la reproducción
    sd.default.samplerate = fm
    sd.default.channels = 1

    # Reproduce el archivo de audio con el filtro y muestra el espectro y la señal en tiempo real
    with sd.InputStream(callback=audioCallback):
        print(f"Reproduciendo archivo: {file} con filtro paso bajo a {cutoff_freq} Hz")
        sd.play(data, blocking=True)

    plt.close()

# pruebas:     
readFile('batman.wav')
# plotRealTimeSpectrum("batman.wav")
applyLowpassFilter("batman.wav", cutoff_freq=100)
# plot_audio_spectrum('batman.wav')
# plot_audio_realtime('batman.wav')
