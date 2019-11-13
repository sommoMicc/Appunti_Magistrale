## Fase 5 - Scelta del predittore e del modello

I parametri sono i valori che influiscono nell'apprendimento, come i vari pesi *w*. Mentre, gli **iper-parametri** sono tutti gli altri parametri che non influiscono con l'apprendimento, come il numero di unità nascoste per le reti neurali o il *k* per l'algoritmo k-nn.

La fase in cui questi valori vengono scelti prende il nome di **model selection** e come valori si cerca di scegliere il migliore per il task.

###Bias e varianza

Per valutare le predizioni di uno stimatore vengono utilizzate due misure:

- **bias**: che misura la distorsione di una stima quando lo stimatore è corretto
 
> b = E[𝜃'] - 𝜃 

- **varianze**: che misura quanto si disperde la stima.

> v = E[(𝜃' - E[𝜃'])^2]

Nelle formule sopra riportate *𝜃* rappresenta il valore corretto e *𝜃'* rappresenta il valore prodotto dallo stimatore.

###Hold out

Una strategia per ricercare il valore ottimo per un iper-parametro è quella dell'**hold out**, ovvero per ogni possibile valore un valore per l'iper-parametro si fa eseguire l'apprendimento allo stimatore su un sotto-insieme del training set, dopodiché si confrontano i risultati ottenuti effettuando delle predizioni su un insieme di validazione, ovviamente viene scelto il valore dell'iper-parametro che porta ad ottenere le predizioni migliori.

Più formalmente:

1. Si sceglie un piccolo sottoinsieme *Tr* del training set che viene utilizzato come set di validazione *Va*.
2. Il classificatore (algoritmo) apprende utilizzando gli esempi in *Tr* ma senza usare quelli che compaiono in *Va*.
3. Si osserva come si comporta il classificatore con un determinato valore dell'iper-parametro, e si ripete a partire dal punto 2 per tutti i possibili valori dell'iper-parametro.

In questo modo riesco a calcolare l'*accuracy* per ogni valore del iper-parametro e di conseguenza posso scegliere il valore migliore.

Con l'**accuracy** si intende la proporzione di predizione corrette effettuate dallo stimatore.

Una volta scelto il valore, tipicamente si rieffettua l'apprendimento utilizzando il training set completo.

###K-fold Cross Validation

Alternativa all'hold-out che permette di valutare in modo più preciso la bontà dei possibili valori per un iper-parametro.

L'insieme di apprendimento viene partizionato in *k* parti disgiunte.
Viene poi eseguito l'apprendimento utilizzando *k-1* partizioni e utilizzando la restante partizione per fare validazione.
L'intero processo di apprendimento viene ripetuto quindi *k* volte, utilizzando ogni volta una partizione per la validazione diversa.

Così facendo per un singolo valore di un iper-parametro si ottengono *k* valori di accuracy e si può utilizzare la media di queti valori per ottenere una stima dell'accuracy migliore.

Il tutto viene poi ripetuto per ogni possibile valore dell'iper-parametro. 

Il valore di *k* influisce la dimensione del training set, utilizzando un *k* piccolo, si ottiene un training set più piccolo, quindi il bias induttivo aumenta e la varianza della stima ottenuta diminuisce.

Viceversa, se *k* è grande, il training set è più grande e si ottiene un minor bias induttivo.

Tipicamente si usa *k=5* o *k=10*.

### Valutazione per dati non bilanciati

Quando nel training set c'è una classe che domanina sulle altre, l'accuracy non è più una stima adatta, vengono quindi utilizzate altre misure quali: **precision**, **recall** e **F-Measure**.

- **Precision**: (π) misura quante volte, quanti tra gli esempi classificati come positivi sono effettivamente positivi

> π  = true positive / (true positive + false positive)

- **Recall**: (p) misura quanti che sono effettivamente positivi sono stati classificati come positivi.

> p = true positive / (true positive + false negative)
 
**Precioson**: quanti tra quelli che ho detto essere positivi sono effettivamente positivi.

Un'altra misura più accurata è la **F-measure** che combina tra loro precision e recall:

> F<sub>1</sub> = 2 πp / (π + p)
> 
> F<sub>𝜷</sub> = (1+𝜷^2)πp / (𝜷^2π + p)