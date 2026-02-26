import numpy as np
import matplotlib.pyplot as plt

def analyze_signals():
    # 1. Configuración de tiempo
    fs = 1000  # Frecuencia de muestreo
    t = np.linspace(0, 1, fs, endpoint=False)

    # 2. Definición de señales
    # Senoidal de 50Hz
    signal_sine = np.sin(2 * np.pi * 50 * t)
    
    # Pulso Rectangular (1 en el centro, 0 el resto)
    signal_rect = np.where((t > 0.4) & (t < 0.6), 1.0, 0.0)
    
    # Función Escalón (Heaviside)
    signal_step = np.where(t >= 0.5, 1.0, 0.0)

    signals = [('Senoidal', signal_sine), ('Pulso Rectangular', signal_rect), ('Escalon', signal_step)]

    for name, sig in signals:
        # 3. Cálculo de la Transformada de Fourier (FFT)
        fft_values = np.fft.fft(sig)
        fft_freqs = np.fft.fftfreq(len(sig), 1/fs)
        
        # Obtener solo la mitad positiva del espectro para graficar mejor
        n = len(sig)
        mag = np.abs(fft_values)[:n//2]
        freqs = fft_freqs[:n//2]

        # 4. Visualización
        plt.figure(figsize=(12, 4))
        
        # Gráfica en el Tiempo
        plt.subplot(1, 2, 1)
        plt.plot(t, sig)
        plt.title(f'{name} - Dominio del Tiempo')
        plt.grid()

        # Gráfica en la Frecuencia (Magnitud)
        plt.subplot(1, 2, 2)
        plt.stem(freqs, mag,)
        plt.title(f'{name} - Espectro de Frecuencia')
        plt.xlim(0, 100) # Limitamos a 100Hz para ver mejor
        plt.grid()
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    analyze_signals()