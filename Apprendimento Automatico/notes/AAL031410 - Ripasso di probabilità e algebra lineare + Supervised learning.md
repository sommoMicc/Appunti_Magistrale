# Lezione 3 - Supervised Learning

##Supervised Learning

Si vuole tradurre un insieme di dati in ingresso *X* in un insieme di dati di uscita *Y*.

Anche in questo caso c'è un _oracolo_ che funziona in modo stocastico e che sceglie un oggetto *x* in *X* secondo una certa probabilità *P(x)* e sceglie *y* in *Y* in base a *P(y|x)*.

L'obiettivo che si vuole raggiungere è quello di approssimare queste probabilità.

Cosa importante, questo oracolo non sempre è una funzione, questo perché può capitare che ad uno stesso *x* corrispondano *y* diversi.

###Operativamente 

Si dispone di una serie di coppie *(x,y)* che seguono lo schema naturale, l'insieme di queste coppie prende il nome di **training set**.

Viene quindi scelta un funzione *h* che prende il nome di **ipotesi**, definita nello spazio delle ipotesi *H* tale che, da valori presenti nell'insieme *X*, restituisca dei valori nell'insieme *Y*.

L'apprendimento consiste quindi nell'andare a scegliere l'*h* migliore in modo che approssimi bene i dati presenti nel training set e che riesca a generalizzare e predirre i corretti valori *y* anche per valori di *x* non presenti nel training set.

Da ciò segue che possono essere commessi due tipi di errori:

- **Errore empirico**: è l'errore commesso da *h* in media, all'interno del training set. In altre parole è l'errore medio dell'ipotesi sul training set.
- **Errore ideale**: è l'errore commesso da *h* su una qualsiasi coppia *(x,y) ~ P(x,y)*, come media su un'insieme infinito di coppie. Questo errore può essere solamente stimato.

Per calcolare una stima dell'errore ideale si può usare un **test set**, cioè un altro insieme di coppie *(x,y)* che non compaiono nel training set. Questa discriminazione è importante perché se così non fosse l'errore ideale sarebbe influenzato dall'errore empirico.

_Riassumendo: l'errore empirico è quello che si fa sui dati che si conoscono, l'errore ideale è quello che si fa su dei dati nuovi._

Dal momento che lo spazio delle ipotesi non può coincidere con tutte le funzioni calcolabili è  necessario fare delle assunzioni sulla funzione oracolo, queste assunzioni prendono il nome di **bias induttivo** e derivano da delle conscenze a priori che abbiamo sul dominio e che vengono utilizzate per fare delle previsioni induttive sui dati.

Fanno parte del bias induttivo:

- Come vengono rappresentati gli esempi;
- Come viene modellato lo spazio delle ipotesi *H*;
- La funzione obiettivo per la ricerca nello spazio *H*, cioè come viene scelta la funzione *h*.

####Es: regressione polinomiale

> TRAIN = {(x<sub>1</sub>,y<sub>1</sub>),...,(x<sub>n</sub>,y<sub>n</sub>)}

Si vuole trovare una funzione polinomiale in grado di approssimare i punti.

In questo caso il bias induttivo è assumere che esista una funzione polinomiale in grado di approssimare i vari punti.

Lo spazio delle ipotesi diventa quindi l'insieme dei vari polinomi e l'apprendimento viene fatto sui vari coefficenti.

Dobbiamo quindi scegliere tra questo spazio un grado *p* che va a limitare i possibili polinomi (definzione di *H*) e i vari parametri della curva (ricerca nello spazio *H*).






























