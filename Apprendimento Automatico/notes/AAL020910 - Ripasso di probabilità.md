#Lezione 2 - Ripasso di probabilità

(Kaggle)[https://www.kaggle.com/], sito che offre sfide con problemi di machine learing sponsorizzati da grandi compagnie.

__Proposta di un progetto di gruppo (opzionale):__ affrontare uno dei problemi proposti da Kraggle per ottenere un bonus sul voto finale.

##Problemi tipici in modo matematico

_Notazione: 
* Ø --> teta, insieme di parametri che rappresenta l'apprendimento (lo so è il simbolo dell'insieme vuoto, ma è semplice da fare)
* X --> insieme di dati su cui applicare l'algoritmo
* Y --> enumeratore (etichette)_

- Classificazione binaria: h(Ø): `X --> {-1,+1}` (_h di teta_, funzione che mappa un dato valore in -1 o +1 (oppure 0 o 1) la funzione _h_ è sempre parametrica, in qunato i parametri rappresentano l'apprendimento (_teta_ Ø));
- Classificazione multiclasse: `h(Ø): X --> Y` con Y che prende come valori un enumeratore o un intervallo di numeri 1..k;
- Regressione: `h(Ø): X --> Reale`
- Ranking di istanze e classi: `h(Ø): XxY --> Reale` dati elementi del prodotto cartesiano tra X (esempio) e Y (etichetta) associa un punteggio espresso da un numero reale. Una funzione che valuta la coppia (x,y) con _x_ valore e _y_ classificazione.
- Novelty detection: `h(Ø): X --> [0,1]` funzione che dato un'esempio mi calcola il fattore di rischio come numero reale da 0 a 1.
- Clustering: `h(Ø): X --> {1,..,k}` funzione che ad un esempio associa una valutazione.
- Associazioni (Basket Analysis): `P(Y|X)`.

##Ripasso di probabilità e statistica

_Evento_: qualcosa che può essere o vero o falso.

La probabilità che si verifichi un'evento è un numero compreso tra 0 e 1, `0 <= P(E) <= 1`. Questo numero può essere calcolato usando la frequenza con la quale si verifica l'evento.

Dato un insieme di eventi E_i mutuamente esclusivi tra loro. La probabilità dell'unione di tutti gli eventi è la somma delle probabilità dei singoli eventi.

La probabilità che si verifichi un evento o il suo complementare è 1. (sempre se gli eventi sono mutuamente esclusivi).

La probabilità dell'unione di due eventi non esclusivi è data dalla probabilità che si verifichi uno o l'altro, meno la probabilità che si verifichino entrambi contemporaneamente.

`P(E unito F) = P(E)+P(F)+P(E intersecato F)`

__Probabilità condizionale__: probabilità che l'evento E accada sapendo che si è verificato l'evento F `P(E|F)`.

L'evento E è indipendente da F se `P(E|F) = P(E)`.

`P(E intersecato F) = P(E|F)*P(F) = P(F|E)*P(E)`

__Formula di Bayes__

`P(F|E) = [P(E|F)P(F)] / P(E)`

Deriva dalla probabilità condizionata, sarà utile nella classificazioni di tipo _bayesiano_ (non sono sicuro che sia scritto giusto).

Dato un insieme di eventi F_i, tra loro esclusivi ed esasutivi (gli Fi coprono tutti i possibili esiti, la propabilità dell'unione di tutti gli F_i è 1).
Allora `E = unione su i (E intersecato F_i)`, la probabilità di E è quindi uguale alla sommatoria della probabilità di tutte le intersezioni.

Il tutto per arrivare a:

`P(F_i | E) = [P(E | F_i)P(F_i)] / sommatoria su j ( P(E|F_j)P(F_j))`

__Valore atteso__: detto anche media, con X e Y variabili aleatorie.

`E[X] = sommatoria su i (x_i * P(x_i))`

`E[aX + b] = aE[X] + b`

`E[X + Y] = E[X] + E[Y]`

`E[g(X)] = sommatoria su i (g(x_i) * P(x_i))`

`E[X^n] = sommatoria su i ((x_i)^n * P(x_i))` detto anche n-esimo momento 

__Varianza__: quanto varia il valore ottenuto attorno alla media dei vari esperimenti.

`sigma^2 = VAR(X) = E[ (X-mu)^2 ]` dove `mu` è il valore atteso. `= E[X^2] - mu^2`.

__Deviazione standard__: o scarto quadratico medio, è la radice quadrata della varianza, ed è la media di quando ci si discosta dal valore attesso.





















