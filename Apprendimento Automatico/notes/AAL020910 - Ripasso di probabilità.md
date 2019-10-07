# Lezione 2 - Ripasso di probabilità
Lunedì 7 ottobre 2019

(Kaggle)[https://www.kaggle.com/], sito che offre sfide con problemi di machine learing sponsorizzati da grandi compagnie.


## Problemi tipici in modo matematico

__Notazione__: 
* $\theta$ $\to$ $\theta$, insieme di parametri che rappresenta l'apprendimento
* X $\to$ insieme di dati su cui applicare l'algoritmo
* Y $\to$ enumeratore (etichette)

- Classificazione binaria: $h(\theta): X \to \{-1,+1\}$ (_h di teta_, funzione che mappa un dato valore in -1 o +1 (oppure 0 o 1) la funzione _h_ è sempre parametrica, in qunato i parametri rappresentano l'apprendimento (_teta_ \theta));
- Classificazione multiclasse: $h(\theta): X \to Y$ con Y che prende come valori un enumeratore o un intervallo di numeri 1..k;
- Regressione: $h(\theta): X \to \rm I\!R$
- Ranking di istanze e classi: $h(\theta): X \times Y \to \rm I\!R$ dati elementi del prodotto cartesiano tra X (esempio) e Y (etichetta) associa un punteggio espresso da un numero reale. Una funzione che valuta la coppia (x,y) con _x_ valore e _y_ classificazione.
- Novelty detection: $h(\theta): X \to [0,1]$ funzione che dato un'esempio mi calcola il fattore di rischio come numero reale da 0 a 1.
- Clustering: $h(\theta): X \to {1,..,k}$ funzione che ad un esempio associa una valutazione.
- Associazioni (Basket Analysis): $P(Y|X)$.

## Ripasso di probabilità e statistica

_Evento_: qualcosa che può essere o vero o falso.

La probabilità può essere interpetata come frequenza: ripetendo molte volte un esperimento, la probabilità che il suo risultato sia contenuto in $E$ tende ad un valore costante, che definiamo come $P(E)$

La probabilità che si verifichi un'evento è un numero compreso tra 0 e 1, $0 \le P(E) \le 1$. Questo numero può essere calcolato usando la frequenza con la quale si verifica l'evento.

Un'altra interpretazione della probabilità è come grado di credenza (la probabilità che domani piova).
### Assiomi di probabilità
* $0 \le P(E) \le 1$. Se $E_1$ è l'evento che non può mai succedere, allora $P(E_1) = 0$;
* Se $S$ è l'insieme di tutti i possibili risultati di un esperimento, $P(S) = 1$
* Se $E_i, i = 1...n$ sono eventi mutualmente esclusivi (intersezione vuota), allora $P(\cup_{i=1}^n E_i) = \sum_{i=1}^nP(E_i)$. 
* Se due eventi non sono mutualmente esclusivi, $P(E \cup F) = P(E) + P(F) - P(E \cap F)$.

Dato un insieme di eventi $E_i$ mutuamente esclusivi tra loro, La probabilità dell'unione di tutti gli eventi è la somma delle probabilità dei singoli eventi.

La probabilità che si verifichi un evento o il suo complementare è 1. (sempre se gli eventi sono mutuamente esclusivi).

La probabilità dell'unione di due eventi non esclusivi è data dalla probabilità che si verifichi uno o l'altro, meno la probabilità che si verifichino entrambi contemporaneamente.

$$P(E \cup F) = P(E)+P(F)+P(E \cap F)$$


### Probabilità Condizionale
__Probabilità condizionale__: probabilità che l'evento $E$ accada sapendo che si è verificato l'evento $F$ $P(E|F)$.

L'evento E è indipendente da F se $P(E|F) = P(E)$.

$$P(E \cap F) = P(E|F)*P(F) = P(F|E)*P(E)$$

__Formula di Bayes__

$$P(F|E) = \frac{P(E|F)P(F)}{P(E)}$$

Deriva dalla probabilità condizionale, sarà utile nella classificazioni di tipo _bayesiano_.

Due eventi E, F si dicono indipendenti quando $P(E|F) = P(E)$. L'indipendenza è importante perché quando due eventi sono indipendenti, la probabilità della loro unione $P(E\cap F) = P(E)P(F)$

Dato un insieme di eventi $F_i$, tra loro esclusivi ed esasutivi (gli $F_i$ coprono tutti i possibili esiti, la propabilità dell'unione di tutti gli $F_i$ è 1).
Allora $E = \cup_{i}(E \cap F_i)$, la probabilità di E è quindi uguale alla sommatoria della probabilità di tutte le intersezioni.

Il tutto per arrivare a:

$$P(F_i | E) = \frac{[P(E | F_i)P(F_i)]}{\sum_{j} ( P(E|F_j)P(F_j))}$$

### Media e Varianza

__Valore atteso__: detto anche media, con X e Y variabili aleatorie.

$$E[X] = \sum_{i} (x_i * P(x_i))$$
Le sue proprietà sono:
* $E[aX + b] = aE[X] + b$
* $E[X + Y] = E[X] + E[Y]$
* $E[g(X)] = \sum_{i} (g(x_i) * P(x_i))$
* $E[X^n] = \sum_{i} ((x_i)^n * P(x_i))$ detto anche n-esimo momento 

__Varianza__: quanto varia il valore ottenuto attorno alla media dei vari esperimenti (esempio del bersaglio).

$$ \sigma^2 = Var(X) = E[ (X-\mu)^2 ] = E[X^2] - \mu^2$$
 dove $\mu$ è il valore atteso. Dato che si eleva al quadrato $X-\mu$, la varianza sarà sempre positivo. $E[X^2]$ è il secondo momento (definito qualche riga sopra).

__Deviazione standard__: o scarto quadratico medio, è la radice quadrata della varianza, ed è la media di quando ci si discosta dal valore atteso.
 
### Distribuzioni notevoli
Caso discreto:
* __Bernoulli__: Output 1 o 0 (successo o fallimento), e $p$ è la probabilità di successo. Allora, $P(X=1) = p$ e $P(X=0) = 1-p$. Inoltre, $E[X] = P$ (perchè nella media moltiplico la probabilità per il valore, calcolo che si annulla perché moltiplico per zero quando calcolo $1-p$). La varianza invece è $Var(X) = p(1-p)$
* __Binomiale__: indica una successione di $N$ esperimenti bernoulliani, dove X indica il numero di successi ottenuti nelle $N$ prove. Qual'è la probabilità che questa variabile aleatoria abbia valore $i$ (probabilità che su 10 lanci si ottengano 3 teste)? 
$P(X = i) = \binom{N}{i}p^i(1-p)^{N-i}$. La media $E[X] = Np$ mentre la varianza è $Var(X) = E[X](1-p)$.

Caso reale
* __Uniforme__ nell'intervallo [a,b]. Allora $p(x) = \frac{1}{b-a}$ se $a \le x \le b$ e $p(x) = 0$ altrimenti. $E[X] = \frac{a+b}{2}$ e $Var(X) = \frac{(b-a)^2}{12}$
* __Gaussiana__ di media $\mu$ e varianza $\sigma^2$, $N(\mu,\sigma^2)$: 

$$ p(x) = \frac{1}{\sqrt{2\pi}\sigma} exp(-\frac{(x-\mu)^2}{}$$

## Algebra lineare
### Vettori

* __Somma__ di due vettori A,B: vettore avente come ciascun elemento $v_i = a_i + b_i$ 

* __Prodotto scalare__ di due vettori A,B: $\sum_i a_i b_i$

* __Lunghezza (o norma)__ di un vettore $x$ si denota con $|x|$. La lunghezza al quadrato vale:

$$|x|^2 = \sum_i x_i^2$$

è molto interessante poter esprimere il prodotto scalare rispetto all'angolo presente tra i due vettori.

$$x * z = |x| |z| cos(\theta)$$
Siccome il coseno si annulla quando l'angolo è 90°, due vettori ortogonali avranno prodotto scalare nullo.

### Vettori binari e insiemi
Se abbiamo a che fare con vettori i cui valori $x_i$ appartengono a {0,1}, la lunghezza al quadrato (ovvero la norma) del vettore indica la cardinalità dell'insieme.

### Matrici (da integrare a casa perché latex dio bono)

Somma di due matrici: le matrici A e B devono avere la stessa dimensione, e la matrice somma ha come elementi la somma degli elementi delle matrici.

$$C = [A + B]_{i,j} = [a]_{i,j} + [b]_{i,j}$$

Per fare il prodotto di due matrici è necessario che siano di dimensioni compatibili.
* $A \in R^{m x d}$
* $B \in R^{d x k}$
> L'elemento (i,j) della matrice C = A * B è uguale alla somma del prodotto riga i-esima di a e colonna j-esima di B

La matrice trasposta di una matriche è la stessa matrice "_ribaltata_" sulla diagonale.

> (AB)<sup>T</sup> = B<sup>T</sup>A<sup>T</sup>

Matrice inversa e determinante.

Utilizzando le matrici è possibile risolvere i sistemi lineari.

Una matrice pseudo inversa è un qualcosa di simile ad una matrice inversa per le matrici rettangolari.

> A<sup>+</sup> = A<sup>T</sup>(AA<sup>T</sup>)<sup>-1</sup>

### Autovalori e autovettori (accenno slide 16 ma anche no)

> A * e = lambda * e
> A matrice
> e vettore

`e` è un autovettore della matrice A e `lambda` è il corrispondente autovalore.

**Traccia**: la traccia di una matrice è la somma degli elementi nella diagonale. (detto anche se non c'è nelle slide)

Una matrice si dice **simmetrica** se tutti gli autovalori sono maggiori di 0.










