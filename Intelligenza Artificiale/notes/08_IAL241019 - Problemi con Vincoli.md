# Lezione 8 - Proprietà alpha-beta pruning. Analisi best case. Limite alle risorse. Funzioni di valutazione. Ricerca con taglio. Giochi nondeterministici. Nodi di chance. Potatura per alberi di gioco nondeterministici.  Giochi a informazione parziale. Esempi e analisi corretta.

Giovedì 24 Ottobre 2019

## Limiti alle risorse

Si suppone di avere un limite al tempo per calcolare le mosse.

Serve quindi una **funzione di valutazione** che può essere applicabile sia ad una foglia e in questo caso funziona da funzione di utilità, sia ad uno stato centrale e in questo caso fornisce una stima della *desiderabilità* dello stato in cui si trova, una sorta di funzione euristica.

Serve inoltre un **test di taglio (cutoff)** che pone un limite all'albero di ricerca, raggiunto il quale viene calcolata la funzione di valutazione.

Con il cutoff c'è un problema in quanto può capitare che per raggiungere uno stato molto favorevole è necessario andare a sacrificare dei pezzi, passando cioè per degli stati svantaggiosi. (Ad esempio il sacrificio di un pezzo nel gioco degli scacchi).

Conviene quindi utilizzare una ricerca di **quiescienza** cioè tagliando la ricerca solamente quando la funzione di valutazione per una serie di nodi non cambia di molto.

Se invece tra nodi successivi c'è un cambio notevole tra le funzioni di valutazioni, allora si tengono delle risorse per andare ad esplorare quell'area dell'albero.

### Funzione di valutazione

È una funzione usata per calcolare il valore degli stati.

Negli scacchi la funzione risulta essere un combinazione lineare pesata di varie caratteristiche, come ad esempio il numero di pedine bianche o nere pesate con la loro importanza (es: regina vale 9, torre 8, cavallo 7 ecc..). I pesi possono essere dati all'inizio/staticamente oppure possono essere appresi (tramite machine learning).

La funzione lineare garantisce l'indipendenza del valore di ogni componente, mentre con le funzioni non lineari questo non succede in quanto possono essere considerate coppie di pezzi.

Come per la funzione euristica c'è un trade-off sulla bontà dell'euristica, perché può capitare che sia necessario tagliare prima per avere più tempo a disposizione in modo da poter calcolare un euristica buona, oppure si può scegliere di esplorare più nodi ed avere una stima più grossolana e veloce da calcolare.

Tipicamente si preferisce la profondità.

La cosa importante della funzione di valutazione non è la stima precisa ma la valutazione corretta della "bontà" di uno stato, cioè che la funzione sia monotona, questo perché la funzione deve semplicemente esplicitare il vantaggio di un giocatore piuttosto che dell'altro in modo coerente nel tempo.

Infatti, quello che conta è solamente l'ordine di vista degli stati. 

Il guadagno in giochi deterministici agisce come una funzione di utilità *ordinale*.

### Ricerca con taglio

`MinimaxCutoff` è identico a `MinimaxValue` con la differenza che:

- `Terminal` viene rimpiazzata da `Cutoff`: non arrivo alla fine ma mi fermo ad un certo punto;
- `Utility` viene rimpiazzata da `Eval`: la funzione di utilità viene sostituita con la funzione di valutazione.

#### Benchmark ricerca con taglio:
Siccome possiamo fare al massimo $10^6$ mosse ogni 100 secondi e per ogni turno di scacchi mediamente si possono fare 35 mosse diverse, possiamo fare al massimo *4ply* (mossa, contromossa, mossa, contromossa), che corrisponde al livello di un giocatore pessimo. 
Le prestazioni sono quindi abbastanza limitate/scarse, ma applicando l' $\alpha-\beta$ pruning, si riesce ad arrivare (nel caso migliore) ad *8-ply* con un pc normale, che corrisponde al livello di un esperto. Deep Blue e Kasparov arrivavano ad *12-ply*

La ricerca di quiescenza permette di capire quanto stabile è la valutazione dei nodi che sono sul confine dell'esplorazione.

## Giochi non deterministici

Sono giochi in cui sono presenti degli eventi casuali (*chance*) introdotti mediente dadi, carte prese a caso, lancio in una moneta, ecc. Ad esempio nel backgammon il sottoinsieme di mosse disponibili è dato dal risultato del lancio di due dadi (devo muovere *n* pedine, dove *n* è la somma dei due dadi)

Nei giochi deterministici si riesce a propagare il valore di utilità dalle foglie ai nodi interni, mentre nei giochi non deterministici, a causa del non determinismo, non si riesce ad avere la certezza ma una probabilità. Non si ragiona più in termini di funzioni deterministiche ma di valore aspettato di utilità (che il giocatore deve massimizzare).

Nell'albero viene introdotta una nuova tipologia dei nodi detti *chance* e che Max utilizza per valutare la mossa da fare.

![](./immagini/l10-albero-chance.png)

Il valore aspettato di uno nodo chance dipende dalla probabilità dei vari valori dei figli del nodo chance. L'idea è che il Min cerchi sempre di minimizzare i valori di utilità, che sono però non deterministici (utilità aspettata/attesa). Quando però l'informazione viene passata a *Max*, essa viene "filtrata" dai nodi di chance, che fanno una media pesata delle utilità aspettate che arrivano dai possibili eventi della variabile stocastica. Nell'esempio, risalendo dai due rami più a sinistra, viene passato al nodo max $2 * 0.5 + 4 * 0.5 = 3$. Da notare che un gioco come backgamon che prevede prima il lancio di dadi e poi la scelta delle mosse, inizierebbe subito con un nodo di chance.

!["Esempio backgammon"](immagini/l08_backgammon.png)

La strategia sta quindi nel scegliere le mosse che massimizzano il valore aspettato di utilità.

La presenza dei nodi chance fa aumentare il numero di nodi dell'albero, perché adesso data una mossa di Max ho due o più possibili mosse di Min.

### ExpectMiniMax

Funziona come Minimax con l'eccezione che si devono trattare anche gli eventi casuali.

```
...
if state is a Max node then
    return the highest ExpectiMiniMax-Value of Successors(state)
if state is a Min node then
    return the lowest ExpectiMiniMax-Value of Successors(state)r
if state is a Chance node then
    return average ExpectiMiniMax-Value of Successors(state)
...
```

![](./immagini/l10-valutazione.png)

### Potatura in alberi da gioco non deterministici

Si riesce comunque a fare una potatura 𝜶-𝜷 solo che risulta meno efficace.

![](./immagini/l10-potatura-bound.png)

### Giochi non deterministici in pratica

L'uso dei dadi aumenta il valore del fattore di branching *b* e questo va a riidurre il valore di lookahead (ovvero diminuisce il numero delle mosse future che posso esplorare).

Nonostante la complessità aumenti si riesce comunque ad ottenere dei risultati buoni (sfruttando anche alcune cose non ancora affrontate).

In questo caso è importante che la funzione di valutazione sia composta da trasformazioni (si intende in merito ai veri valori di utilità) lineari e positive, altrimenti non si riesce a preservare l'ordine dei nodi chance. Non è dunque sufficiente che la funzione sia solo monotona (come avveniva invece per i giochi deterministici)!

## Riassumendo i giochi

I giochi sono stati i primi esempi di intelligenza artificiale, si è partiti dai giochi deterministici sfruttando anche lo sviluppo tecnologico.

Le cose si complicano notevolmente quando l'informazione è parziale o il gioco non è deterministico.

L'approssimazione risulta quindi molto importante dal momento che non è possibile raggiungere la perfezione per motivi computazionali.

