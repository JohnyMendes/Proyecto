# Algorisima i Programación Audiovisual - Proyecto Final

# Visualizador de espectro de audio

## Gabriel Lorenzo y Johny Silva

# 1. Introducción
El objetivo de este proyecto es analizar y filtrar señales de audio en tiempo real, utilizando técnicas de procesamiento digital de señales. Se han desarrollado diversas funciones y herramientas para la lectura y representación de archivos de audio, así como para el análisis espectral de las señales capturadas en tiempo real desde un archivo de audio o un micrófono. Además, se ha implementado la capacidad de aplicar un filtro paso bajo a la señal de audio, permitiendo observar los efectos del filtrado en el dominio del tiempo y la frecuencia.

# 2. Desarrollo
## 2.1. Lectura y Representación del Archivo de Audio
Para poder trabajar con las señales de audio, se ha implementado la función readFile(file) que permite leer un archivo de audio en formato WAV. Esta función utiliza la biblioteca soundfile para cargar los datos del archivo y obtener información como la frecuencia de muestreo y la duración. Además, se ha desarrollado la función plotAud(file) que muestra por pantalla el plot de la señal de audio en el dominio del tiempo.

## 2.2. Espectro de la Señal
Para visualizar el contenido espectral de la señal de audio, se ha creado la función plotFreq(file) que calcula la transformada de Fourier de la señal y muestra el espectro de frecuencias. Utilizando la biblioteca scipy.fftpack, se obtienen los coeficientes de la transformada de Fourier y se calculan las magnitudes correspondientes. El espectro de frecuencias se representa gráficamente utilizando la biblioteca matplotlib.

## 2.3. Espectro en Tiempo Real desde Archivo de Audio
Para analizar la señal de audio en tiempo real desde un archivo, se ha implementado la función plotRealTimeSpectrum(file). Esta función reproduce el archivo de audio utilizando la biblioteca sounddevice y captura la señal en tiempo real utilizando un callback. En cada iteración del callback, se calcula la transformada de Fourier de la señal capturada y se muestra el espectro de frecuencias actualizado en una ventana gráfica. Esto permite visualizar los cambios en el espectro a medida que se reproduce el archivo.

## 2.4. Espectro en Tiempo Real desde Micrófono


## 2.5. Filtraje de la Señal del Archivo de Audio
Con el objetivo de aplicar un filtrado a la señal de audio, se ha creado la función applyLowpassFilter(file, cutoff_freq, filter_order=4). Esta función utiliza la biblioteca scipy.signal para diseñar un filtro paso bajo utilizando el método Butterworth. La función recibe como parámetros el archivo de audio a filtrar, la frecuencia de corte del filtro y el orden del filtro.

Dentro de la función, se lee el archivo de audio utilizando la función readFile(file), se calcula la duración de la señal y se obtiene la frecuencia de muestreo. A continuación, se diseña el filtro paso bajo utilizando la función signal.butter(), especificando la frecuencia de corte normalizada y el orden del filtro.

Para reproducir el archivo de audio con el filtro aplicado, se utiliza la función sounddevice.play(), y se captura la señal filtrada en tiempo real mediante el callback audioCallback(). En cada iteración del callback, se aplica el filtro paso bajo a la señal de audio utilizando signal.lfilter(). Luego, se calcula la transformada de Fourier de la señal filtrada y se muestra el espectro de frecuencias actualizado en una ventana gráfica.

# 3. Programa para Acceder a las Funciones
Se ha construido un programa principal que permite acceder a las funciones desarrolladas anteriormente. En este programa, se importan las bibliotecas necesarias, como numpy, scipy, matplotlib, soundfile, sounddevice y pyaudio. Luego, se pueden llamar a las funciones según sea necesario, pasando los parámetros adecuados, como el nombre del archivo de audio y la frecuencia de corte del filtro.

# 4. Conclusiones
En este proyecto, se ha logrado desarrollar un conjunto de funciones y herramientas que permiten la lectura, representación y análisis de señales de audio. Se han implementado funciones para visualizar el espectro de frecuencias de las señales, tanto desde archivos de audio como en tiempo real desde un micrófono. Además, se ha incorporado la capacidad de aplicar un filtro paso bajo a las señales de audio, lo que permite observar los efectos del filtrado en tiempo real. Estas herramientas ofrecen una forma intuitiva y práctica de trabajar con señales de audio y explorar su contenido espectral.

# 5. Referencias
Documentación oficial de Python: https://docs.python.org/
Documentación de NumPy: https://numpy.org/doc/
Documentación de SciPy: https://docs.scipy.org/doc/
Documentación de Matplotlib: https://matplotlib.org/stable/contents.html
Documentación de SoundFile: https://pysoundfile.readthedocs.io/en/latest/
Documentación de SoundDevice: https://python-sounddevice.readthedocs.io/en/latest/
Documentación de PyAudio: https://people.csail.mit.edu/hubert/pyaudio/docs/