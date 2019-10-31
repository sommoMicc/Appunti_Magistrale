M = 128; % size of one OFDM block (number of subcarriers)
N = 20; % OFDM symbols you want to transmit
L = 5; % length of the cyclic prefix
x = round(rand(M, N)); % data to be transmitted

y = sqrt(M) * ifft(x); % transmission

% Cyclic prefix
z = [y(M-L+1:M,:); y]; % matrice input della conversione P/S composta da:
                         % - nella prima riga le ultime 5 righe di y (blocco OFDM)
                         % - nelle rimanenti il resto di y (valori OFDM)

PS = reshape(z, 1, (M + L) * N); % conversione parallel/serial


% Lato ricevente
SP = reshape(PS, M+L, N); % conversione serial to parallel
zhat = SP(L+1:M+L, :); % scarto il cyclic prefix, input della DFT

b = fft(zhat) / sqrt(M); % output della DFT, quindi valori ricevuti
