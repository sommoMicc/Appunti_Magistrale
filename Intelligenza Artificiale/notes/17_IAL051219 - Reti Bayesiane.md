# Lezione 17 - Reti Bayesiane

5 Dicembre 2019

L'idea è quella di andare a rappresentare la distribuzione congiunta delle probabilità sotto forma di un grafo e con delle tabelle più piccole.

Si ottiene così una notazione grafica per rappresentare asserzioni condizionalmente indipendenti.

La sintassi è quindi quella di un grafo con un insieme dei nodi, ognuno dei quali rappresenta una variabile.
Il grafo è diretto e aciclico, dove un arco rappresenta un'influenza diretta (archi diretti, con direzione) tra due variabile.
Per ogni nodo viene calcolata la distribuzione condizionale dati i suoi genitori $P(X_i|Parents(X_i)$.

Nel caso più semplice, la distribuzione condizionale viene rappresentata come una _tabella della probabilità condzionale_ (**CPT**) data la distribuzione $X_i$ per ogni cominazione di valori discreti assunti per i genitori. (Noi non tratteremo il caso continuo

![](./immagini/l27-dentista.png)

Rete bayesiana per il problema del dentista.
Si può notare che c'è un nodo per ogni variabile e la variabile _Weather_ è disconnessa dal momento che è assolutamente indipendente.

## Esempio giocattolo

Un tizio ha un'allarme che può rilevare sia un'infrazione da parte di un ladro, sia da un terremoto. I vicini John e Mary, se sentono l'allarme, chiamano il tizio per avvisarlo.

Variabili (booleane): _Burglar_, _Earthquake_, _Alarm_, _JohnCalls_, _MaryCalls_.

![](./immagini/l27-allarme.png)

_Per motivi di spazio, le variabili vengono abbreviate con le lettere iniziali._

Dal grafo è possibile notare che:

- Ci sono due eventi indipendenti, _Burglary_ e _Earthquake_, e lo si capisce dal momento che non hanno genitori. In questo caso viene utilizzata la probabilità a priori e di conseguenza la CPT contiene un solo valore.
- Le CPT contengo i valori di probabilità che l'allarme scatti, dal momento che per ottenere la probabilità che l'allarme non scatti si può ottenere complementando a 1.
- Se l'allarme potesse assumere _n_ valori (es: _Suona, NonSuona, Intermittente_) sarebbero state necessarie _n-1_ colonne per rappresentare i valori della tabella del nodo _Allarm_.
- La rete modella l'indipendenza condizionale tra le variabili _JohnCalls_ e _Burglary_ dato _Allarm_.

## Compattezza

La distribuzione congiunta completa avrebbe bisogno di $2^n-1$ locazioni di memoria.

Una CPT per variabili booleane $X*i$ con $k$ genitori booelani ha $2^k$ righe per per combinazioni dei vari genitori.
Ogni riga richiede un solo numero, dal momento che l'altro si può calcolare con $1-p$.

Pertanto, se ogni variabile non ha più di $k$ genitori, la rete completa richiede $n \cdot 2^k$ locazioni di memoria.
Cioè l'occupazione cresce in modo lineare anziché esponenziale. (Nella rete precedente sono 10 locazioni contro 31).

Se tutte le variabili sono dipendenti (l'una con l'altra) si verifica il caso pessimo: sono necessari $2^n-1$ numeri/parametri (per 5 nodi, 31 numeri/parametri)

## Semantica globale e locale

La semantica **globale** di una rete definisce la distribuzione congiunta completa espressa come il prodotto delle distribuzioni condizionali locali:

$$P(X_i,...,X_n) = Prod_{[1..n]}(X_i | Parents(X_i))$$

La rete bayesiana rappresenta quindi una fattorizzazione della distribuzione di probabilità congiunta. Se cambia la topologia della rete, cambia anche la fattorizzazione.

La stessa fattorizzazione può essere ottenuta applicando la **chain rule** alla distribuzione congiunta completa e semplificando i vari termini utilizzando la nozione di indipendenza e indipendenza condizionale, secondo quanto speficicato dalla topologia della rete.

Questa rappresentazione oltre ad essere compatta ha anche il pregio di mettere in evidenza le relazioni causa/effetto tra le variabili.

La semantica **locale** riguarda l'indipendeza condizionale tra un nodo e i suoi non discenti dati i genitori.

![](./immagini/l27-locale.png)

Quindi, se conosco il valore dei genitori del nodo _X_, il nodo _X_ è condizionalmente indipendente dai nodi _Z_.

Questa definizione non comprende tutte le relazioni di indipendenza condzionale. Una definzione più approssimata è quella della **Markov blanket**

![](./immagini/l27-markov.png)

Ovvero, ogni nodo è condizionalmente indipendente da tutti gli altri dato il suo **markov blanket**: genitori, figli e genitori dei figli.

Ricapitolando:

- Semantica globale --> distribuzione congiunta completa
- Semantica locale --> indipendenza condizionale tra un sotto insieme di nodi

## Complessità dell'inferenza esatta

Non avendo quantificatori e/o variabili, si fa riferimento alle regole di inferenza in Logica Classica Proposizionale (LCP), in cui il problema di inferenza è co-NP-completo.

Le considerazioni precedenti portano ad un miglioramento all'efficenza, ma nel caso pessimo, il tempo di esecuzione è comunque esponenziale.

Più nel dettagli, se una rete è **singolarmente conessa**, ovvero ogni coppia di nodi è connessa da al più un cammino (non diretto) il costo in tempo per l'algoritmo di eliminazione di variabile è $O(d^k \cdot n)$.

Nel caso di reti più che connesse singolarmente, il problema di inferenza può essere ridotto a 3-SAT, pertanto si tratta di un problema NP-hard.

Fare inferenza essata è tipicamente costoso.
Tipicamente si preferisce trovare un'ordinamento per le azioni in modo da scegliere quella migliore e pertanto basta avere una relazione d'ordine piuttosto che il valore essatto.

## Inferenza tramite simulazione stocastica

L'idea di base è:

1. Estrarre _N_ campioni da una distribuzione di campionamento _S_
2. Calcolare la probabilità a posteriori approssimata _P'_
3. Mostrare che converge alla vera probabilità _P_, ovvero aumentando il numero di campioni, il risultato converga al valore della probabilità.

**Nota del 2019**: _Campionamento di una rete vuota, Rejection Sampling, Likelihood weighting, MCMC **solo accennate**. Le riporto qua sotto copiando dagli appunti vecchi, che sono anche troppo esaustivi!!! **Attenzione**_

## Campionamento da una rete vuota

Con rete vuota si intende che nessuna variabile è istanziata con un valore.
C'è una rete bayesiana con un nodo per ogni variabile e gli archi che rappresentano le relazioni con i genitori. Si hanno inoltre a disposizione le tabelle di probabilità condizionale per ogni nodo.

Per generare un campione si parte dai nodi che non hanno genitori, creando devi valori per quel nodo, seguendo la loro distribuzioni di probabilità.

Una volta generati i campioni, si fissano i valori e si considera il resto della rete, generando il resto del campione utilizzando le probabilità condizionali.
Terminato ciò si ritorna il campione generato.

**Rete vuota:** rete che non considera evidenza, ovvero le cui variabili non sono assegnate.

![](./immagini/l29-priorsample.png)

![](./immagini/l29-prior-example.png)

Vengono quindi generati tanti esempio che vengono poi utilizzati per stimare la distribuzione di probabilità congiunta.
Di conseguenza se un determinato campione compare più volte, maggiore è la sua probabilità di comparire.

_S<sub>PS</sub>(x<sub>1</sub>, ..., x<sub>n</sub>)_ è la probabilità che venga generato un determinato evento.

![](./immagini/l29-ps.png)

## Rejection Sampling

Si vuole stimare la probabilità a posteriori data una certa evidenza, pertanto si usa `PriorSample` per generare i vari campioni, e vengono scartati tutti i campioni che non concordano con l'evidenza.

I campioni rimanenti vengono utilizzati per stimare la probabilità di un determinato valore per la variabile query.

![](./immagini/l29-rejection.png)

_X_ sono le variabili di query, **x** è il campione generato, _x_ è il valore della query _X_ per l'esempio **x**.

![](./immagini/l29-rejection-t.png)

Se la probabilità dell'evidenza è bassa, vengono generati pochi campioni consistenti con l'evidenza, pertanto per raggiungere un risultato significativo è necessario generare molti campioni.

## Likelihood weighthing

Per evitare il problema di rejection sampling, vengono fissati i valori per le variabili di evidenza, in modo da generare solo campioni consistenti.
Ogni campione viene poi pesato con la likelihood accordata dall'evidenza, altrimenti si perderebbe la consistenza con la distribuzione di probabilità a priori.

Il peso iniziale viene fissato ad _1_, dopodiché per ogni variabile di evidenza fissata, viene moltiplicato il peso per la probabilità di ottenere quel determinato valore di evidenza, dato il valore dei genitori del nodo.

![](./immagini/l29-weight.png)

![](./immagini/l29-likelihood.png)

In questo caso si va a stimare la probabilità delle variabili che non hanno evidenza _S<sub>WS</sub>(**z**,**e**)_, così facendo si tiene in considerazione solamente l'evidenza degli antenati, mentre il peso per un dato campione _w(**z**,**e**)_ rappresenta la probabilità dell'evidenza per le variabili fissate.

![](./immagini/l29-asd.png)

Utilizzando questa strategia si generano solamente campioni consistenti con le variabili di evidenza, in un modo più efficente rispetto alla versione precedente, tuttavia se le variabili di evidenza sono tante la stima della probabilità diventa meno accurata.

## Inferenza approssimata tramite MCMC

- Rejection sempling genera tanti campioni e butta via quelli non consistenti
- Likelihood weighting genera solo campioni consistenti con l'evidenza, ma è necessario tenere traccia di un peso. Inoltre per generare un campione si riparte da capo.

Markov Chaining Monte Carlo genera dei campioni modificando il campione corrente, andando a cambiare in valore di una variabile, rispettando comunque il valore di probabilità della variabile.

L'algoritmo inzia creando un campione randome per le variabili **Y**, dopodiché, viene calcolata la distribuzione di probabilità andando ad creare nuovi campioni cambiando il valore delle variabili per cui non si ha evidenza considerando la distribuzione di probabilità dalla dalla **Markov blanket** della variabile che si vuole aggiornare.

**c'è un pacchetto di slide alternativo che non è condiviso con il pseudo-codice dell'algoritmo e un'esempio**

Per stimare **P**(_Rain_|_sprinkler_,_wetgrass_) viene campionato _Cloudy_ e _Rain_ considerando il loro Markv blanket, tenendo conto di quanti campioni generati hanno _Rain_ vero e quanti ce falso.

Supponendo di creare 100 campioni, 31 dei quali con _Rain_ vero, la distribuzione risulta **P**(_Rain_|_sprinkler_,_wetgrass_) = _<0.31,0.69>_ ovvero la normalizzazione dei campioni ottenuti.

...convergenza al cammino...

Il campionamento utilizzando il Markov blanket risulta facilmente implementabile in modo parallelo.

Ci sono però dei problemi computazionali legati al riconoscere se è avvenuta la convergenza e legati alla dimensione del Markov blanket.

... cose, probabilità, altre cose ...

... vedi libro, sia seconda che terza edizione ...

## Riassumento

L'inferenza esatta tramite l'enumerazione di variabili è polinomiale sui polialberi (reti singolarmente connesse) ma NP-Hard in generale. Se i domini delle variabili sono grandi, il calcolo può essere oneroso.

Per fare inferenza approssimata risulta migliroe con Likelihood weigthing e MCMC.
LW è indipendente dalla topologia, ma si comporta male nel caso ci sia molta evidenza.
La convergenza piuò essere lenta per le probabilità vicine a 1 o 0. Si possono trattare cominazioni arbitrarie discrete e continue

----- ROBA NON FATTA ----------

## Costruzione di una rete bayesiana

![](./immagini/l27-build.png)

Una volta fissato l'ordinamento e un nodo Xi, l'insieme _Parent(X_i)_ deve essere un sotto-insieme delle variabili _X<sub>1</sub>...X<sub>i-1</sub>_. Le _X<sub>j</sub>_ mancanti derivano dall'indipendenza condizionale tra le variabili _X<sub>1</sub>...X<sub>i-1</sub>_.

La costruzione richiede sempre e comunque un tempo esponenziale perché deve considerare tutte le possibili cominazioni per verificare l'indipiendenza condizionale.

Resta da definire come ordinare le variabili e come stimare i dati mancanti.
Entrambi possono fornire da un esperto che conosce il dominio applicativo.

La scelta dell'ordinamento influenza notevolmente la dimensione del grafo. Ordinare le variabili mettendo prima le cause e poi l'effetto porta ad avere una rete più compatta rispetto all'ordinamento inverso.

Ad esempio, utilizzando come ordinamento _M, J, A, B, E_ si ottiene la rete seguente che richiede 13 numeri per essere rappresentata.

![](./immagini/l27-bad.png)

## Compiti di inferenza

Con una rete bayesiana è possibili calcolare la probabilità a posterirori marginale **P**(X_i|E=e) e congiuntive **P**(X_i,X<sub>j</sub> | E=e), riducendole ad una serie di query semplici (scomponendola con la regola del prodotto).

È possibile inoltre utilizzare una rete per prednere decisioni ottimali del tipo P(outcome|action, evidence).

Allo stesso modo si possono fare delle meta-query, ovvero ricavare informazioni su quali variabili influenzano maggiormente la distribuzione di probabilità, ovvero quale evidenza mi conviene cercare.

-- FINE ROBA NON FATTA --

## Cenni di Apprendimento Automatico

Per risolvere alcuni problemi non è possibile applicare un approccio algoritmico tradizionale, per vari motivi, come l'impossibilità di formalizare il problema, il rumore sui dati o l'alta complessità nel formulare una soluzione. Sennò ci sono dei casi in cui si riesce a formalizzare un problema ma non si ha idea di come risolverlo.

Per poter utilizzare questo approccio sono necessari:

- **Dati**: più ce ne sono meglio è, possono essere ottenuti in blocco, una volta per tutte o man man interagendo con l'ambiente.
- **Conoscenza**: avere informazioni sul dominio applicativo permette di ottenere algoritmi più efficenti, anche in caso di informazioni incomplete o imprecise.

Si vuole quindi utilizzare i dati per ottenere una nuova conosscenze o raffinare quella di cui si dispone.

Ci sono 3 paradigmi principali di apprendimento:

- Supervisionato
- Non supervisionato
- Con rinforzo

### Apprendimento supervisionato

Dato un insieme di esempi pre-classificati {_(x, f(x))_}, apprendere una descrizione generale che incapsula l'informazione contenuta negli esempi, cioè per trovare delle regole che sono valide su tutto il dominio di ingresso.

La descrizione così ottenuta deve poter poi essere utilizzata per fare predizione su nuovi dati del dominio d'ingresso.

Il supervisionato deriva dal fatto che ci sia un esperto che supervisioni l'algortimo e cioè che fornisca il valore della funzione target per alcuni esempi.

### Apprendimento non supervisionato

Dato un insieme di esempi _Tr = {x}_ si vogliono estrarre delle regolarità e o pattern sui dati che siano valide per tutti gli elementi del dominio di ingresso.

Non esiste nessun supervisiore che fornisce una classificazione dei dati, ma si cerca di raggruppare tra loro dei dati simili (_clustering_) e di scoprire nuove regole.

Un esempio di questa applicazione è il data mining su database strutturati come quelli medici o commerciali.

### Apprendimento con Rinforzo

In questo caso è presente un agente che opera all'interno di un ambiente. L'agente si trova in un determinato stato _s_ e può eseguire una certa azione _a_ tra tutte le azioni possibili per il determianto stato. Quando l'agente esegue l'azione, l'ambiente fornisce all'agente lo stato successivo e una ricompesta _r_ che può essere posivita, negativa o neutra.

Lo scopo dell'agente è quello di massimizzare una funzione delle ricompense tramite una politica di scelta delle azioni. Di fatto, è una via di mezzo tra l'apprendimento supervisionato e non supervisionato, perché se è vero che ho un feedback sull'azione, è anche vero che il valore della ricompensa non è un valore assoluto, quindi non permette **a priori** di sapere il valore dello stato in cui ci si trova!!

## Elementi fondamentali dell'apprendimento supervisionato

L'elemento principale sono i dati, senza i dati non è possibile fare apprendimento.

Serve poi uno spazio delle ipotesi _H_, cioè l'insime delle funzioni che possono essere realizzate dal sistema di apprendimento. Si assume quindi che la funzione da apprendere _f_ possa essere rappresentata da un ipotesi _h_ presente in _H_.

Ma come si fa ad avere la certezza che _H_ contenga _h_? In questo caso torna utile la conoscenza a priori, avere delle informazioni riguardo _f_ permette di scegliere un'insieme _H_ più adeguato.

L'algoritmo di apprendimento può essere quindi visto come un algoritmo di ricerca nello spazio delle ipotesi _H_.

Da notare che _H_ non può coincidere con l'insieme di tutte le funzioni possibili e allo stesso tempo avere una ricerca esaustiva. In questo caso l'apprendimento è inutile dal momento che la ricerca su uno spazio così grande è troppo onerosa, inoltre in uno spazio infinito di funzioni c'è sempre un numero infinito di funzioni che approssimano i dati di apprendimento. In pratica, rischio di trovare una funzione che esprime in maniera diversa i dati di apprendimento, ma non aggiunge nessun valore (ad esempio, non permette di fare predizione).

Si parla quindi di **bias induttivo**, cioè di vincoli che si vanno a porre sulla rappresentazione delle funzioni o sulla strategia di ricerca. Se si hanno delle conoscenze a priori è possibile avere un bias induttivo molto forte e corretto, limitando così lo spazio di ricerca senza escludere la soluzione.

**_seguono degli esempi di spazi delle ipotesi uguali a quelli visti ad apprendimento automatico_:**

- Iperpiani in $\R^2$

### Tipi di algoritmi

Algoritmi **eager**, sono algoritmi che raccolgono tutti i dati di apprendimento e lavorano molto sull'apprendimento della funzione, richiedono quindi tanto tempo per trovare un ipotesi _h_, però effettuano la predizione in poco tempo.

Mentre gli algoritmi **lazy**, ricercano un'ipotesi on-demand, cioè i dati di apprendimento vengono valutati solamente quando viene richiesta una predizione.
