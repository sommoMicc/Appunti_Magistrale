# Lezione 4 - Rircerca informata (A* in poi)

### Ricerca su grafo

Al posto di creare un albero con la replica degli stati si va a sostituire l'albero con un grafo dove i nodi rappresentano gli stati e gli archi sono dati dal collegamento dei due stati.

```
function RicercaGrafo(problema,frontiera) returns una soluzione o il fallimento
	chiuso = insieme vuoto //insieme dei nodi già esplorati
	frontiera = Inserisci(CreaNodo(StatoIniziale[problema])),frontiera)
	loop do
		if Vuoto(frontiera) then return fallimento
		nodo = RimuoviPrimo(frontiera)
		if TestObiettivo[problema](Stato[nodo]) then return Soluzione(nodo)
		if Stato[nodo] non è in chiuso then
			aggiungi Stato[nodo] a chiuso
			frontiera = InserisciTutti(Espandi(nodo,problema),frontiera)
	end
```

## Ottimalità di A* su un grafo

la stessa prova di A\* su un albero non va bene per il grafo.

![](./immagini/l4-esempio-fail-astar.png)

Nell'esempio del grafo, il nodo $A$ viene prediletto rispetto a $B$ perché ha un valore $f(A)$ minore rispetto a $B$. Inoltre, quando $A$ viene espanso, in  cima alla coda (con priorità) dei nodi di frontiera viene messo $C$, perché ha valore $f(C) < f(B)$. $C$ quindi viene espanso, rimosso dalla frontiera e aggiunto alla lista dei nodi esplorati. Ecco perché, quando si espande anche $B$, $C$ non viene più modificato, perché non appartiene più alla frontiera.

La condizione che $h$ sia ammissibile (deve sottostimare il costo effettivo) non è sufficiente.

Le eristiche devono essere anche **consistenti**, ovvero:

$$h(n) \le c(n,a,n') + h(n')$$

Il valore della funzione euristica calcolata per $n$ deve essere minore o uguale della funzione euristica di $n'$ sommata al costo per spostarsi da $n$ a $n'$ (disuguaglianza triangolare).

In questo modo si ottiene una funzione di valutazione $f$ non decrescente. Nota: tutte le euristiche _consistenti_ sono __ammissibili__!

A\* espande i nodi in ordine di valore rispetto alla funzione di valutazione dei nodi.

## Proprietà di A\*

L'algoritmo è **completo** a meno che non ci sia un numero infinito di nodi con la funzione di valutazione minore e uguale della funzione di valutazione dello stato di goal.

Il tempo di esecuzione è in ogni caso esponsenziale in quanto è necessario andare ad espandere tutti i nodi che hanno la funzione di valutazione più piccola del nodo di goal. Tuttavia, se la funzione euristica fa una buona stima, si arriva prima alla soluzione.

Nel caso pessimo è necessario avere memoria per tutti i nodi del problema.

L'algoritmo però è **ottimo**, in quanto non può espandere un nodo che ha un determinato valore della funzione di valutazione finché non sono stati espansi i nodi con funzione di valutazione minore. Nello specifico, $A*$ può espandere solo alcuni nodi con $f(n) = C^*$ (dove $C^*$ è il costo della soluzione ottima), perché essi potrebbero essere prima del nodo goal nella coda di priorità. Alla fine però, tutti questi nodi verranno espansi, quindi rimossi dalla coda, e si arriverà ad estrarre il nodo goal.

L'algoritmo non è solamente ottimo, non esite algoritmo che trova la soluzione ottima espandendo meno nodi rispetto ad A\*.
Questo perché se un altro algoritmo esplorasse meno nodi allora rischierebbe di andare a scartare dei nodi che potrebbero essere ottimo. (I due algoritmi devono però avere la stessa euristica, altrimenti le cose cambiano).

Il limite di A* è sempre quello dell'utilizzo di memoria. Ecco che, per provare ad ovviare il problema, è presente un algoritmo chiamato IDA\*

### IDA\*
L'idea dell'algoritmo è quella di adottare la tecnica dell'iterative deepening (aumento di profondità di esplorazione iterativa) alle euristiche.

Non inserisce nella coda dei nodi con valore di $f$ maggiore di un certo valore _cutoff $f$_.

Questo valore di _cutoff f_ alla iterazione successiva viene posto uguale al minimo valore di *f* dei nodi non inseriti in coda.

(Ad ogni iterazione prendo il nodo di che non ho inserito in coda e con funzione di valutazione minima e assegno a _cutoff_ il su f-valore, in questo modo quel nodo verrà preso in cosiderazione alla prossima iterazione dell'algoritmo)

Viene così limitato l'uso della memoria.

Ad ogni aggiornamento di _cutoff_ devo comunque reiniziare la ricerca da capo.

_Possibile tema di progetto: utilizzo di A\* e IDA\* per la risulzione di 8-puzzle_

Esistono comunque soluzioni migliori: RBFS, MA\*, SMA\*.

## Ricerca Best First Ricorsiva - RBFS

Algoritmo che imita una ricerca in profontidà utilizzando uno spazio lineare, sempre andando a considerare la funzione di valutazione come A* (costo per raggiungere quel nodo + stima distanza da goal).

Invece di seguire indefinitamente il cammino corrente, tiene traccia dell'*f-valore* del miglior cammino alternativo che parte da uno degli avi.

Se il nodo corrente supera l*'f-valore* (valore della funzione di valutazione), la ricorsione torna indietro al cammino alternativo.

Durante il ritorno, si sotistuisce l'*f-valore* di ogni nodo lungo il cammino con il miglior *f-valore* dei suoi nodi figli. Questo perché, durante la ricerca, si ottengono stime sempre più realistiche di $f$ (perché esso era composto anche dall'euristica, che sottostima!). Quindi, la stima del nodo figlio è migliore di quella del padre: posso quindi riportarla e "farla salire".

Come per A\*, la ricerca è ottima se la funzione euristica è ammissibile.

La complessità spaziale è lineare ma la complessità temporale è difficile da definire, nel caso pessimo è sempre esponenziale e maggiore di A*, perché si è risparmiato in memoria (__tradeoff spazio-tempo__).

Anche questo algoritmo soffre di un problema simile ad IDA\*, cioè non usano tutta la memoria a disposizione. Sono stati proposti allora _MA*_ e _SMA*_, che sfruttano al meglio la memoria disponibile.

> Martedì 15 ottobre 2019

### SMA*
Di fatto, SMA* procede come A* (espandendo la foglia migliore candidata) finché ha memoria disponibile. In quel momento, A* normale si bloccherebbe, mentre SMA* si crea spazio all'interno della frontiera cancellando dalla memoria un nodo _vecchio_ per far posto ad un nodo _nuovo_: nella pratica viene scartato il nodo foglia peggiore, quello con l'*f-valore* più alto. Tale valore viene riportato sul nodo padre, per "correggere" l'euristica (e non perdere informazioni). Se si dovesse arrivare a non trovare dei cammini, il nodo padre verrebbe espanso nuovamente solo se tutti i suoi figli presenti in frontiera hanno un f-valore maggiore rispetto al suo.

Viene proposto in classe un esempio di SMA* con limite di memoria di 3 nodi. E' importante osservare come non si potrà mai raggiungere la soluzione più profonda, perché essa richiede che siano memorizzati 4 nodi (corrispondente alla sua profondità).

Se si arriva ad un punto in cui tutte le foglie hanno lo stesso *f-valore* si potrebbe incorrere in un loop: viene eliminata una foglia che poi viene subito ri-espansa. Una soluzione è rimuovere la foglia più _vecchia_ (quella che è in frontiera da più tempo) ed espandere la più _recente_. Se queste due foglie coincidono, allora la soluzione che passa da quel nodo non può essere contenuta nella memoria disponibile, quindi è corretto rimuoverla (non arriverei mai alla soluzione). Ricapitolando, SMA* è:
* completo solo se la soluzione può essere contenuta in memoria
* ottimo se la soluzione è raggiungibile (altrimenti restituisce la miglior soluzione raggiungibile)

## Considerazioni finali su A\*

Si può limitare il consumo della memoria in una modo simile all'iterative deeping al contesto delle euristiche.

Questo si può fare andando ad aggiungere un limite al valore dalla funzione di valutazione.