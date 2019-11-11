# Lezione 7 - Reti neurali
Mercoledì 23 Ottobre 2019

Due sono le motivazioni che hanno spinto la ricerca a studiare le reti neurali:
1. Riprodurre (e quindi comprendere) il cervello umano, cercando di modellarne la struttura in modo affidabile.
2. Estrarre i principi fondamentali di calcolo utilizzati dal cervello replicandone solamente il comportamento, concentrandosi sui principi di calcolo che il cervello utilizza al fne di ripordurre un sistema artificiale in grado di replicarli.
    * L'idea è che non interessa riprodurre fedelmente la struttura del cervello, ma creare un sistema artificiale che ne riproduca le funzioni (magari più veloci ed efficenti) [metafora del volo: all'inizio del '900, i primi esperimenti di volo tentarono di riprodurre fedelmente il volo di un uccello, ma l'aereo che poi fu inventato è radicalmente diverso dall'uccello]

Durante il corso ci concentreremo sul secondo approccio applicato al contesto dell'apprendimento supervisionato.

## Quando usarle?

Quando si hanno tanti input numerici e discreti e si vuole effettuare una classificazione o regressione.

I dati di input possono anche contenere del rumore e la forma della funzione target è totalmente sconosciuta. Quando invece abbiamo conoscenza del dominio (cioè abbiamo un'idea sommaria della forma della funzione target) è stato dimostrato che le reti neurali performano peggio di altre tecniche di apprendimento. In generale le reti neurali si prestano bene ai task sensoriali (riconoscimento di immagini ad esempio).

Il risultato finale non deve essere compreso da un esperto umano, il funzionamento della rete è una black-box.

Tipicamente vengono utilizzate quando non ci sono conoscenze a priori nel dominio ed è accettabile avere tempi lunghi di apprendimento.

## Reti neurali artificiali

![](./immagini/l9-rete.png)

Il cervello umano è costituito da circa $10^{11}$ neuroni fortemente interconnessi tra loro (ogni neurone è mediamente connesso ad altri $10^4$ neuroni), il tempo di risposta di un neurone è di circa 0.001 secondi.

Considerando che per riconoscere il contenuto di una scena un unmano impiega circa 0.1 secondi, ne segue che il cervello umano sfrutta pesantemente il calcolo parallelo: infatti, in questo caso, non pul effettuare più di 100 calcoli seriali ($0.1 / 0.001$).

Questo funzionamento va in contrasto con quello attuale dei nostri processori, i quali ottenogno ottime prestazioni nelle operazioni seriali ma sono in difficoltà con il calcolo parallelo.

Una rete neurale artificiale è un sistema costituito da unità interconnesse che calcolano funzioni numeriche, ci sono vari tipi di unità:

- le unità di input che rappresentano le variabili di ingresso;
- le unità di output che rappresentano le variabili di uscita;
- le unità nascoste che rappresentano le variabili interne che codificano (dopo l'apprendimento) le correlazioni tra le variabili di input relativamente al valore di output che si vuole generare.

Sulle connessioni tra le varie unità sono definiti dei pesi che vengono definiti dall'algoritmo di apprendimeno.

Ci sono due modi per replicare un neurone:

- Hard-threshold
- Sigmoidale

### Singolo Neurone - Perception

![](./immagini/l9-threshold.png)
Dato l'insieme degli iperpiani di $\R^n$, possiamo definirlo come:

$$H = \{f_{w'}(x') = sign(w' \cdot x'): w', x' \in \R\}$$ 
con $w' = [b,w]$ e $x' = [1,x]$
L'idea è quella di avere un vettore di input che rappresenta i nodi di ingresso da ognuno dei quali  arriva un segnale $x_i$. A ogni segnale è associato un peso $w_i$ che lo amplifica, tutti questi pesi vengono definiti dall'algoritmo di apprendimento.

Il neurone è poi composto da altri due elementi: il primo che effettua una sommatoria, detta **net** di tutti i segnali d'ingresso moltiplicati per il loro peso, mentre il secondo utilizza il risultato del primo e calcola una funzione gradino (funzione $sign$ definita precedentemente), il cui output è 1 o -1 in base al segno di net.

Alcune precisazioni:

- Nella sommatoria iniziale gli ingressi vengono rappresentati da $x_1$ a $x_n$, ognuno moltiplicato per il proprio peso. Tuttavia è presente anche un ingresso $x_0$ sempre fisso a 1, al quale viene associato il peso $w_0$, questa componente rappresenta il bais induttivo.
- Possono essere usate altre funzioni gradino oltre a quella del segno.

Si può dimostrare che questo tipo di neurone definisce un iperpiano.
Questo perché la somamtoria a partire da *i=1* può essere vista come un $w^Tx+w_o$ e concide con la definizione di iperpiano. 

Lo scopo del perception è quello di costruire un iperpiano che separi gli input corretti da quelli errati.

### Implementazione di funzioni booleane

Ad esempio Percepton può implementare l'operatore *or* con gli ingressi $x \in \{0,1\}^{n+1}$ (vettori rappresentanti stringhe binarie, che se poste in OR devono restituire come output un numero > 0 se e solo se almeno un valore è non nullo), si possono usare come pesi $w_0' = -0.5$ e $w_i = 1$ per $i=1..n$. Si ottiene quindi un valore positivo in caso ci siano uno o più valori impostati a 1 nel vettore di input $x$.

In modo simile può essere implementato anche l'operatore *and* con $w'_0 = -n+0.5$ e $w_i = 1$ per $i = 1..n$.

Si può anche realizzare l'operatore *not* con una singola connessione e con un unico peso negativo. Ad esempio, $w_0' = 0.5$ e $w_1 = -1$

Un problema che il singolo perceptron non riesce a risolvere è la *xor*, questo perché si tratta di una funzione non linearmente separabili. Ciò non vuol dire che non esista una combinazione di perception in grado di svolgere tale operazione.


### Apprendimento di funzioni linearmente separabili

Si può far apprendere a Perceptron tutte le funzioni linearmente separabili con un algoritmo che è garantito che termini.

Tuttavia se la funzione da apprendere non è linearmente separabile l'algoritmo non converge.

Dato un insieme di apprendimento $S = \{(x,t)\}, x \in \R^{n+1}, \eta \ge 0$, dove $t \in \{-1,+1\}$ è il target (classificazione binaria), $x$ sono i vettori di input e $\eta$ è il learning rate.

1. Inizializza il vettore dei pesi $w$ al vettore nullo (con tutte le componenti a 0, possono anche essere random ma piccole)
2. Ripeti finché non si raggiunge un punto fisso:
    1. Seleziona a caso uno delgi esempi di apprendimento $(x,t)$
    2. Se $out = sign(w * x) \ne t$ (quindi x non viene correttamente classificato perché "non sta dalla parte giusta dell'iperpiano") allora $w \leftarrow w + \eta(t-out)x$

Cioè per ogni esempio nel training set va a controllare il segno del prodotto scalare tra *x* e i pesi, se questo non coincide con il valore di training è necessario adattare *w* in modo che anche per *x* venga calcolato il valore corretto.

In questo modo si riesce ad apprendere una funzione che per costruzione non commette nessun errore nel training set.

Da notare che:
* Non necessariamente un singolo passo di apprendimento riuscirà a modificare il segno dell'input. Tuttavia ogni singolo passo "avvicina" il risultato del perception al Training Set.
* Il learning rate $\eta$ serve per regolare la stabilità ("non violenza") dell'apprendimento: con un learning rate alto le variazioni che subisce $w$ ad ogni passo sono violente.
* Questo algoritmo, se l'insieme di apprendimento è linearmente separabile, è garantito che l'apprendimento del perception converga in un numero di passi limitato.

Piccola precisazione, *x* e *w* sono dei vettori.

END
---

### Sigmoidale


Il vantaggio fondamentale di σ è che si tratta di una funzione derivabile e quindi permette di utilizzare l'algoritmo di **back propagation**. Un algoritmo che permette di fare apprendimento all'indietro in grado di funzionare anche su reti composte da più livelli.

Un'altra caratteristica interessante di questa funzione è che la sua derivata può essere espressa come una funzione dei valori di input. 
Cioè:

> ∂σ / ∂z = σ(z)(1-σ(z))

Questa proprietà tornerà utile quando sarà applicato l'algortimo di back propagation.

Infine, il neurone sigmoidale può utilizza altre funzioni al posto di *1 / (1 + e<sup>-z</sup>)*, come la tangente iperbolica.

## Perceptron

È una rete neurale composta da un singolo neurone con Hard Threshold che viene utilizzata per rappresentare un iperpiano.

L'algoritmo di apprendimento per questa rete cerca dei valori per i vari pesi *w<sub>i</sub>* in modo da apprendere la funzione target.
Per apprendere i coefficenti corretti vengono utilizzati gli esempi del training set.

