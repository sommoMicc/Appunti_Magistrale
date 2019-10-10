# OFDM odissey part 2
Giovedì 10 ottobre 2019

In un sistema QAM convenzionale si ha una costellazione di punti (16 nel caso del QAM16), ognuno corrisponde ad un simbolo che può essere trasmesso. Per ovviare al problema del whitenoise, basta aggiungere un po' di "spazio" (in frequenza e fase) tra un punto QAM e un altro.

Ad esempio, prendiamo i due segnali $x_0$ e $x_1$, che costituiranno:

$$ y = 2x_0 + x_1 $$
Se ad esempio viene trasmesso un altro segnale $y = 2x_0+2_x1$, i punti QAM di $x_0$ si sovrappongono a quelli di $x_1$, quindi si annullano.

La soluzione potrebbe essere quella di dividere il canale in sottoportanti in modo che i segnali non interferiscano tra di loro.
In pratica:
* si divide il segnale in più segnali narrowband;
* si applicano filtri che interpolano il segnale in pezzi differenti delo spettro separatamente (per ogni narroband);
* lato ricevente, si riapplicano i filtri inversi per "ricostruire" i singoli pezzi del segnale trasmesso originariamente

## Cos'è OFDM
OFDM è ispirato dai principi di divisione dello spettro e inserimento di ogni simbolo in una frazione dello spettro. 

L'idea di OFDM è:
* associare ciascun simbolo QUAM ad una frequenza
* siccome l'antenna ragiona in tempo, è necessario applicare una inverse discrete-time fourier transform (IDFT). Ho quindi ora i segnali espressi in tempo (e non in frequenza)
* effettuare una conversione parallel-to-serial (in pratica, si leggono i punti uno ad uno e si piazzano nel canale)
* inviare il segnale convertito nel canale. Notare che l'effetto della convoluzione effettuata dal canale (in tempo) corrisponde ad una moltiplicazione di segnali nel dominio di frequenza.
* lato ricevente, si effettua una conversione serial-to-parallel, piazzando ogni simbolo in una posizione specifica di un vettore, in base al tempo in cui appaiono
* effettuare una discrete frequency fourier transform (DFT) per andare dal dominio del tempo a quello della frequenza.

Per quanto osservato al punto 3, i vari $b[n]$ (quindi quello che effettivamente riceviamo) sono l'effetto della convoluzione che avviene nel canale:

$$ b[n] = a[n]\cdot H[n] $$
dove $H[n]$ è la frequenza di risposta del canale.

Otteniamo quindi n-*subcarriers*, ognuna trasmettente in un canale differente. Nella conversione parallelo-seriale del canale, oltre a tutti gli n-simboli da trasmettere, vengono ripetuti anche alcuni dei primi simboli trasmessi (si chiama __Cyclic Prefix__). Lato ricevente, esso viene scartato.

Siccome la DFT è lineare, l'output del canale è la somma di tutto quello che avviene al suo interno, quindi il rumore può essere "sommato" ad ogni singolo termine.

## Cyclc Prefix
Prima di tutto, esso evita l'__inter-block interference__. Quando trasmetto un segnale su un canale, esso reagirà con la __impulse response__, quindi il simbolo in realtà verrà trasmesso più volte, con diverse intensità e attenuazioni. Quando poi la trasmissione di un segnale si interrompe, in realtà il ricevente continua a ricevere degli eco relativi agli ultimi dati/simboli trasmessi. Quindi, se subito dopo il primo blocco di dati se ne trasmette un altro, i primi pezzi di esso subiranno interferenze dal primo blocco di dati trasmesso. Grazie al __cyclic-prefix__, se è lungo abbastanza, opera come buffer/separazione tra i blocchi di dati (al posto di usare un silenzio radio). Quindi, lato ricevente, se li scarto, viene eliminata l'inter-block interference.