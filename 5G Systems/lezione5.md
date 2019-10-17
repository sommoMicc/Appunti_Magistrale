# OFDM and Waterfiling algorithm
Lunedì 14 ottobre 2019

## Capacity of OFDM
La capacità del canale è il massimo numero di bit per secondo che si possono trasmettere nel canale con una probabilità di errore molto bassa (bit error rate). Se si trasmette più velocemente della capacità del canale, prima o poi arriva un bit errato (come l'inculata di Tullio). Se si è disposti a tollerare una percentuale di errore si può anche trasmettere più velocemente della capacità del canale.

La capacità di un canale in cui si utilizza OFDM è:

$$ C_{OFDM} = \frac {1}{T} \frac{N}{N+L} \sum_{n=1}^{N}log_2 (1 + \frac{P[n]|H[n]|}{\sigma^2_W}) $$ 
dove $P[n]$ è la potenza trasmessa sulla sottoportante $n$, $L$ è la lunghezza del $CP$, $T$ è il transmission rate, $H[n]$ è il guadagno della sottoportante $n$.

OFDM ha N sottoportanti "additive White Gaussian Noise (AWGN)". Ciascuna sottoportante ha un rumore AWGN con media 0 __indipendente rispetto agli altri canali__ (importante), perché i simboli trasmessi sono indipendenti tra le varie sottoportanti. Per questo motivo è inutile utilizzare un ECC (error correcting code) che ragioni in parallelo nel canale, ovvero che consideri $a[1], a[2], .., a[N]$ ad un dato momento.


### Esempio della lavagna
In un secondo devo processare N samples, quindi nello stesso tempo devo sbarazzarmi di tutti gli N+L simboli che devo trasmettere, altrimenti i bit iniziano ad accumularsi. La lunghezza di ogni sample è quindi $T' = \frac {T}{N+L}$. Consegue che $T = T'(N+L)$
Quindi, $C_{OFDM} = \frac{1}{T'(N+L)}\sum_{n=1}^{N}log_2 ..$
Da notare che, maggiore è la lunghezza del cyclic prefix ($L$), minore sarà la capacità del segnale. Poi ha spiegato cosa sia l'$N$ al numeratore ma non ho mica capito. C'entra con la frequenza di arrivo dei simboli ($\frac{T}{N}$)

Abbiamo detto che nella sottoportante $n$ si utilizza una potenza $P[n]$. Ma a quando ammonta questo valore? E soprattutto, chi ha detto che dobbiamo dare la stessa potenza su tutte le sottoportanti? Ecco che si formula un altro problema: data una _power constraint_ $\sum_{n=1}^{N} P[n] = \bar{P}$, quanta potenza utilizzare per ogni sottoportante.
Formalmente:

$$ max_{P[n]} C_{OFDM}, s.t. \sum_{n=1}^{N}P[n] = \bar{P} $$
Si può applicare il fattore di *Lagrange* per risolvere il problema (massimo vincolato, ricerca operativa/analisi, non poi così strano insomma). Infatti, la funzione da massimizzare è concava, quindi ammette un singolo massimo (che si trova o nel dominio o nella frontiera) e il vincolo è lineare. Basta calcolare la derivata e via, se vuela. Da tutto questo ne deriva che la potenza ottimale 

$$ P[n]^* = (\frac{1}{\lambda}-\frac{\sigma^2_W}{|H[n]|^2})^+$$
La parentesi con il "+" implica che se l'output è minore o uguale a 0, si tiene 0 (non sono ammessi valori negativi di potenza). Se $H[n]$ (guadagno del canale) è molto basso, non investo potenza (perché tanto la trasmissione sarà un pacco fotonico).

## Waterfiling algorithm
Per calcolare $\lambda$ posso usare il seguente algoritmo.

Rappresentoando il reciproco di $\frac{\sigma^2_W}{|H[n]|^2}$, ovvero $\frac{|H[n]|^2}{\sigma^2_W}$, si otteine un grafico che può essere interpretato come il waterfiling algorithm: c'è un lago con un fondale irregolare, quando lo riempio calcolo la distanza tra la superfice dell'acqua e un punto del fondale (che rappresenta un canale): quell'altezza sarà la potenza che dovrò mettere in quel canale. L'acqua utilizzata è limitata (e rappresenta il vincolo di potenza). A livello pratico, però, non è facile da implementare. 

La formula che rappresenta il livello del lago (altezza dal fondale alla superfice dell'acqua) è:

$$ \sum_{n=1}^{N} (\frac{1}{\lambda}-\frac{\sigma^2_W}{|H[n]|^2})^+ = \bar{P}$$


Per prima cosa bisogna capire quali sono le sottoportanti che non riceveranno potenza. Per farlo, ordino le sottoportanti in ordine di guadagno decrescente (le migliori per prime). Suppongo inizialmente che tutti gli $N$ subchannels siano attivi. Calcolo $\lambda$ e se condizione 2 non è soddisfatta (non ho abbastanza potenza da dare a tutti), provo a decrementare di uno il numero di canali attivi e ricomincio il cilco. 

Per scalare una costellazione QAM (da distanza 1 a distanza 3) è il quadrato della distanza dal centro del grafico al punto QAM. Quindi, se ho un QAM in cui tutti i simboli sono distanziati di $3$ (in coordinate) dall'origine, ognuno dista dal centro $3\sqrt 2$, quindi la potenza media per simbolo richiesta è $3$.