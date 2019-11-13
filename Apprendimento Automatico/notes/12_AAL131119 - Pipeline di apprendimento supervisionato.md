# Lezione 12 - Pipeline di apprendimento supervisionato

L'apprendimento supervisionato può essere visto come una serie di fasi:

1. Analisi del problema
2. Raccolta, analisi e preprocessing dei dati
3. Studio delle correlazioni tra variabili
4. Feature selection, definizione dei pesi, normalizzazione
5. Scelta del predittore e del modello
6. Verifica del modello

## Come è possibile rappresentare gli oggetti

Per rappresensentare gli oggetti con i quali lavora un algoritmo di apprendimento è possibile utilizzare varie rappresentazioni:

- **vettori**: come il valore di pressione del sangue, il battito cardiaco, altezza e peso, (Un vettore con dei numeri.
- **stringhe**: Una serie di caratteri che rappresentano un documento o la struttura del DN
- **insiemi e bag**: ad esempio l'insieme di termini che compare in un documento. La differenza tra insieme e bag è che l'insieme contiene oggetti unici, mentre la bag, per ogni oggetto, ne considera anche la cardinalità (numero). La "bag" dei termini che compaiono in un documento indica, per ciascun terminie, il numero di volte che compare
- **array multidimensionali** (_tensori_): come immagini e video
- **albero o grafi**: un documento XML 
- **strutture composte**: ottenute combinando tra loro le precedenti.

Nel corso ci concentriamo principamente sui vettori.

Per ogni oggetto possiamo avere a disponsizione delle **feature categoriche/simboliche**, che rappresentano delle caratteristiche nominali dell'oggetto (marca di un auto, paese di origine), alcune di queste possono essere anche **ordinali**, cioè che impongno un ordine tra gli elementi ma la distanza tra un valore e un altro non è quantificabile, come per esempio i gradi militari: soldato, caporale, ecc. L'anno di uscita in commercio di una macchina è una variabile simbolica se non consideriamo rilevante l'ordine. 

Un altro tipo di feature sono le **feature quantitative**, cioè delle caratteristiche che sono **enumerabili**, come il livello di apprezzamento di un prodotto, oppure **ratio**, ovvero dei numeri reali, come il peso di una persona.

### Mapping Feature categoriche (OneHot encoding)

Le feature categoriche si possono mappare in un vettore con tante componenti quanti sono i possibili valori della variabile (**one-hot**).

> Ad esempio per rappresentare una macchina con le seguenti caratteristiche è possibile utilizzare un vettore che lo codifica.
>
> - Marca: Fiat [c1], Toyota [c2], Ford [c3]
> - Colore: Bianco [c4], Nero [c5], Rosso [c6],
> - Tipo: Economica [c7], Sportiva [c8]
I valori sono inseriti mettendo tutti 0 tranne in corrispondenza dei valori dell'istanza, Quindi si ha che la macchina (Toyota, Rossa, Economica) viene quindi rappresentata con un vettore `[0,1,0,0,0,1,1,0]` (0 Fiat, 1 Toyota, 0 Ford, 0 Bianca, 0 Nera, 1 Rossa, 1 Economica, 0 Sportiva). In generale, il numero di "uni" del vettore sarà sempre uguale al numero di variabili.

### Mapping per feature continue

Tipicamente le feature continue vengono trasformate per ottenere dei valori comparabili con le altre feature.

Per ottenere ciò è possibile applicare una delle seguenti traformazioni:

- **Centramento**: $f(x) = x - E(x)$
- **Normalizzazione STD**: $f(x) = \frac{(x - E(x))}{\sigma(x)}$
- **Rescaling**: $f(x) = \frac{x - x_{min}}{(x_{max}-x_{min})}$

Nota di Taglia: "Le formule ve le guardate a casa" (cit. Aiolli).

Dove:

- *E(x)* è la media di tutti i possibili valori di *x*
- $\sigma(x)$ è lo scarto quadratico medio



### Algoritmo K-NN

**K-Nearest-Neighbors**: è un algoritmo di classificazione in cui un esempio di test è classificato come la classe di maggioranza dei sui *k*-vicini nel training set.

Si vanno a scegliere i *k* elementi più vicini all'elemento che si vuole classificare e viene scelta come classe quella della maggioranza dei suoi *k*-vicini.

Volendo si può normalizzare per perdere volontariamente delle informazioni, in modo da togliere del rumore.

Trattandosi di vettori la distanza deve essere misurata come:

$$||x - y||^2 = ||x||^2 + ||y||^2 - 2x^Ty$$

Per semplificare i calcoli, si può tenere in considerazione che se i due vettori hanno la stessa norma, la loro distanza è uguale alla similiarità indotta dal prodotto scalare:

$$||x - y||^2 = const - 2x^Ty$$

## Feature selection e feature extraction
Sono metodi che dovrebbero ridurre il numero di feature da trattare. L'efficenza di un algoritmo potrebbe dipendere anche dalla dimensione dell'input. Ridurre questa dimensione porterebbe solo giovamento idilliaco. Ovviamente, non bisogna perdere feature importanti in questo processo.

Le due metodologie principali sono:
- **Feature Selection**, consiste nel ridurre la dimensionalità rimuovendo feature non rilevanti o ridondati. Il vantaggio di questo approccio è che, mantenendo le feature originali, il modello rimane interpretabile.
- **Feature Extraction**, secondo cui le feature originali vengono combinate. Problema: si perde l'interpretabilità del modello. Un metodo molto utilizzato per la combinazione delle feature è quello della Principle Component Analysis. 

### Feature Selection
I metodi si possono classificare in 3 grandi famiglie:
- **Filter Methods**, che vengono definiti usando solo il training set (quindi in modo indipendente rispetto al predittore che poi si andrà ad usare). Il funzionamento si basa sull'utilizzo di una funzione di valutazione ("**scoring function**"), che da una misura di utilità (ordinata, cioè dice anche quale è migliore) di un insieme di feature;
- **Metodi Wrapper**: Su vari sottoinsieme di caratterisitche si valutano le performance del predittore. Cioè si prende un sottoinsieme di feature e si danno in pasto al predittore, calcolando poi (con un test-set) una accuracy. In questo caso, come è evidente, si usa il classificatore per stimare la bontà del sottoinsieme di feature scelto (RFE = Recurrent Feature Elimination);
- **Metodi Embedded**: una via di mezzo. Feature Selection e Apprendimento sono fatti contemporaneamente, prendendo una funzione obiettivo e andandola a modificare. Ad esempio, possiamo provare a risolvere un problema con le SVMs, cercando contemporaneamente di *minimizzare* il numero di pesi $w_i \ne 0$ (avere il maggior numero possibile di pesi a 0 permette in pratica di "ignorare" molte feature).

### Feature Extraction
**Principal Component Analysis**: converte un set di istanze con features possibilmente correlate nei corrispondenti valori su un altro insieme di features linearmente non correlate (componenti principali). 

