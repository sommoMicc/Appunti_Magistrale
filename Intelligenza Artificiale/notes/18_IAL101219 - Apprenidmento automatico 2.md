# Lezione 18 - Apprendimento Automatico 2

## Esempio dell'algoritmo del Perceptron

> Vedi appunti di apprendimento automatico. Nulla di nuovo.

$$
\begin{bmatrix}b\\\vec{w}\end{bmatrix} \cdot \begin{bmatrix}1\\\vec{x}\end{bmatrix} = || \begin{bmatrix}b\\\vec{w}\end{bmatrix} || \cdot || \begin{bmatrix}1\\\vec{x}\end{bmatrix}|| \cdot cos(\theta)
$$

Siccome l'output della funzione $XOR$ non è linearmente separabile, per apprendere l'XOR bisogna usare una rete neurale, ovvero una "catena" di _perceptron_. Per allenare la rete neurale bisogna:

- Definire la funzione da minimizzare (es: scarto quadratico medio);
- Inizializzare il vettore dei pesi con valori random;
- Utilizzare una tecnica (come la discesa di gradiente) per trovare una combinazioni di pesi che approssimino la funzione target.

## Come usare i dati

Tipicamente i dati disponibili vengono divisi in due insiemi, uno che costituisce il training set che viene utilizzato per fare apprendimento e che contiene circa il 70% dei dati.
Il restante 30% viene utilizzato come **test set** per valutare l'ipotesi appresa.

> __IMPORTANTE__: mai usare il test set per l'apprendimento (training)!!

Se l'algortimo di apprendimento prevede degli **iper-parametri** (numero di nodi interni da usare, "velocità" della discesa del gradiente ecc..), il sotto-insieme di training set viene diviso ulteriormente, in modo da ottenere anche il **validation set** che viene utilizzato per provare più valori per gli iper-parametri, in modo da scegliere quelli migliori.

## Errori

L'**errore ideale** $error\,D(h)$ di un'ìpotesi $h$ rispetto ad un concetto $c$ (ovvero $c: X \to \{0, 1\}$, funzione booleana) e la distribuzione di probabilità $D$, ovvero la probabilità di osservare l'ingresso $x \in X$, è la probabilità che $h$ classifichi erroneamente un input selezionato a caso secondo $D$.

$$
error_{D(h)} = Pr_{x \in D} [c(x) \ne h(x)]
$$
L'errore ideale si chiama così perché non si può prevedere: per farlo servirebbe la funzione $c$ che però (ovviamente) non abbiamo, altrimenti non servirebbe fare apprendimento!!

Il numero di errori che un'ipotesi commette classificando gli esempi del training set prende il nome di **errore empirico**. A volte si usa un rapporto tra il numero di errori sul training set e il numero di esempi totali (_accuracy_). L'idea teorica è che se il training set è molto grande l'errore empirico converge all'errore ideale.

Possono però verificarsi dei casi in cui c'è un'ipotesi che commette degli errori sul training set, ma nello spazio completo si comporta correttamente, come può esserci un'ipotesi che non commette errore sul training set ma che commette tanti errori nello spazio completo.

Per questo viene utilizzato il validation set per cercare di trovare l'ipotesi migliore.

Quando un'ipotesi è troppo specifica per un insieme di apprendimento ma ha un errore ideale troppo elevato, si dice che l'ipotesi è **overfit**.
Formalmente: un'ipotesi $h \in H$ è overfit su $Tr$ se $\exists h' \in H$ tale che $error_{Tr}(h) < error_{Tr}(h')$

## VC-dimension

Tanto più lo spazio delle ipotesi è espressivo, tanti più saranno i pezzi in cui viene frantumato lo spazio delle istanze (X). Questa è l'idea della definizioni della **frammentazione** (**shuttering**).

La **VC-dimension** è la cardinalità maggiore del sottoinsieme di $X$ che è frammentato dallo spazio delle ipotesi $H$.

Importante:

- Una ipotesi implica una sola dicotomia: la **VC-dimension** è una caratteristica dell'intero spazio delle ipotesi, non della singola ipotesi;
- Basta avere un unico sottoinsieme frammentato con cardinalità massima: possono esistere sottoinsiemi che non sono neanche frammentabili. E' quindi facile dare un lower bound $lb$ alla VC-dimension (basta trovare un esempio che frammenta lo spazio delle ipotesi in $lb$ pezzi). Tuttavia, è difficile dire qual'è esattamente il valore la VC-dimension dello spazio delle ipotesi: bisogna dimostrare che tutte le ipotesi che frammentano lo spazio in più di x punti non appartengono.

Ad esempio, con un iperpiano in $\R^2$ (quindi una retta) si possono trovare qualche insieme (almeno uno) di tre punti per cui, in qualsiasi modo le etichette (+ e -, o 0 e 1) vengano a loro assegnate, si può tracciare un iperpiano (retta) che li separi.

La _VC-dimension_ è utile perché permette di dare un bound sugli intervalli di confidenza. In pratica, si cerca di capire quanto l'errore empirico rappresenta l'errore ideale. 

[mancano note sulla VC-confidence]

## Structural Risk Minimization

Tanto più complesso è lo spazio delle ipotesi, tanto più è facile minimizzare l'errore empirico. Tuttavia, con un'ipotesi complessa sale la VC-confidence e quindi il bound sull'errore ideale diventa o supera 1 (e risulta inutile). Bisogna trovare un compromesso tra VC-dimension (complessità dello spazio delle ipotesi) e VC-confidence.

L'idea del Structural Risk Minimization è partire da uno spazio delle ipotesi semplice e man mano aggiungere complessità. In questo modo l'errore empirico diminuisce gradualmente, ma allo stesso modo aumenta il bound sulla VC-confidence: facendo la somma $S$ tra questi due valori, trovo lo spazio delle ipotesi che ha valore di $S$ minimo. Per realizzare questa gerarchia, ad esempio, nel caso delle reti neurali basta aggiungere unità nascoste. Il problema di questo approccio è la difficoltà nel calcolare la VC-dimension.

## Apprendimento di Concetti

Un **concetto** su uno spazio delle istanze _X_ è definito come una funzione booleana su _X_.
Ad esempio un concetto _c_ su uno spazio delle istanze _X_ è definito come una coppia _(x,c(x))_, dove _x_ è un esempio nello spazio delle istanze.

Si dice che una funzione _h_ **soddisfa** _x_ se _h(x) = 1_, inoltre si dice **consistente** se _h(x) = c(x)_. Se _h_ è consistente con tutti gli esempi di un training set, allora si dice che _h_ è consistente con il training set ovvero c'è un errore empirico nullo.

Date due ipotesi _hi_ e hj definte su X, si dice che hi è più generale o equivalente a hj se per ogni istanza di X, hj(x) = 1 ==> hi(x) = 1. (hi >=g hj)
Può essere che due ipotesi non siano paragonabili.

### Find-S

Algoritmo per trovare l'ipotesi più specifica e consistente con l'insieme di apprendimento.

Si assume quindi che la funzione che si vuole apprendere sia contenuta nello spazio delle ipotesi.

Assumendo anche che lo spazio delle ipotesi sia quello dei letterali positivi:

1. Viene inizializzata l'ipotesi corrente _h_ con l'ipotesi più specifica, ovvero la congiunzione di tutti i letterali presenti nello spazio delle ipotesi, sia affermati che negati, questa ipotesi è sempre falsa.
2. Per ogni istanza positiva di apprendimento _(x,true)_, si rimuove da _h_ ogni letterale affermato o negato che non è soddisfatto da _x_.
3. Una volta terminate gli esempi si ritorna la versione corrente di _h_.

Il passo 2 cerca di effettuare una **generalizzazione minima** dell'ipotesi.

Il fatto che l'ipotesi sia una congiunzione di letterali affermati o negati rappresenta il bias induttivo di tipo rappresentativo.
In questo caso l'effetto del bias induttivo si vede dopo aver esaminato 3 esempi, perché non si riesce a trovare una generalizzazione minima che riesce a classificare come positivi esattamente 3 esempi distinti.

Find-S è quindi una schema generale di algortimo che si può applicare in vari spazi delle istanze e delle ipotesi, sempre sotto l'assunzione che la funzione da apprendere sia rappresentabile nello spazio delle ipotesi.
Se questo non è garatito allora non si riesce a trovare.

Anche la scelta di ritornare l'ipotesi più specifica fa parte del bias induttivo, dal momento che non c'è un valido motivo per preferire quella più specifica rispetto a quella più generale.
Ci sono altri algortimi come **canditate elimination** che per diminuire questo bias ritorna un insieme di ipotesi consistenti con il training set, tale insieme prende il nome di **version space**. Un tipico utilizzo di un insieme delle ipotesi e quello di utilizzarne più di una per fornire, oltre alla predizione anche un livello di confidenza.
