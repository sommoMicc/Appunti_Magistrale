# MIMO

Lunedì 18 Novembre 2019

## Multiple antenna System

MiMo significa che almeno un soggetto (trasmittente o ricevente) è equipaggiato almeno con due antenne.
Un motivo per usare MiMo è che, avendo più canali di comunicazione (uno per antenna), si ha più probabilità di trovare un canale "buono". Inoltre, avendo più copie del segnale ricevute da tutte le antenne, ed essendo il rumore indipendente, si ha più possibilità di identificaro ed eliminarlo (facendo la media dei valori ricevuti dalle varie antenne). Infine, si ha la possibilità di trasmettere più datastream (uno per antenna) alla volta.

## Narrowband Multiple Antenna Model

I segnali trasmessi vanno da 1 a $N_T$, mentre quelli ricevuti vanno da 1 a $N_R$. Combinando OFDM e MiMo, il risultato è quello dell'immagine: invece di avere un canale wideband si hanno numerosi canali narrowband (il cui dato trasmesso è l'input moltiplicato per un numero complesso, ovvero $h_{m,n}$, guadagno del canale).

$$r_m[k] = \sum_{n=1}^{N_T} h_{m,n} s_n[k] + w_m[k]$$
dove $k$ è un indice temporale. Da notare che, non essendoci un $k$ al pedice di $h$, si assume che il canale non cambi col passare del tempo.
Il potenziale di questo modello è dato da quanto osservato nella sezione precedente, mentre il problema è che c'è un sacco di interferenza!

## MiMo Systems

Il sistema si può rappresentare come

$$r[k] = H\cdot s[k] + w[k]$$
dove H è una matrice complessa avente come cella $m,n$ il valore $h_{m,n}$

## Special Cases

- $N_T > 1, N_R = 1$, si ha un _Muliple input single output system (MISO)_. Questo comporta che $H$ è un vettore $1 \times N_T$ e $r[k]$ è uno scalare. Datosiché i nostri telefoni hanno una sola antenna mentre la _base-station_ ne ha molte, questo è lo scenario in cui la telefonia mobile opera (in downlink).
- $N_T = 1, N_R > 1$, si ha un _Single input Multiple Output System (SIMO)_. H in questo caso è un vettore $N_R \times 1$ e $s[k]$ è uno scalare.

## Examples

1. SiMo
2. MiSo. Divido per radice di due per usare una potenza di trasmissione uguale al sistema SiSo (con cui voglio confrontare le performance). L'esempio dei calcoli mostra come, trasmettendo da due sorgenti diverse aventi guadagni opposti (penso), i due segnali si annullano e quindi ottengo solo noise!

# Capacity of MiMo System

L'analisi della capacità di un sistema MiMo serve anche a dare un'idea di quanto incrementa la capacità del sistema aggiungendo un'antenna lato ricevente o lato trasmittente (ad esempio).

## MiMo AWGN Channel Capacity

Il canale considerato è MiMo AWGN narrowband (quello di prima).
La capacità del canale è il massimo della mutua informazione tra l'input e l'output, moltiplicato per la larghezza di banda $B$. Il power-constraint è $E[x^H\cdot x] = 1$, che sarà uno scalare (somma del modulo quadrato delle due x).
$I$, la mutua informazione, è definita come la differenza delle entropie $H$ tra $y$ e $y|x$ ($y$ dato $x$, come in probabilità).

## Entropy of Gaussian Vector

Strana formula del PDF del vettore ZMCSCG, dove PDF sta per [probability density function](https://en.wikipedia.org/wiki/Probability_density_function).

formule ancora

$$E(Hx(Hx)^H) = E(Hxx^HH^H) = HR_XH^H $$
perché $xx^H$ è la correlation matrix di $x$

"trace" di una matrice è la somma degli elementi della diagonale.
