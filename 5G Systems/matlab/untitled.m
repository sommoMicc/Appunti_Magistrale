% Come generare un numero di bit casuale:
% * genero un array di 10 numeri casuali (compresi tra 0 e 1)
% * arrotono i numeri così ottengo un array di 0 e 1 equidistribuiti
N = 10 % Numero di bit totali

R = round(rand(1,N));
s = R * -2 + 1 + round(rand(1,N)) * 2i - 1i; % creo un vettore di -1 e 1

w = randn(1, N) + 1i * randn(1,N); % creo il rumore (white gaussian noise)
r = s + w; % aggiungo il rumore al canale

% Implementazione del filtro (con impulse response)
h = [1 -5];
x = rand(1,5);
y = filter(h, 1, x)

bhat = (ric > 0) % per capire quando ho trasmesso uno zero o un uno