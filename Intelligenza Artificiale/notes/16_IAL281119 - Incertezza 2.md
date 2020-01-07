# Lezione 26 - Incertezza 2

### Formalmente

![](./immagini/l25-enumerazione.png)

La sommatoria per tutti i possibili valori delle variabili nascoste prende il nome di **marginalizzazione**, e viene effettuata per evitare che l'aggiunta di nuove evidenze porti a delle incosistenze.

Problemi ovvi, descrizione:

1. Nel caso pessimo devo accedere a tutti i valori delle _n_ variabili. Essendo l'inferenza probabilistica un caso particolare dell'inferenza logica, la complessità è analoga.
2. Devo poter tenere in memoria tutta la distribuzione congiunta
3. O la distribuzione è nota a priori oppure vengono utilizzate delle stime. Tipicamente è necessario stimare i dati, ma per riuscire ad avere una stima corretta è necessario avere tanti dati, quindi la complessità spaziale aumenta ancora (multiplo di un'esponenziale).

Non si riesce a migliorare la complessità in tempo, ma con oppurtuni accorgimenti si riesce a migliorare la complessità in spazio.

## Indipendenza

Due variabili sono _A_ e _B_ sono indipendenti se e solo se

> $P(A|B) = P(A)$ oppure $P(B|A) = P(B)$ oppure $P(A\wedge B) = P(A) \cdot P(B)$

![](./immagini/l25-indipendenza.png)

Se fossero tutte dipendendi servirebbe un entry per ogni possibile combinazione di valori (8 della tabella del dentista x 4 valori del tempo), mentre con l'indipendenza del tempo si ottengono due tabelle, una da 8 entry per il dentista e una separata da 4 per il tempo.

In questo caso si parla di **indipendenza assulta** che porta ad avere un notevole risparmio di memoria, tuttavia nel mondo reale le variabili non sono indipendenti.

L'indipendenza assoluta è molto rara.

## Indipendenza condizionale

![](./immagini/l26-indcond.png)

Ovvero alcuni fatti sono indipendenti da altri sotto determinate condizioni.

Quindi nella applicazioni pratiche è possibile utilizzare l'indipendenza condizionale.

La distribuzione della probabilità congiunta si può quindi scrivere come (deriva dall'applicazione della Chian rule):

> **P**(Toothache, Catch, Cavity) = **P**(Toothache | Cavity)**P**(Catch | Cavity)**P**(Cavity)

Servono quindi 2 valori per _**P**(Toothache_ | _Cavity)_, perché una volta fissato un valore di _Cavity_ basta avere un solo valore dal momento che l'altro valore può essere calcolato complementando a 1.

Con questa strategia si riesce a ridurre la dimnesione della rappresentazione della probabilità congiunta da esponenziale a linare.

L'indipendenza condizionale rappresenta la forma più basilare e robusta di conoscenza sugli ambienti incerti.

C'è sempre da tenere a mente che se viene aggiornata la probabilità di un evento, c'è almento un'altra probabilità da aggiornare dal momento che la somma deve sempre essere 1.

## Naive Bayes

Utilizza la regola di Bayes per fare inferenza probabilistica.

![](./immagini/l26-naive.png)

Questo modello prende il nome di naive perché assume l'indipendenza condizionale tra gli eventi che non è sempre vero.

In questo modo per trovare la causa più probabile è possibile calcolare il valore di probabilità per ogni possibile valore della causa trovando così quello più probabile.

### Bayes nel mondo nel Wumpus

![](./immagini/l26-wumpus-1.png)
![](./immagini/l26-wumpus-2.png)
![](./immagini/l26-wumpus-3.png)
![](./immagini/l26-wumpus-4.png)
![](./immagini/l26-wumpus-conti.png)
![](./immagini/l26-wumpus-5.png)

## Riassumendo

Utilizzando il calcolo delle probabilità si ottiene un formalismo per esprimere l'incertezza.

In particolare la distribuzione congiunta delle probabilità specifica la probabilità di ogni evento atomico e grazie a questa distribuzione si riesce ad effettuare l'inferenza tramite enumerazione, andando a sommare i singoli eventi atomici (tenendo anche in considerazione le variabili nascoscoste).

Questa distribuzione può essere rappresentanta in forma tabellare, tuttavia se il dominio applicativo non è banale la tabella risultante è troppo grande, pertanto è necessario prendere in considerazione l'indipendenza tra eventi e l'indipendenza condizionale.
