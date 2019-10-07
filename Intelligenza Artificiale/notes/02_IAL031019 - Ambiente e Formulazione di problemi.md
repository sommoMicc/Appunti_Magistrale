# Lezione 2 - Ambiente e Formulazione di problemi
3 Ottobre 2019 (happy birthday to me!)

Il Performance Environment Actuators Sensors (PEAS) definisce l'ambiente in cui l'agente opera.

## Esempio di agente (new)
Taxi automatizzato:

- **Misura di prestazioni??**: sicurezza, destinazione, profitto, comodità;
- **Ambiente operativo**: strade e autostrade, traffico, pedoni, tempo;
- **Attuatori**: volante, accelleratore, freni, clackson, microfono/video,..
- **Sensori**: telecamera, accelerometri, sensori del motore, GPS,..


## Esempio di agente intelligente (old)

Bot che compra su internet.

- **Misura di prestazioni**: risparmio, affidabilità del venditore, tempo di spedizione;
- **Ambiente operativo**: motori di ricerca, siti di e-commerce, aste on-line;g
- **Attuatori**: sistema di pagamento, indirizzo di spedizione e intestatario;
- **Sensori**: protocolli di accesso ad internet e di pagamento.

## Tipi di ambiente

Alcune caratteristiche degli ambienti possono permettere ipotesi semplificative andando così ad influenzare la progettazione.

- **Osservabile**: si ha accesso a tutta l'informazione che caratterizza l'ambiente. Avere o non avere tutta l'informazione influisce nelle varie azioni, perché potrebbero essere intraprese delle decisioni solamente per ottenere ulteriori informazioni.<br> Ad esempio, il Solitario (con carte scoperte) e Backgammon sono osservabili, mentre l'internet shopping (è improbabile riuscire ad accedere contemporaneamente a tutti i siti che vendono un determinato oggetto) e il taxi (perché percepisco solo l'ambiente in prossimità) sono in parte osservabili.
- **Determinstico**: quando l'esecuzione di un'azione porta sempre lo stesso effetto nell'ambiente. Molto spesso un ambiente non è del tutto deterministico: ci sono quindi vari "gradi" di determinismo/stocasticità. In generale, lavorare in un ambiente deterministioco è più semplice in quanto si riesce a prevedere i risultati. <br>Ad esempio, il solitario è deterministico (ho un numero determinato di mosse che posso fare), mentre l'internet shopping lo è in parte (ci possono essere degli altri agenti che mi fottono i prodotti dal momento che li aggiungo al carrello a quello che li pago). Il taxi non è deterministico.
- **Episodico**: _la percezione attuale dell'ambiente non è influenzata dallo storico delle percezioni._ Anche in questo caso, un ambiente episodico permette di effettuare alcune assunzioni semplificative in quanto non è necessario tenere conto dello storico delle percezioni. Se l'ambiente non è episodico è necessario scegliere quante percezioni tenere in memoria, dal momento che non è possibile immagazzinarle tutte. Se in un ambiente una decisione influenza poi tutte quelle successive (ovvero il contrario di *episodico*) si dice che esso è **sequenziale**.<br>Nessuno degli esempi precedenti è episodico (solitario e backgamon dipendono dalle mosse precedenti, mentre il prodotto che acquisto tramite shopping su interent dipende dalle pagine che ho visitato).
- **Statico** (o stazionario): se le relazioni tra le entità che definiscono il problema stesso (le leggi che regolano il rapporto dell'agente con l'ambiente) restano intalterate nel tempo (ad esempio, le leggi della fisica). <br>Internet Shopping è parzialmente statico perché potrebbe cambiare o il valore della moneta o il prezzo del bene (asta). Il taxi è considerato dinamico perché ci possono essere lavori o impedimenti sulla strada (la viabilità non è statica!).
- **Discreto**: se le quantità che vengono osservate sono discrete o continue. <br>Solitario, Backgamon e Internet Shopping sono discreti (anche la moneta è considerata a grandezza finita, approssimazione al centesimo di euro). Il taxi invece è continuo.
- **Agente singolo**: c'è un solo agente che modifica l'ambiente o possono esserci più agenti che operano nello stesso ambiente?

Il mondo reale tipicamente è parzialmente osservabile, stocastico (non deterministico), sequenziale, dinamico, continuo e multi-agente.

## Tipi di agenti

Un agente può essere visto come un'_architettura_ e un _programma_ che permette di effettuare un'azione a seguito di una percezione (software specifico per un determinato problema).

Ogni agente può essere trasformato in un agente in grado di apprendere.

### Agente a riflesso (reattivi) semplice

Data una singola percezione si sa già che azione andare ad intraprendere, indipendentemente dalla storia passata. 
Non serve quindi salvare la storia delle operazioni. Un esempio di questo agente è l'aspirapolvere.

Si chiama agente riflesso perché esso, data una singola percezione, eseguirà sempre la stessa azione indipendentemente dalla storia, quindi a qualsiasi istante di tempo.

![alt text](./immagini/l2-agente-semplice.png "Agente semplice")

La conseguenza è programma composto da una serie di regole `if-then-else` necessarie per scegliere l'azione da fare. Si ottiene un comportamento funzionale (percezione mappata ad azione).

Questo tipo di agente è molto semplice da realizzare ed efficace, però funziona solamente nel caso le assunzioni fatte siano corrette (cioè se l'ambiente è effettivamente totalmente osservabile).

Ad esempio, una navetta deve andare da un punto A ad un punto B passando sempre per lo stesso tragitto.

Un miglioramento a questa tipologia di agente è quello di introdurre alcune scelte casuali, in modo da cercare di rompere alcuni loop infiniti. 

Se l'ambiente è parzialmente osservabile, questo approccio potrebbe essere fallimentare: si potrebbe provare a migliorare il nostro agente tenendo traccia delle percezioni passate in uno stato interno (funziona se l'ambiente è statico, altrimenti le percezioni passate diventano inutili).

### Agente a riflesso con stato

Per eseguire un'azione è necessario andare a considerare sia la percezione corrente, sia lo storico.

![alt text](./immagini/l2-agente-riflesso.png "Agente a riflesso con stato")

L'attivazione delle regole viene influenzata anche dallo stato interno.

In questo caso è però necessario che l'agente abbia conoscenza riguardo le leggi che regolano l'ambiente e come le azioni che svolge influenzano l'ambiente.

Sulla base di queste informazioni vengono poi applicate le regole per la scelta dell'azione da svolgere.

Si riesce quindi a gestire meglio situazioni parzialmente osservabile, tuttavia le scelte sono _hard coded_ nelle regole, quindi la soluzione non è flessibile.

### Agenti basati su goal (obiettivi)

Agenti più flessibili che cercano di raggiungere un determinato obiettivo.

![alt text](./immagini/l2-agente-goal.png "Agente con goal")

In questo caso le regole vengono sostituite da degli obiettivi.

La modifica principale sta nell'aggiunta di un componente che cerca di prevedere come il mondo cambia se vado ad effettuare una derterminata azione.

Viene quindi cercata la sequenza di azioni migliori da svolgere per raggiungere il proprio obiettivo, tenendo sempre in considerazione la percezione attuale dell'ambiente.

Ad esempio, un taxi ha come obiettivo (goal) quello di raggiungere la destinazione designata dal cliente.

Ci sono però dei problemi nel caso il goal prefissato dall'agente non sia pienamente raggiungibile oppure ci sono più goal in constrasto tra loro. Ad esempio, se ho un agente che cerca di farmi ottennere entro 30 giorni il 2% del profitto dei soldi investiti in borsa, potrebbe essere poco utile in quanto in quello stesso periodo, ad esempio, avrei potuto raggiungere il 6% di profitto.

### Agenti a misura di utilità

Agente che sceglie le azioni da intraprendere in modo che siano le più convenienti per una data misura di utilità.

![alt text](./immagini/l2-agente-utilita.png "Agente a misura di utilità")

Il concetto di goal viene sostituito da una funzione che calcola quando l'agente è _"contento"_ di essere in un determinato stato.

Quando viene valutato l'effetto dell'azione sull'ambiente si tiene conto anche di quanto quello stato è _"buono"_ per l'agente. Tenendo anche conto delle varie probabilità di raggiungere con successo lo stato.

Ad esempio, un taxi deve correre veloce (goal) per arrivare il prima possibile. Tuttavia, se va *troppo* veloce si schianta. Ecco perché viene introdotta una funzione di utilità dello stato, e grazie a questa una velocità troppo eccessiva può essere marcata come deplorevole.

## Agenti in grado di apprendere
L'apprendimento può essere visto come una caratteristica che va innestata alla struttura di un agente.

Nel caso dell'agente a riflesso, ad esempio, l'apprendimento può servire a "tarare" le regole (che poi comunque verranno eseguite come se fossero _hardcoded_).

![alt text](./immagini/l2-agente-apprende.png "Agente in grado di apprendere")

Per garantire l'apprendimento deve essere presente un __elemento critico__ che sia in grado di valutare le azioni dell'agente in modo critico. Serve quindi un modo per valutare le prestazioni dell'agente.

L'emento critico genera quindi un feedback per l'__elemento di apprendimento__ che è quello che influenza il __performance element__, ovvero che cambia i parametri che determinano l'azione da compiere dato un set (anche composto da un elemento solo, in base al tipo di agente) di percezioni. 

Il performance element è l'elemento che decide quale azione andare a prendere in base alle informazioni ottenute dai sensori.

C'è anche un __problem geneator__ che fa in modo che tutte le casistiche possibili vengano affrontate dall'elemento di apprendimento, in modo che anche queste vengano considerate.

Questo perché l'apprendimento potrebbe essere come quello di uno studente, che cerca di imparare le domande tipiche di un compito, il problem generator è quello che genere le domande che non sono mai comparse in un compito. In pratica, se io ho delle percezioni che non mi portano molto lontano dal punto iniziale, l'agente non fa esperienza.  Formalmente, questo si chiama rischio di sovraspecializzazione. Grazie al problem generator l'agente viene forzato a fare delle scelte "alternative" che non sono mai state esplorate in precedenza.

Il problem generator risulta particolarmente importante nelle fasi iniziali.

## Ricerca in uno spazio di soluzioni

Esempio della vacanza in Romania.

__Goal:__ essere a Bucharest;

__Stati:__ varie città;

__Azioni:__ viaggi tra una città e l'altra;

Trovare una soluzione vuol dire quindi trovare una sequenza di città che permetta di raggiungere Bucharest in tempo per il volo.

### Formulazione di un problema (single state)

Un problema è definito da 4 elementi:

- __Stato iniziale__: stato iniziale, ad esempio 'Arad' (una citta della Romania).
- __Funzione successore__: funzione che dato uno stato fornisce tutti gli stati vicini allo stato dato e l'azione che permette di raggiungerli. Esempio: _S(Arad) = {&lt;Arad-Zerind,Zerind&gt;...}_.
- __Test per il goal__: che può essere _esplicito_ (raggiungo Bucharest) oppure può essere _implicito_ che descrive una caratteristica/proprietà (città con una determinata officina), è una funzione che dato uno stato specifica se lo stato soddisfa o meno la proprità che mi interessa(_Bucharest(x)_).
- __Costo di un cammino__: è la somma dei costi del cammino che sto considerando, a partire dallo stato iniziale fino allo stato attuale. Il costo di ogni singolo passo, _c(x,a,y)_ (costo per arrivare da x a y usando l'azione a) viene assunto &ge; 0.

_Una soluzione è quindi una sequenza di azioni che conduce da uno stato iniziale ad uno stato di goal._

Questa formulazione è limitata in quanto non è possibile andare a specificare delle preferenze riguardo la ricerca delle città.

Tuttavia permette di astrarre il problema che risulterebbe troppo complesso nel mondo reale.

Nell'esempio della Romania vengono astratti sia gli stati sia le azioni, questo perché le città non sono un semplice punto ma hanno una certa aerea e allo stesso modo da una città all'altra posso essere disponibili molte più strade.

Di conseguenza anche la soluzione ottenuta sarà una soluzione astratta.



```python
function SIMPLE-PROBLEM-SOLVING-AGENT(percept) returns an action
    persistent: seq, an action sequence, initially empty
                state, some description of the current world state 
                goal, a goal, initially null
                problem, a problem formulation
    state <- UPDATE-STATE(state,percept) 
    if seq is empty then
        goal FORMULATE-GOAL(state)
        problem <- FORMULATE-PROBLEM(state, goal) 
        seq SEARCH(problem)
        if seq = failure then
            return a null action
    action <- FIRST(seq)
    seq <- REST(seq)
    return action
```
Viene portato un esempio di ricerca in ampiezza su un albero. La coda dei nodi da esplorare è una FIFO. La coda viene riempita finché non ho trovato il nodo target (raggiunto il goal). Per la ricerca in profondità, invece, si usa una struttura LIFO (il nodo aggiunto viene subito "esploso").

Il "bug" della ricerca ad albero per risolvere il problema è che ho una pesante duplicazioni delle città, ma la caratteristica positiva è che mi permette di differenziare i vari percorsi che partono da uno stato/città X e arrivano ad uno stato Y. Ecco perché nelle slide viene riportata sia la ricerca ad albero che quella a grafo.