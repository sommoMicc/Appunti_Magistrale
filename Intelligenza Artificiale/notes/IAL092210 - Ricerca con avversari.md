#Lezione 9 - Ricerca con avversari

Ovvero algoritmi per i giochi.

##Differenza con i problemi di ricerca

Non c'è più uno spazio di ricerca statico, perché si ha a che fare con un avversario che è un'entità imprevedibile, quindi la soluzione al problema non è più un cammino da uno stato iniziale ad uno stato finale (questo perché non è più il singolo giocatore che effettua tuttele mosse).

In questo caso c'è un altro agente che decide in autonomia come contrastare il cammino del primo giocatore.

La soluzione diventa quindi una strategia, una funzione che specifica una mossa per ogni possibile mossa dell'avversario.

In alcuni casi ci sono anche dei limiti di tempo codificati nelle regole del gioco, le possibilità di ricerca sono quindi limitate e non sempre è possibile arrivare ad una strategia ottima.

## Tipi di giochi

- Informazione completa e deterministici: come la dama, gli scacchi, othello;
- Informazione completa e non deterministici: backgammon, monopoli;
- Informazione parziale e non deterministici: poker, risiko, briscola.

Possono essere aggiunte anche altre informazioni, come online/offline.

## TicTacToe

*Nelle slide c'è un esempio di albero di gioco*

Sono presenti due funzioni, Max(x), Min(o) che rappresentano i due giocatori, i quali a turno mettono il loro simbolo nella griglia. 

Vince il primo che riesce ad allineare 3 simboli uguali, altrimenti c'è una patta.

I nomi derivano dal fatto che Max cerca di massimizzare la funzione di utilità mentre Min cerca di minimizzarla.

Questo gioco viene detto a **somma zero** o costante, questo perché il vantaggio di un giocatore equivale allo svantaggio dell'avversario.

## Minimax

Gioco perfetto per giochi deterministici e ad informazione perfetta.

L'idea è quella di scegliere la mossa che conduce alla posizione con valore *minimax* più alto che equivale al miglior vantaggio raggiungibile con un avversario che gioca in modo ottimo.

*ply*: mossa di un giocatore, un turno di gioco è composto da 2 ply.

![](./immagini/l9-minimax.png)

Con questo algoritmo si cerca di massimizzare l'utilità nel caso pessimo in quanto si suppone che l'avversario stia giocando in modo ottimo.

```javascript
function MiniMaxDecision(state) returns an action
    inputs: state, current state in game
    v <- MaxValue(state)
    return the action in Successor(state) with value v
    
function MaxValue(state) returns a utility value
    if TerminalTest(state) then return Utility(state)
    v <- -∞
    for a,s in Successors(state) do
        v <- Max(v, MinValue(s))
    return v
    
function MinValue(state) returns a utility value
    if TerminalTest(state) then retrun Utility(state)
    v <- ∞
    for a,s in Successors(state) do
        v <- Min(v, MaxValue(s))
    return v
```

La funzione `MaxValue` cerca di massimizzare la funzione d'utilità quando gioca Max, mentre `MinValue` cerca di minimizzare la funzione funzione d'utilità quando gioca Min.

### Proprietà

L'algoritmo è completo solo se l'albero degli stati è finito.

Nel caso in cui l'albero è infinito non è mai possible raggiungere le foglie e quindi non è garantita la completezza, da notare che se l'albero è infinito la strategia di gioco può essere finita.

L'algoritmo risulta ottimo sia se entrambi i giocatori giocano in modo ottimo, sia nel caso l'avversario giochi in modo non ottimo.

Questo perché Max quando può vincere, va a vincere e se l'avversario gioca in modo sub-ottimo, Max riesce a vincere anche in situazioni in cui non avrebbe vinto.

La complessità in tempo è *O(b<sup>m</sup>)*, dove *b* è il fattore di branching e *m* la profondità della soluzione.

Questo perché l'algortimo deve esaminare tutto l'albero fino alle foglie per poter calcolare i valori per i nodi interni. 

La complessità in spazio invece è *O(bm)* con esplorazione depth-first.

Il gioco degli scacchi ha in media *b = 35* e *m = 100* in caso di avversari normali, non è quindi possibile trovare una soluzione perfetta.

##Limiti alle risorse

Si suppone di avere un limite al tempo per calcolare le mosse.

Serve quindi una **funzione di valutazione** che può essere applicabile sia ad una foglia e in questo caso funziona da funzione di utilità, sia ad uno stato centrale e in questo caso fornisce una *desiderabilità* dello stato in cui si trova, una sorta di funzione euristica.

Serve inoltre un **test di taglio (cutoff)** che pone un limite all'albero di ricerca, raggiunto il quale viene calcolata la funzione di valutazione.

Con il cutoff c'è un problema in quanto può capitare che per raggiungere uno stato molto favorevole è necessario andare a sacrificare dei pezzi, passando cioè per degli stati svantaggiosi. (Ad esempio il sacrificio di un pezzo nel gioco degli scacchi).

Conviene quindi utilizzare una ricerca di **quiescienza** cioè tagliando la ricerca solamente quando la funzione di valutazione per una serie di nodi non cambia di molto.

Se invece tra nodi successivi c'è un cambio notevole tra le funzioni di valutazioni, allora si tengono delle risorse per andare ad esplorare quell'area dell'albero.

### Funzione di valutazione

È una funzione usata per calcolare il valore degli stati.

Negli scacchi la funzione risulta essere un combinazione lineare pesata di varie caratteristiche.

La funzione lineare garantisce l'indipendenza del valore di ogni componente, mentre con le funzioni non lineari questo non succede in quanto possono essere considerate coppie di pezzi.

Come per la funzione euristica c'è un trade-off sulla bontà dell'euristica, perché può capitare che sia necessario tagliare prima per avere più tempo a disposizione in modo da poter calcolare un euristica buona, oppure si può scegliere di esplorare più nodi ed avere una stima più grossolana e veloce da calcolare.

Tipicamente si preferisce la profondità.

####Digressione

La cosa importante della funzione di valutazione non è la stima precisa ma la valutazione corretta della "bontà" di uno stato, cioè che la funzione sia monotona, questo perché la funzione deve semplicemente esplicitare il vantaggio di un giocatore piuttosto che dell'altro.

Infatti, quello che conta è solamente l'ordine di vista degli stati. 

Il guadagno in giochi deterministici agisce come una funzione di utilità *ordinale*.

###Ricerca con taglio

`MinimaxCutoff` è identico a `MinimaxValue` con la differenza che:

- `Terminal` viene rimpiazzata da `Cutoff`: non arrivo alla fine ma mi fermo ad un certo punto;
- `Utility` viene rimpiazzata da `Eval`: la funzione di utilità viene sostituita con la funzione di valutazione.

Ad esempio nel gioco degli scacchi si può fare un *4 ply* che corrisponde al livello di un giocatore pessimo.

Deep Blue e Kasparov arrivavano ad *12-ply*

###𝜶 - 𝜷 pruning

Vengono fatte delle considerazioni per evitare di espandere dei rami che portano a situazioni disastrose.

𝜶 = valore della scelta migliore per Max al di fuori del cammino corrente

𝜷 = valore della scelta migliore per Min al di fuori del cammino corrente

Questa ricerca aggiorna i valori di 𝜶 e 𝜷 man mano che procene e pota i rami restanti non appena il valore del nodo è minore di quello di 𝜶 quanto tocca a Min e maggiore di 𝜷 per Max.
 
Nel caso ottimo in cui le mosse sono ordinate per funzione di utilità (decrescente quando cerca max, *(trovo subito il massimo)*, crescente quando cerca min *(trovo subito il minimo)*) si riesce a raddoppiare la profondità raggiungibile, mentre nel caso pessimo non si ha nessun miglioramento.

Questa strategia non va a modificare il risultato finale in quanto vengono scartate solamente stati non ottimi.

####Perché 𝜶 - 𝜷?

𝜶 è il miglior valore per Max trovato al di fuori del cammino corrente, se V è peggiore di Max questo verrò evitato, lo stesso vale per 𝜷.

####Codice

```javascript
function AlphaBetaSearch(state) return an action
    inputs: state, current state in game
    v <- MaxValue(state, -∞, +∞)
    return the action in Successros(state) with value

function MaxValue(state, 𝜶, 𝜷) retrun a utility value
    inputs: state, current state in game
            𝜶, the value of the best alternative for Max along the path to state
            𝜷, the value of the best alternative for Min alogn the path to state
    if TerminalTest(state) then return Utility(state)
    v <- -∞
    for a, s in Successors(state) do
        v <- max(v, MinValue(s, 𝜶, 𝜷))
        if v >= 𝜷 then return v
        alfa = Max(𝜶, v)
    return v

function MinValue(state, 𝜶, 𝜷) returns a utility value
    inputs: state, current state in game
            𝜶, the value of the best alternative for Max along the path to state
            𝜷, the value of the best alternative for Min alogn the path to state
    if TerminalTest(state) then return Utility(state)
    v <- +∞
    for a, s in Successors(state) do
        v <- min(v, MaxValue(s, 𝜶,𝜷))
        if v <= 𝜶 then return v
        beta = Min(𝜷, v)
    return v

```



**CSP Binario**: ogni vincolo si riferisce ad al più due variabili.

**Grado dei vincoli**: i nodi del grafo sono le variabili del CSP e gli archi rappresentano i vincoli.

Considerando un CSP come un grafo è possibile utilizzare le proprietà del grafo per velocizzare la ricerca di una soluizone.

## Varietà di CSP

Tipicamente le variabili dei problemi CSP sono discrete.

I loro domini possono essere *finiti* o *infiniti*.

In alcuni casi è necessario utilizzare un linguaggio per definire vincoli.

Solamente i vincoli lineari sono risolvibili, mentre la risolvibilità di quelli non lineari non è decidibile.

C'è anche la possibilità di utilizzare variabili continue con vincoli lineari, in questo caso la risoluzione dei vincoli avviene con il metodo del simplesso (programmazione lineare) con complessità esponenziale nel caso pessimo (polinomiale tipicamente).

I vincoli possono essere:

- **unari**: coinvologono una sola variabile;
- **binari**: coinvologono due variabili:
- **di ordine superiore**: coinvolgono più di due variabili;
- **prefenze (o soft)**: trammite l'assegnamento di un costo ad ogni variabile, un esempio di questo vincolo è preferire il rosso al verde nel problema della colorazione di una cartina. (il problema diventa un problema di ottimizzazione vincolata, vengono prefreite le soluzioni di costo minore)

## Formulazione di ricerca standard

Gli stati vengono definiti dai valori assegnati fino ad un dato momento.

**Stato iniziale**: l'assegnamento vuoto.

**Funzione successore**: assegna un valore ad una variabile non ancora assegnata che è compatibile con l'assegnamento corrente. Questa funzione fallisce se non esiste un assegnamento legale.

**Test di goal**: l'assegnamento corrente è completo, tutti i vincoli sono soddisfatti.

Proprietà:

1. Valido per tutti i CSP;
2. Ogni soluzione appare a profondità *n* con *n* variabili (tutti gli stati a profondità *n* sono soluzioni, questo per costruzione, perché altrimenti non sarei riuscito a scendere fino a tale profondità), conviene quindi usare la ricerca depth-first;
3. Il cammino è irrilevante, interessa solo lo stato (anche una soluzione locale può andare bene);
4. A profondità *l* il fattore di branching (cioè nodi nella frontiera) è tipicamente *(n-l)\*d*.

## Ricerca con Backtracking

Gli assegnamenti sono tra loro commutativi.

Utilizzare il backtracking nella ricerca depth-first consiste nel tornare indietro di un nodo e utilizzare un altro valore per l'assegnamento.

La ricerca con backtracking è l'algoritmo non informato di base per risolvere i CSP.

```
function BacktrackinSearch(csp) returns solutions/failure
	return RecursiveBacktracking([],csp)

function RecursiveBacktracking(assigned, csp) return sorultion/failure
	if assigned is complete then retun assigned
	var <- SelectUnassignedVariable(Variables[csp], assignd, csp)
	for each value in OrderDomainValue(var, assigned, csp) do
		if value is consistent with assigned according to Constraints[csp] then
			result <- RecursiveBackracking([var = value | assigned], csp)
			if result != failure then return result
	end
	return failure
```

### Miglioramenti dell'efficienza

Aggiungendo degli accorgimenti ai vari assegnamenti è possibile andare a migliorare l'efficienza dell'algoritmo.

1. Quale variabile si deve assegnare al prossimo passo?
2. In quale ordine testare i valori del dominio?
3. È possibile rilevare a priori dei fallimenti inevitabili?
4. È possibile sfruttare la stuttura del problema? (es: il problema è composto da più sotto-problemi tra loro indipendenti oppure la stuttura dei vincoli è simmetrica)

#### Assegnamenti delle variabili

Una euristica che porta ad un miglioramento è quella di scegliere come prossima variabile da assegnare quella **più vincolata** cioè con il minor numero di valori possibili. In questo modo scopro prima se sto andando verso un assegnamento che non può essere completato.

Se ci sono più variabili con lo stesso numero di vincoli, tra queste conviene scegliere quella che ha **più vincoli con variabili non assegnate**, perché è quella che scegliendo un valore vincola maggiormente la scelta delle altre.

Una volta scelta la variabile, posso scegliere di assegnarle il valore **meno vincolante**, cioè quello che esclude meno valori tra quelli possibili delle variabili non ancora assegnate.

#### Foward checking

*attività di propagazione dei vincoli*

L'idea è quella di tenere traccia dei rimanenti valori legati per le variabili non assegnate. Viene terminata la ricerca se c'è qualche variabile che rimane senza valori legali.

Dopo un assegnamento si va a controllare come cambiano i domini delle altre variabili.

Questa cosa prende il nome di **constraint propagation** e ci sono vari algortimi che permettono questi, vedi corso di Sistemi Con Vincoli.

#### Struttura del grafo

Se il grafo è composto da sotto-problemi tra loro indipendenti, conviene risolverli separatamente e poi combinare tra loro le soluzioni.

In alcuni casi il guadagno temporale risulta estremo, si passa da miliardi di anni a qualche secondo.

Inoltre, se il grafo associato al CSP ha una struttura ad albero, ovvero non ha vincoli, il CSP può essere risolto in *O(nd<sup>2</sup>)*.

Questo perché si può scegliere un ordine delle variabili che sia consistente con la topologia del grafo.

## Algoritmi iterativi per CSP

Per risolvere un CSP è possibile utilizzare sia Hill-Climbing che Simulated Annealing, in quanto questi lavorano con stati "completi", cioè che hanno tutte le variabili assegnate.

Per applicarli ad un CSP è necessario permettere stati con vincoli non soddisfatto e degli operatori che permettono di riassegnare valori ad una variabile.

La selezione della variabile viene fatta in modo casuale tra quelle che hanno dei conflitti, mentre come valore per la variabile si usa l'euristica del minimo conflitto, utilizzando quindi la funzione classica `h(n) = numero totale di vincoli violati`.

### Presetazioni di min-conflicts

Dato una stato iniziale random, si può risolvere n-regine per n arbitrario in un tempo costante con alta probabilità.

Questo sembra essere vero per ogni CSP generato a caso, tranne che per un intervallo ristretto, del rapporto:

```
R = numero di vincoli / numero di variabili
```