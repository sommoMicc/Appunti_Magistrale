# Massive MIMO
2 Dicembre 2019

Il **massive MIMO** è una tecnica che ammette un numero di antenne che tende all'infinito (tenendo finito il numero di utenti).

Ovviamente, in un cellular-system è il numero delle antenne alla base-station che tende all'infinito.

$$y_u = \sum_{k=1}^K \frac{1}{N_{BS}} H_u^T H_k^* \tilde{x}_k + w_u$$

Se il numero di antenna tende all'infinito, la dimensione dei vettori $H_u^T$ e $H_k^*$ tendono all'infinito.

Con un po' di calcoli e conseguenze logiche, basate prevalentemente sull fatto che $\frac{1}{N_{BS}} H_u^T H_k^*$ ha potenza unitaria, quindi la media dele potenze è 1, si ha che:

$$y_u = \tilde{x}_u + w_u$$
con $N \to \infty$. Quindi quello che l'utente riceverà sarà solo il simbolo trasmesso + il rumore bianco gaussiano. Inoltre, siccome il numero di antenne è infinito, la probabilità che due utenti usino lo stesso canale è pressoché 0, quindi gli utenti sono sempre distinguibili.

### Problematiche

In caso di _Massive-MIMO_ la stima del canale diventa critica perché il numero di segnali-pilota che bisogna trasmettere aumenta drammaticamente.

$y = [H_1..H_k] \cdot [x_1...x_k]^T$. $[H_1..H_k]$ ha grandezza $N_BS \cdot k$, mentre il vettore colonna $[x_1...x_k]^T$ ha dimennsione $k\cdot N_{PILOT}$.

$Y X^T (X X^T)^{-1} = H(X X^T)(X X^T)^{-1} = H$, siccome $(X X^T)(X X^T)$ è la matrice di identità.

# Antenna Diversity Techniques

Antenna Diversity Techniques è l'idea di usare multiple antenne per aumentare l'affidabilità di uno stream di dati. A differenza di MiMO multiplexing, qua non vengono spinti più databit, ma si vuole che questi databit arrivino a destinazione in modo affidabile.

Sapendo che $\sigma^2_w = \frac{N_0}2$, si ottiene che il bit error rate è una generica funzione Q che come argomenti ha:

$$BER = Q(\sqrt{2||h||^2 \Gamma})$$
Gli integrali nella slide lasciamoli stare che sono complicati, nel senso il calcolo non lo abbiamo trattato.
Morale della favola: il BER scende più velocemente con l'aumentare del numero delle antenne.

Ad un certo punto c'è una divisione per $\sqrt{|h_1|^2 + |h_2|^2}$ per preservare la potenza.

## Alamouti Code

Un modo per trasmettere i segnali tra le due antenne in modo che siano ricevuti propriamente (senza interferenze).
