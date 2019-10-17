# Downlink Multiple Users. FEC in 5G systems. Peak to Average Power Ratio.

17 Ottobre 2019

Spiegazione dell'ambiente matlab

##### Fft
per fare la discrete Fourier transform del vettore h di lunghezza N si calcola $\bar{h}$, che è h esteso alla fine con $N - |h|$ zeri. Alla fine si effettua la Fast Fourier Transform (versione rapida della DFT) di $\bar{h}$