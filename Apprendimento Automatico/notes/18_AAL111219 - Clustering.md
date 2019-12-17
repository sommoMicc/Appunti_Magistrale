# Lezione 17 - Clustering

Il clustering è il processo che partiziona un'insieme di oggetti in sottogruppi in modo che gli oggetti di questi gruppi siano simili tra loro.

Questa tipologia di apprendimento prende il nome di **apprendimento non supervisionato** dal momento che non vengono calcolate delle etichette e non c'è un supervisore che fornisce delle etichette per i dati di apprendimento.

Il clustering si presta molto bene anche a risolvere il problema di rappresentare per via grafica i dati, grazie ad un raggruppamento di dati "simili". 

Infine, è utile anche nello raggruppare le feature degli esempi: due feature sono simili se tendono ad avere valori simili sugli esempi.

## Il problema del clustering

Tipicamente è composto da:

- Un insieme di esempi, detti anche documenti, $D = \{d_1,..,d_n\}$
- Una misura di similiarità o distanza, decisa da noi. Rappresenta una sorta di _bias induttivo_ dell'algoritmo di clustering
- Un criterio di partizionamento
- Un numero desiderato di cluster $K$ (opzionale: si può pensare an un clustering che non necessiti di questo parametro a priori).

L'algoritmo di clustering calcola quindi una funzione di assegnamento 𝜸 che prende un elemento di $D$ e lo assegna ad un gruppo $\{1..K\}$, in modo che non ci siano cluster vuoti e che venga soddisfatta la misura di similarità.

## Problemi del clustering

Come rappresentare i dati? Anche in questo caso è necessario utilizzare una rappresentazione nel vector space, normalizzando i dati.
Inoltre, la rappresentazione influsce sulla misura di similarità.

Serve poi una notazione per la similarità/distanza, che va decisa a priori e condiziona moltissimo il risultato.

C'è poi il problema di quanti cluster fare, se stabilirlo a priori o sceglierlo in base ai dati, evitando i casi triviali con cluster troppo grandi o troppo piccoli.

## Funzione obiettivo

Tipicamente l'obiettivo di un problema di clustering è quello di ottimizzare una funzione, definendo così un problema di ricerca tra i possibili assegnamenti.

Questi stati sono tanti, $\frac{K^N}{K!}$. Il $K!$ serve per togliere i cluster equivalenti, cioè quando la divisione degli elementi è identica ma cambia "l'etichetta" dei cluster a cui sono assegnati (permutazioni).

Tra l'altro ci sono dei problemi con i minimi locali per la funzione obiettivo, possono essercene tanti e possono impedire di raggiungere un minimo ottimo. Infatti, molto spesso gli algoritmi di clustering sono greedy e partono da un assegnamento iniziale, che man mano verrà raffinato sempre di più (come su _K-means_). Avendo potenzialmente tanti minimi locali, partendo da due assegnamenti iniziali diversi si possono ottenere assegnmenti finali molto diversi!

## Valutazione di un clustering

> Cosa vuol dire fare __BENE__ clustering?

Ci sono dei **criteri interni** che vanno a misurare la similarità tra oggetti della stessa classe (**intra-class**) e tra oggetti di classi diversi (**extra class**), un buon clustering cerca quindi di massimizzare l'intra-class e di minimizzare l'extraclass.

La qualità misurata inoltre dipende da come vengono rappresentati i dati e dalla misura di similirità adottata.

Ci sono poi i **criteri esterni**, l'idea è quella di trovare quanto simile è il clustering trovato rispetto ad una divisione data a priori che prende il nome di **ground truth**.

Si assume quindi che i documenti possano essere partizionati in $C$ classi che rappresentano la ground truth e che l'algortimo di clustering produca *K* cluster, $ω_1 ... ω_K$, ognuno contenente $n_i$ documenti.

La misura più semplice prende il nome di **purity** e rappresenta, per ogni cluster, il rapporto medio tra la classe dominante in quel cluster e la dimensione del cluster. Nell'immagine, in "Cluster 1" ci sono 5 pallini di classe "rosso" (che, essendo quella di numero maggiore, è la classe dominante in quel cluster) su 6 totali.

Dalle slide: purity, the ratio between the dominant class in the cluster $π_i$ and the size of the cluster $ω_i$

Altre misure si basano sull'entropia.

![](./immagini/l17-purity.png)

Nell'esempio il numero di cluster coincide con il numero di etichette è una cosa voluta, ma il gioco funziona anche con un numero diverso di cluster.
**Il core business della situazione è che le etichette per il clustering servono solo per VALUTARLO e non per fare apprendimento**

### Rand Index
Differenza tra rand index e accuracy:

- Nella accuracy guardo se un esempio è nella classe corretta o no
- In Rand Index non si guada il singolo esempio: prendo tutte le possibili coppie di esempi e costruisco una matrice dove calcolo il numero di coppie che sono nella stessa classe nel __ground truth__ e che hanno lo stesso cluster [_A(tp)_]. Il _B_ rappresenta i falzi positivi: coppie nello stesso cluster ma appartenenti a classi diverse nel _ground truth_. I _true negative_ sono quelli che sono classificati in classi diverse e appartengono a classi diverse.

Il RandIndex si ottiene a partire da questa matrice ed è la somma di A + D / (somma di tutto). Quindi è sempre un numero compreso tra 0 e 1 e raggiunge il valore massimo quando i cluster corrispondono perfettamente alla classificazione.

È una misura di similiratà tra cluster, definita come il rapporto tra il numero di elementi che hanno la stessa classe ground e si trovano nello stesso cluster e con classi diverse in cluster diversi, sul numero totale di elementi.

![](./immagini/l17-rand-index.png)

Viene creata una tabella di contingenza, valutando per ogni coppia di punti, se hanno etichette diverse e se sono nello stesso cluster.

I numeri della tabella corrispondo alle coppie che rispondo a quella categoria.

In questo modo ci si riconduce all'accuracy:

$$
RI = \frac{A + D}{A+B+C+D}
$$

Allo stesso modo si possono calcolare **precision** e **recall**

$$
P = \frac A{A+B}\\
R = \frac A{A+C}
$$

## Algoritmi di Clustering

Ci sono due tipologie di algoritmi: 

- **partitional**: che partono da un partizionamento casuale e cercano di migliorarlo iterativamente (K-means clustering, Model based clustering)
- **hierarchical**: che vanno a definire un clustering come un albero in cui la radice contiene tutti gli esempi e man mano che si scende questi vegono partizionati. Si può usare un approccio **agglomerative** che costruisce l'albero in modo bottom-up (permettendo di fissare un numero di cluster), o **divisive** che funziona in top-down, applicando K-mean sulla radice e poi ricorsivamente su ogni figlio, arrivando fino alla foglie che consistono in cluster di un solo elemento.

## K-means

Questo algoritmo appartiene alla categoria degli algoritmi di partizionamento, ovvero vengono partizionati gli *n* documenti in *K* cluster, cercando di trovare un partizionamento ottimo secondo un determinato criterio.

Gli elementi da clusterizzare sono dei vettori con numeri reali e come criterio di partizionamento si utilizza la distanza vettoriale tra gli esempi e il centro del cluster.

Si cerca quindi di creare dei cluster che minimizzano il raggio della ipersfera che contiene gli esempi. (cluster **centroidi**)

La formula da minimizzare è la seguente:

![](./immagini/l17-center.png)

### Algoritmo

1. Si posizionano K punti a caso nello spazio degli oggetti da clusterizzare, questi punti rappresentano i centroidi dei cluster.
2. Si assegna ogni oggetto al centroide più vicino.
3. Una volta completato l'assegnamento si ricalcola la posizione di tutti i centroidi utilizzano la media dei valori di tutti gli oggetti che sono finiti nel cluster.
4. Si ripetono i passi 2 e 3 finché non si spostano più i centrodi.

Questo algoritmo raggiunge un punto fisso. Ovvero, oltre una certa iterazione non si modifica più niente rispetto la precedente.

K-means è dimostrato che converge. Infatti, ogni volta che si effettua il passo 2 la seguente quantità non aumenta, ma rimane stabile o diminuisce:
$$
V(d,\gamma) = \sum_{k=1}^K \sum_{i:\gamma(d_i) = k} ||d_i - c_k||^2
$$

Essendo che, come abbiamo detto prima, ad ogni passo diminuisce, prima o poi convergerà: non può diminuire oltre lo 0, perché è una somma di numeri positivi (in quanto elevati al quadrato).

Resta comunque il problema della scelta del numero di cluster da utilizzare.

## Approcci gerarchici agglormerativi

**quelli disivi utilizzano ricorsivamente k-means**

Costruiscono un dendogramma a partire dagli oggetti, che vengono agglomerati tra loro quando vengono trovati simili.
Si ripete il procedimento finché tutti gli oggetti non vengono agglomerati in un unico cluster.

Si parte quindi da N cluster, uno per ogni esempio e si agglomerano via via finché non si ottiene un unico cluster.

Ad ogni itereazione l'algoritmo può essere interroto per evitare di ottenere un unico cluster.

Le linee verticale di un dendogramma rappresentano un cluster, mentre quelle orizzontali rappresentano un punto di **merge** ovvero quando la similarità di due cluster è tale che vengono uniti in un unico cluster.

![](./immagini/l17-clustering.png)

In base alla misura di similitarità l'operazione può essere **monotona** o meno, cioè se $s_1, ..., s_{k-1}$ sono combinazioni di similarità associate a delle operazioni di merge, allora $s_1 > ... > s_{k-1}$

### HAC - Hierarchical agglormerative Clustering

Prima viene creato un cluster per ogni esempio, dopodiché viene eseguito via via il merge del **clostes pair**, ovvero dei due cluster più simili, fino a che non rimane un unico cluster.
Lo storico dei merge crea il dendogramma.

Per scegliere il **closest pair** di cluster utilizzando vari criteri:

- **single link**: ovvero la distanza minima che c'è tra tutte le coppie di elementi di cluster dirversi
- **complete link**: ovvero la distanza massima che c'è tra tutte le coppie di elementi di cluster dirversi
- **centroid link**: ovvero la distanza tra i dentroidi dei due cluster
- **average link**: la distanza media che c'è tra tutte le coppie di elementi di cluster dirversi

Viene quindi effettuato prima il merge dei cluster con similirità minima.

![](./immagini/l17-dendogram-cluster.png)

Sia single link che complete link garantiscono la monotonia, tuttavia con single link si tendono a creare dei cluster che sono delle *catene*, ovvero si ottengono dei dendogrammi sbilanciati, mentre il complete link tende a dare dei cluster sferici e più compatti, se però ci sono degli esempi **outliers**, ovvero che escono dalla distribuzione.

Il centroid link è carino ma non garantisce la monotonia.

![](./immagini/l17-riassunto.png)

(le complessità della tabella indicano quante operazioni servono per scegliere il closest pair)