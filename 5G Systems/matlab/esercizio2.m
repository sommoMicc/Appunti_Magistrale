clear all;

M = 9; % size of one OFDM block (number of subcarriers)
N = 4; % OFDM symbols you want to transmit
L = 5; % length of the cyclic prefix
a = round(rand(M, N)); % data to be transmitted

a1 = sqrt(M) * ifft(a); % input della parallel/serial

% Cyclic prefix
PS = [a1(M-L+1:M,:); a1]; % matrice input della conversione P/S composta da:
                         % - nella prima riga le ultime 5 righe di y (blocco OFDM)
                         % - nelle rimanenti il resto di y (valori OFDM)

x = reshape(PS, 1, (M + L) * N); % conversione parallel/serial

w = randn(1, (M + L) * N) + 1i * randn(1, (M + L) * N); % creo il rumore (white gaussian noise)

z = filter(0, 10,x); % filtro impulse response del canale
y = z + w; % segnale grezzo presente effettivamente nel canale

% Lato ricevente
SP = reshape(y, M+L, N); % conversione serial to parallel
zhat = SP(L+1:M+L, :); % scarto il cyclic prefix, input della DFT

b = (fft(zhat)/sqrt(M)) > 0; % output della DFT, quindi valori ricevuti

b == a

