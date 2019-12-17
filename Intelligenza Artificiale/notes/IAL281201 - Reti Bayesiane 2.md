#Lezione 28 - Reti Bayesiane 2

Con le reti Bayesiane è possibile fare **inferenza esatta** tramite enumerazione.

![](./immagini/l28-simple.png)

Una possibile query è **P**(B|j,m), per ottenere la distribuzione di probabilità della variabile _B_ dato che entrambi i vicini hanno chiamato.

L'inferenza per enumerazione viene poi fatta riducendosi alla tabella della distribuzione di probabilità congiunta, andando a sommare sui valori delle variabili nascoste (marginalizzazione sulle variabili nascoste).

La distribuzione della probabilità congiunta può essere poi fattorializzata utilizzando la semantica globale data dalla topologia della rete bayesiana.

Nel caso pessimo, per calcolare la distribuzione congiunta servono _n\*2<sup>n</sup>_ operazioni (variabili booleane), sfruttando la topologia si riesce a scendere a _O(n)_ per il tempo e _O(d<sup>n</sup>)_ per lo spazio.
## Algorimto di enumerazione

![](./immagini/l28-enumerazione.png)

L'algoritmo esegue il calcolo delle varie sommatorie, riscorsivamente, in profondità e a partire da quella più a sinistra. Da notare che prima di ritornare la risposta alla query, questa deve essere normalizzata.

Questo approccio è inefficente dal momento che esegue dei calcoli ripetuti, ad esempio per rispondere alla query precedente calcola _P(j|a)P(m|a)_ per ogni valore di _e_.

![](./immagini/l28-albero.png)

_Nell'albero i pallini rappresentano le operazioni e gli archi rappresantano i valori_

Per limitare il numero di calcoli si può costruire l'albero con un approccio bottom-up, considerando le sommatorie da destra a sinistra ed effettuando i calcoli sono quando è necessario.
In questo modo si riesce facilmente ad individuare il caso in cui ci siano dei sotto alberi uguali.

## Inferenza tramite eliminazione di variabile

![](./immagini/l28-elem.png)

![](./immagini/l28-elem-2.png)

_c'è un esempio nel libro che spiega il prodotto pointwise_

In pratica viene creato un tabellone, con una colonna per ogni variabile da cui dipende il fattore. Ad ogni riga corrisponde un valore e nel caso del prodotto point-wise vengono fatte le moltiplicazioni delle corrispettive righe dei fattori.

L'algoritmo risultante è il seguente:

![](./immagini/l28-elvar.png)

Da notare che l'algoritmo inizia rovesciando le variabili e con i fattori vuoti.

Quando viene trovata una variabile nascosta si esegue il `Sum-Out` della variabile, il quale per ogni valore possibile delle altre variabili, fissa un valore ed esegue la sommatoria dei valori al variare della variabile da sommare.

Come sempre alla fine viene normalizzata la risposta.

## Variabili irrilevanti

Effettuando l'inferenza esatta è possibile che alcune variabili siano irrilevanti per la query.
Dalla topologia di una rete bayesiana si riesca a capire quali sono.

In particolare (**teorema**), la variabile _Y_ è irrilevante a meno che non sia un **antenato** della query _X_ o delle variabili di evidenza.

Una versione alternativa si ottiene con il grafo **moralizzato**, ovvero una rete bayesiana con tutti i genitori "sposati" e con archi non direzionati.

In questo caso si dice che _F_ è **m-separato** da _G_ tramite _H_ se e solo se è separato tramite _H_ nel grafo moralizzato.
In particolare _Y_ è irrilevante se m-separato da _X_ tramite _E_.

L'algoritmo di eliminazione può quindi rimuovere queste variabili prima di valutare la query.

![](./immagini/l28-irr.png)
