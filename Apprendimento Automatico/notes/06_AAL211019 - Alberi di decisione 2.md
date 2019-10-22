# Lezione 8 - Alberi di decisione 2
21 Ottobre 2019

## Bias Induttivo
Ricapitolando, è quell'informazione che unita ai dati storici ci permette di fare apprendimento. Lo avevamo definito come composto da:
* Spazio delle ipotesi
* Algoritmo di apprendimento, che definisce come viene effettuata la ricerca all'interno dello spazio delle ipotesi (metodologie di ricerche diverse possono produrre scelte diverse)

Negli alberi di decisione, lo spazio delle ipotesi è l'insieme dei possibili alberi di decisione che possono essere generati. Questo corrisponde ad un sottoinsieme delle possibili DNF definite sugli attributi delle istanze. In sostanza si assume che la funzione target abbia qualcosa a che fare con questa tipologia di funzione.

Per come è definito ID3, esso è un algoritmo *hill climbing*: esso tenta di minimizzare l'entropia sui nodi, massimizzando di volta in volta l'information gain. Inoltre, partendo dall'ipotesi più semplice, man mano che si procede con l'algoritmo si ottengono alberi di decisione sempre più grandi, espressione di funzioni sempre più complesse, finché non si ottiene una soluzione che "soddisfa" gli esempi. Siccome ci fermiamo non appena troviamo una soluzione, andare a scegliere l'albero più semplice che soddisfa i dati è preferibile. Tuttavia, siccome non procediamo in modalità breath-first ma ci facciamo "guidare" (dall'hill-climbing), vengono preferiti gli attributi ad alto guadagno informativo. In pratica essi, venendo "trattati" prima, sono posti più vicino alla radice.

## Alberi continui
Fino ad ora abbiamo esaminato casi in cui i dati erano discreti. Ma se i dati sono continui? Ad esempio, nel dataset della temperatura, se sostituiamo all'indicatore di temperatura ("HOT/COLD") la temperatura reale (in gradi), si ottiene un dataset continuo.

L'idea è, per un attributo di tipo continuo, definire una soglia in modo da sostituire un valore continuo con un valore binario. Ad esempio, se sono nel nodo iniziale e devo decidere come dividere gli esempi (capendo l'information gain dell'attributo temperatura), prendiamo un qualsiasi valore per l'attributo temperatura (tipo 62), andando a sostituire la temperatura con "falso" se è minore di 62, e "vero" altrimenti. Il problema è ora come decidere la soglia: è stato dimostrato che se ordiniamo i valori in modo crescente, nei nodi in cui avviene un cambio di etichetta ci sono i candidati per i valori soglia ideali.

Una volta trovata la soglia migliore, però, l'attributo potrebbe essere "ritestato" più avanti con un'altra soglia (a differenza del caso discreto, in cui un attributo, una volta fissato, non viene più ritestato).

## Attributi con valori mancanti
Se in qualche dato di training mancano alcuni valori per gli attributi, si potrebbe essere nel gatto. Abbiamo tre soluzioni:
1. Associare il valore dell'attributo più presente nel training set
2. Associare il valore dell'attributo più frequente nel training set il cui target corrisponda
3. Considerare un esempio come se fossero più esempi con pesi diversi: da un'istanza con peso 1 ottengo tre istanze (nell'esempio del tennis) con peso proporzionale alla sua popolarità (calcolata con uno dei due metodi precedenti). 

<strike>
## Dove'è il bias induttivo degli alberi di decisione?

Con **candidate elimination** c'era l'incompletezza delle ipotesi ma la ricerca all'interno dello spazio è esaustiva, mentre negli alberi di decisione, c'è la completezza per quanto riguarda lo spazio delle ipotesi ma la ricerca non è completa in quanto vengono effettuate scelte greedy.

Un altro bias induttivo è che tutti gli attributi che producono un guadagno entropico alto si trovano vicino alla radice.

## Casi speciali

### Attributi continui

Uno o più attributi hanno dei valori continui, escluso il target che rimane binario o con un numero discreto di possibili valori.

La soluzione è quella di trasformare dinamicamente un attributo continuo *A* nell'attributo booleano *A<sub>c</sub>* in modo che sia true se il valore di *A* è minore di una certa soglia *c*.

Il tutto sta ne scegliere la soglia *c* migliore cioè che corrispone al massimo guadagno entropico.

Si è dimostrato che il valore ottimo di soglia si localizza nel valore di mezzo tra due valori a cui corrisponde un target diverso.

Da notare che con ID3 un attributo può essere utilizzato soltanto una volta, in questo caso però è possibile riutilizzare l'attributo con un *c* diverso. 

### Attributi con costi

In alcune situazioni andare a verificare il valore assunto da un attributo potrebbe avere un costo.

Può essere preferibile quindi testare prima gli attributi meno costosi, serve quindi un criterio per la selezione degll'attributo ottimo che tiene conto dei costi.

Alcuni criteri sono:

> **Diagnosi medica** (2<sup>Guadagno(S,A)</sup>-1)/(Costo(A)+1)<sup>*w*</sup> con *w* tra 0 e 1 (più vicino a 1 è *w* più peso si da al costo)
> 
> **Percezione robotica**: (Guadagno<sup>2</sup>(S,A))/Costo(A)

### Attributi con valori mancanti

In alcuni casi si vuole classificare qualcosa che non ha tutti i dati per gli attributi.

Questi casi possono essere trattati in vari modi diversi:

- Utilizzare per *A* il valore più comune nell'insieme d'esempi associato al nodo interno.
- Come prima, solo che vengono considerati solamente esempi con target uguale a quello dell'esempio corrente (ovviamente devo sapere il valore del target dell'esempio corrente).
- Considerare tutti i valori *a<sub>i</sub>* che può assumere l'attributo e la loro probabilità di occorrenza nell'insieme degli esempi associati al nodo interno e andare sostituire l'esempio corrente *(x,target)* con delle istanze frazionarie per ogni possibile valore di *A*, ognuna con un peso pari alla probabilità. Quando devo scoprire il target di un'esempio "provo" con tutti i possibili valori, e poi faccio la media pesata dei valori ottenuti, rispondo come target la classe più probabile.

</strike>

## Overfitting

Cioè l'ipotesi è molto accurata sui valori di training, ma sui valori di test risulta meno accurata (succede quando le ipotesi sono troppo complesse per il fenomeno che si intende rappresentare).

All'aumentare della complessità dell'albero creato, l'accuratezza dell'abero sui dati di training aumenta, ma una volta provata con i dati di test, l'accuratezza cala drastricamente.

```
in fact it can lead to difficulties when there is noise in the data,
 or when the number of training examples is too small to produce a 
 representative sample of the true target function
```

Si è osservato che fino ad un certo livello di complessità l'accuratezza in training è molto simile all'accuratezza in test, è quindi importante **potare** gli albteri complessi.

Ci sono però due problemi:

1. Come si effettua la potatura?
2. Quando fermarsi con la potatura o con l'apprendimento?


Per quanto riugarda il problema (2) ci sono varie soluzioni:

- Valutare le prestazioni sull'insieme di apprendimento usando un test statistico;
- Valutare le prestazioni su un'insieme separato di validazione;
- Usare un principio di **minimizzazione della lunghezza di descrizione (MDL)**: *min_Tree[size(tree) - size(errori(tree))].*

### Come potare

#### Reduce error pruning

Effettuare il pruning di un nodo consiste nel rimuovere il sotto albero che ha origine in quel nodo, trasformando il nodo potato in una foglia e assegnandogli come valore la classificazione più comune tra gli esempi di training associati a quel nodo.

I nodi vengono rimossi solamente se le prestazione dell'albero potato non peggiorano rispetto la versione originale, confrontate sul validation set.

- Dividere il training set in due sottinsiemi, uno per fare training e l'altro per fare validazione.
- Ripetere fino a quando le prestazioni peggiorano:
    - Per ogni nodo interno *n* valutare l'impatto del nodo sul sottoinsieme di valutazione avendo potato il nodo
    - Effettuare la potatura che porta alle prestazioni migliori sull'insieme di valutazione.

Al sottoalbero radicato in *n* si sotistuisce la foglia con etichetta uguale alla classe più frequente nell'insieme degli esempi associati al nodo *n*.

#### Rule-Post pruning

- Si genera una regola $R_i$ per ogni cammino $path(r, f_i)$ dalla radice $r$ alla foglia $i$-esima $f_i$.
- Si effettua la potatura indipendentemente su ogni regola *R<sub>i</sub>*:
    - Si stimano le prestazioni utilizzando solo $R_i$ come classificatore
    - Si rimuovo le precondizioni (una o più) che conducono ad un aumento della stima delle prestazioni utilizzando un approccio greedy.
- Si ordinano le $R_i$ potate per ordine crescente di prestazione (evitando i conflitti)
- Eventualmente si aggiunge come classicazione di default la classe più frequente

$R_i$ è del tipo:

> IF (Attr<sub>i<sub>1</sub></sub> = v<sub>i<sub>1</sub></sub>) ⋀ ... ⋀ (Attr<sub>i<sub>k</sub></sub> = v<sub>i<sub>k</sub></sub>) THEN label<sub>f<sub>i</sub></sub>

La classificazione di una nuova istanza a partire da parte delle regole ordinate avviene seguendo l'ordine stabilito per le regole:

- La prima regola la cui precondizione è soddisfatta dalla istanza è usata per generare la classificazione
- Se nessuna regola ha le condizioni soddisfatte, si utilizza la regola di default per la classificazione, cioè si ritorna la classi più frequente nell'insieme di apprendimento.

Dal punto di vista dell'efficacia, è stato visto che questo metodo funziona meglio del Reduced-Error pruning. Infatti, la trasformazione *Albero $\to$ Regole*, una volta effettuata la potatura, non sono più rappresentabili come albero binario (stiamo cambiando lo spazio delle ipotesi). Le regole ottenute sono anche più facilmente interpretabili da un albero binario.