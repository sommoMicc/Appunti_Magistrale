#Lezione 11 - Support Vector Machine 2
Lunedì 11 Novembre 2019


Nelle precedenti puntate:

- Sappiamo che un iperpiano in uno spazio di dimensione m ha VC dimension m+1.
- Si può aggiungere un vincolo di classificazione relativo al margine.
- Per ottenere l'iperpiano con margine ottimo è necessario considerare le ipotesi che minimizza la norma di *w*.
- Il tutto si fa prima con un polinomio di Lagrange e il suo duale.

## Dati non separabili linearmente

Tutto quello visto finora funziona se i dati sono linearmente separabili.

Nel caso questi non lo siano è necessario aggiungere una nuova variabile per ogni elemento presente nel training set.

![](./immagini/l13-non-linear.png)

Vengono quindi definite delle $\xi_i$ che rappresenta la distanza del elemento i-esimo dal margine entro il quale dovrebbe trovarsi.

L'idea è quindi quella di andare a sommare alla funzione costo, un altro quoziente della sommatoria di tutti i $\xi_i$ dei vari esempi presenti nel training set.

Il valore *C* del coefficente che va a moltiplicare la sommatoria degli $\xi_i$ può essere scelta con le tecniche di model selection.

In pratica vengono penalizzati (aumentato il costo) gli esempi che non rispettano il margine.

La funzione $\xi_i$ si comporta anche come upper buond per l'errore della rappresentazione dell'esempoio i-esimo del trainging set.

Sommando le $\xi_i$ di tutti gli esempi è maggiore o ugale al numero di errrori analizzzando tutto il training set. Ovvero $\sum \xi_i$ indica un upper bound al numero di errori che si ottengono nel training set.

Inoltre, *C* può essere visto come una manopola per controllare l'overfitting: all'aumentare del suo valore, aumenta l'aderenza ai dati (quindi il rischio di overfitting). Al suo diminuire, invece, si va più verso un underfitting.

![](./immagini/l13-slack.png)

Allo stesso modo si può trovare il problema duale (non vengono visti i conti)

![](./immagini/l13-cost.png)

Da notare che nel caso separabile i vettori di supporto stanno su uno dei due iperpiani margini.

Nel caso di dati non linearmente separabili o si trovano in un iperpiano margine oppure uno $\xi_i$ negativo.

Da notare che le $\xi_i$ sono variabili del problema primale e che quindi non compaiono nel problema duale.

### Another Approach
Questa strategia per esempi non linearmente separabili non sempre garantisce buone prestazioni perché un iperpiano può solo rappresentare dicotomie dello spazio delle istanze.

Per questo motivio, quando gli esempi non sono lineramente separabili su usa una strategia divisa in due passi:

1. Si mappano i dati di ingresso (input sapce) in uno spazio a dimnesione molto superiore (feature space). Quindi a partire dalle feature degli elementi dell'input space vengono creati nuovi esempi nel feature space che utilizza combinazioni non lineari delle feature del primo spazio.
2. Si calcola poi l'iperpiano ottimo per il nuovo spazio usando la formulazione precedente (che prende il nome di variabili slack).

Perché dovrei farlo?

1. Perché il teorema sulla separabilità di Cover afferma che uno spazio delle ipotesi più grande è più probabile che questo sia linearmente separabile. (Un problema di classificazione complesso, formulato attrvareso una trasfomrazione non linear dei dati in uno spazio ad alata dimensionalità, ha maggiore probabilità di essere linearmente separabile che in uno spazio a bassa dimnsionalità).
2. Perché l'iperpiano ottimo minimizza la VC-Dimension e quindi la capacità di generalizzazione migliora.

![](./immagini/l13-alt.png)

In un modo simile a come accade con il perceptron.

![](./immagini/l13-train.png)

## Funzioni Kernel

![](./immagini/l13-kernel.png)

La cosa bella è che si può "inventare" una funzione K che ci permette di calcolare agevolmente il prododdo scalare.

![](./immagini/l13-kernel-2.png)

![](./immagini/l13-comparsion.png)

## Regressione

Quando si considera il problema di approssimazione di funzioni a valori reali (regressione) si utilizza l'ϵ-tubo: output che differiscono dai valori di target per più di ϵ in valore assolunto vengono penalizzati linearmente, altrimenti non vengono considerati errori.
In partica aggiungo un intervallo di tolleranza al iperpiano che partiziona lo spazio.

![](./immagini/l13-min-primale.png)

che trasformata in duale diventa

![](./immagini/l13-duale.png)

(2019: calcoli evitati a man bassa, slide presentata in 0.2397 secondi)

## Accenno su Funzioni Kernel

![](./immagini/l14-kernel.png)

In pratica la funzione Kernel serve per calcolare un prodotto scalare in uno spazio a più dimensioni.

## Rappresentazione dei dati con i Kernel

Le funzioni Kernel permettono di andare a definire una serie di metodi per l'apprendimento supervisionato.

Ad esempio data una serie di oggetti $S = \{x_1,x_2,.., x_n\}$ può essere rappresentata con i Kernel come una funzione

$$k: X \times X \to R$$

Cioè una funzione che confronta le varie coppie della serie e le valuta utilizzando un numero reale.

Il dataset *S* può essere quindi rappresentato con una matrice simmetrica $K_{i,j} = k(x_i,x_j)$. Inoltre, dal momento che la funzione *k* rappresenta un prodotto scalare su un certo spazio, la matrice *k* è semi-definita positiva (questa realzione vale in se e solo se).


### Vantaggi di questa rappresentazione

La rappresentazione dei dati con matrici kernel ha come vantaggi:

- lo stesso algortimo può essere utilizzato per analizzare dati diveri, quindi tutti gli algoritmi **kernel based** saranno definiti sulla forma della matrice.
- la progettazione dei kernel e degli algortimi è modulare
- risulta più semplice integrare viste diverse di oggetti, non sempre esiste una rappresentazione ottimale dello stesso oggetto, diventa quindi possibile combinare tra loro queste rappresentazioni.
- La dimensionalità dei dati dipente solo dal numero di oggetti e non dalla loro dimensione vettoriale.
- La comparazione tra oggetti può risultare più semplice rispetto ad una loro esplicita rappresentazione.

### Metodi Kernel

Molti metodi kernel, comprese le SVM possono essere interpretati come algortimi che, dato un insieme di oggetti *S* risolvono un problema di minimo di una certa funzione *L* associata al rischio empirico.

### Modularità dei metodi Kernel

I metodi Kernel possono essere rappresentatni da 5 fasi modulari

1. *n*-oggetti
2. definizione della funzione kernel
3. costruzione della matrice *K*
4. applicazione dell'algoritmo su *K* e *Y* (valori target attesi) (ad esempio SVM)
5. produzione dalla funzione

## Kernel Trick

Ogni algoritmo per i dati vettoriali che può essere espresso in termini del prodotto scalre tra vettori può essere implicitamente eseguito nello spazio delle feature associatio ad un determinato kernel, rimpiazzando i prodotti scalari con valutazioni kernel.

1. Kerneliizzazione di metodi lineari o basati su distenze, come il Perceptron e K-NN.
2. Applicazione di algoritmi definiti su vettori a dati non vettoriali, utilizzando dei kernel definiti per dati non vettoriali.

Ad esempio K-NN può utilizzare i kernel per calcolare la distanza tra due vettori.

## Tipologie di Kernel

Per **vettori** si possono utilizzare come kernel:

- **lineare**: *k(x,z) = x \* z*
- **polinomiale**: _k(x,z) = (x * z + c)<sup>d</sup>_
- **gaussiano** (RBF): _k(x,z) = exp(-𝜸||x-z||<sup>2</sup>)_, ha la caratteristica di essere sempre compreso tra 0 e 1.

Il fatto che il kernel sia sempre maggiore di 0, implica che i due vettori sono nello stesso ottante (tra i due vettori c'è un angolo minore di 90°).

Se $k(x,x)$ è uguale a 1 si dice che il kernel è **normalizzato**, ovvero tutti i vettori del feature space sono normalizzati. La matrice kernel definita con un kernel normalizzato ha tutti 1 nella diagonale.

È sempre possibile normalizzare un kernel $k(x,z)$ dividendolo per la radice quandrata di $k(x,x) \cdot k(z,z)$

Come kernel per le **stringhe** si possono contare tutte le sequenze di una cerca lunghezza e costruire un vettore delle feature delle occorrenze, questo si fa con le tecniche di programmazione dinamica.

Per gli alberi si possono utilizzare delle tecniche analoghe, considerando i sotto alberi in comune.

C'è un libro **Kernel Methods for Pattern Analysis** che spiega molto bene questa tecnica.