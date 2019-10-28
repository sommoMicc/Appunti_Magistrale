# Channel Estimation for OFDM and SC-FDMA
Lunedì 28 ottobre 2019

## Channel Estimation
La stima del canale avviene tipicamente nel dominio delle frequenze $H[n], n=0...N-1$. Il canale funziona come il prodotto tra la frequenza trasmessa e il canale più il rumore:

$$b[n] = H[n]a[n] + W[n]$$
Per stimare il canale (quindi $H[n]$) si può trasmettere un **simbolo pilota**, quindi noto anche al ricevente, il quale, dividendo $\frac{b[n]}{a[n]}$ riesce a stimare il canale (includendo però purtroppo il rumore nel risultato). 

La scelta del simbolo è importante, perché, nel caso di una costellazione QAM, più il simbolo trasmesso è esterno e più la sua trasmissione richiederà potenza, ma il segnale sarà meno influenzato dal rumore. Al contrario, se il simbolo è vicino al centro, il suo segnale sarà troppo contaminato dal rumore (non riuscirà a sovrastarlo).

I canali in frequenze differenti sono in qualche maniera correlate ai valori in dominio di tempo. Infatti, H[n] può essere ottenuto tramite una $DFT$, con un numero di sottoportanti N molto più grande di L (che è la lunghezza del canale)

E' da ricordare che il canale cambia nel corso del tempo.


## Block-type Pilot Arrangement
Nell'immagine della slide, i cerchi neri rappresentano i simboli pilota, mentre quelli bianchi i dati "utili" trasmessi. Il fatto della trasmissione dei simboli pilota in tutte le sottoportanti ad intervalli regolari è effettuata per riestimare il canale dopo un suo cambiamento. L'intervallo $S_t$ che intercorre tra la trasmissione di un simbolo pilota e un altro è minore dell'effetto Doppler:

$$S_t \le \frac{1}{f_{Doppler}}$$
dove $f_{Doppler}$ è la massima frequenza Doppler.

Datosiché il canale cambia continuamente, i valori del canale tra due letture del _simbolo pilota_ possono essere interpolati o con il __sampling theorem__ (nel caso si avessero pochi campioni) o con un'interpolazione semplice (tipo quella lineare, nel caso si avessero frequenti campioni, come succede di solito). La tecnica dell'interpolazione, tuttavia, aumenta la latenza, perché necessita che i simboli vengano inseriti in un buffer per poi calcolare l'interpolazione

## Comb-type Pilot Arrangement
Al posto di porre i simboli pilota in ogni sottoportante con una frequenza fissa, i simboli pilota vengono trasmessi in modo continuo su alcune sottoportanti selezionate. In questo caso, lo spazio tra due sottoportanti riservate alla trasmissione del simbolo pilota deve essere minore o uguale al _channel impulse response_:

$$ S_f \le \frac{1}{\sigma_{max}}$$
dove $\sigma_{max}$ rappresenta il ritardo massimo di diffusione della _impulse response_ del canale: più lungo è il canale, più frequentemente bisogna avere sottoportanti riservate alla trasmssiione del simbolo pilota. Anche in questo caso si possono interpolare i valori delle *sottoportanti-dati* usando interpolazione tra le frequenze di due *sottoportanti-pilot*. Inoltre, l'interpolazione tra due frequenze non aumenta la latenza, perché viene già fatto da OFDM

In generale, si preferisce un *Block-type arrangement* quando il canale cambia in modo molto lento, come l'ADSL (trasmessa con il cavo). Quando invece il canale cambia molto velocemente, è preferibile usare il *Comb-type arrangement*.

## Lattice-type Pilot Arrangement
I simboli pilota sono messi in diagonale più o meno. Questa tecnica è più complessa da implementare, anche perché richiede tecniche di interpolazione bidimensionali. 

## Simple estimation approach
Nel caso di un _Comb-type_ arrangement, dove i simboli pilota sono spaziati da _S_ sottoportanti, per stimare il canale:
* calcolare $\tilde{H}[nS] = \frac{b[nS]}{a[nS]}$
* Interpolare nelle altre sottoportanti (formula lunga delle slide)

## DFT-based Channel Estimationn
Problema: le stime "LeastSquare channel estimation" contengono anche il rumore!! Quindi i simboli $\tilde{H}$ sono già contaminati dal rumore, il quale si diffonderà anche nel time-domain. Notare però che le $\tilde{H}[L] \to \tilde{H}[N-1]$ saranno ignorate (quindi avranno solo rumore), perché vanno oltre la lunghezza del canale. Questi valori verranno impostati a 0 dalla DFT (lato ricevente), quindi verrà eliminato un bel po' di rumore.


# General Linear Minimum Mean Square Error
Affanno
