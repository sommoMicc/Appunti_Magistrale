# MapReduce

## Implementation of a MapReduce round

Supponiamo che l'input sia in un file. L'implementazione di un round procede come segue:

- Il file di input è diviso in _X chunks_ (sottoinsieme di key-value pair) e ogni _chunk_ forma l'input di un **map task**
- Un map task è assgnato ad un _worker_ (computer) che applica la map function ad ogni coppia chiave-valore, salvando il risultato (intermedio, ovviamente) sulla sua memoria locale.
- Le coppie chiave-valore intermedie, finché sono ancora residenti nel disco locale, vengono partizionate in **Y buckets** tramite una funzione di hash _h: (k,v) -> Bucket **i**=h(k) mod Y_. Il valore **i** rappresenta l'indice del bucket in cui verranno memorizzate le coppie. Da notare che tutte le coppie aventi la stessa chiave saranno nello stesso bucket;
- Ogni bucket forma l'input di un differente task **reduce** che è assegnato ad un worker (nodo di calcolo).
  Il worker applica la funzione _reduce_ ad ogni gruppo chiave-valore avente la stessa chiave, scrivendo l'output sul _Distributed File System_. L'applicazione della funzione reduce ad un gruppo di coppie chiave-valore è chiamata **reducer**
- Il programma è diviso in due: **master process** e **worker process**. Il master è il coordinatore dell'esecuzione del programma, incaricato di assegnare il task map-reduce ai worker e di monitorarne lo stato (worker in idle, esecuzione di un task in corso o completata).
- I file di input e di output risiedono nel _Distributed File System_, mentre i risultati intermedi risiedono nelle memorie locali dei computer.
- I round necessitano di una operazione di movimentazione dei dati: le coppie chiave-valore intermedie devono essere mosse dal computer che le ha prodotte in output a quello che le richiede in input. E' sicuramente una parte del round molto onerosa in termini di tempo, tuttavia con Spark lo _shuffle_ è implementato in maniera intelligente, quindi è un po' meno costoso. In ogni caso, è un indice di performance molto importante
- I valori di _X_ (numero di _Map Tasks_) e Y(numero di _Reduce Task_) sono degli iperparametri, cioè dovrebbero essere definiti dall'utente _a priori_ in base alla tipologia del problema.

## Dealing with Faults

Il DFS è fault-tolerant, quindi in caso di problemi i dati contenuti in esso possono essere recuperati. Uno dei compiti del master program è quello di pingare i _workers_ in modo periodico per rilevare gli errori. In caso di fallimento, i Map task completati o in corso nel "faulty worker" sono resettati e verranno rieseguiti. Siccome l'output del map task è salvato "in locale" sul worker, se esso si guasta anche l'output dei task già completati verrà perso, quindi tutti (a prescindere) dovranno essere rischedulati, cioè riassegnati ad altri worker.
In caso di task _Reduce_, solo i task falliti dovrano essere riassegnati, in quanto l'output di un task reduce viene salvato nel DFS, che per definizione è fault tolerant.
Invece, se il master fallisce, l'evento causa un errore non recuperabile, quindi l'intero task MapReduce deve essere resettato.

## Implementation of MapReduce Algorithm

Un algoritmo definisce come un output viene calcolato a partire dall'input. Quando specifichiamo un agloritmo MapReduce, dovremmo farlo avendo in mente che dovrebbe essere "facile" capire:

- Quali sono input e output dell'algoritmo;
- Qual'è la sequenza di round eseguita e, per ognuno di esso, quali sono input, intermediate e output sets di coppie chiave-valore e quali funzioni vengono applicate nella fase map e reduce.
- Quali sono e a quanto ammontano i limiti asintotici per gli indicatori fondamentali di performance (_key performance indicators_)

## Specification of a MapReduce Algorithm

Per descrivere ogni algoritmo di MR con un numero fissato di round _R_, si può usare il seguente stile:

- **Input**: descrizone dell'input come un insieme di coppie chiave-valore.
- **Output**: descrizione dell'output come un insieme di coppie chiave-valore.
- **Round 1**:
  - _Fase di Map_: descrizione della funzione applicata ad ogni coppia chiave-valore
  - _Fase Reduce_: descrizione della funzione applicata ad ogni gruppo di coppie chiave-valore aventi la stessa chiave
- **Round n**: Come il round 1

Questa specifica ad alto livello dovrebbe non essere tediosa, quindi le descrizioni dovrebbero essere abbastanza straight-forward!s
Inoltre, in un algoritmo MapReduce, il numero di round _R_ potrebbe dipendere dall'istanza di input.

## Analysis of a MapReduce algorithm

Nell'analisi di big data, oltre alla complessità temporale dell'algoritmo, è molto importante la sua complessità spaziale! Infatti, per definizione i dati di input sono tanti, e c'è bisogno di salvare i risultati intermedi in locale nei vari worker; tali risultati potrebbero essere ancora più onerosi da memorizzare del dataset iniziale.

Quindi, l'analisi di un algoritmo MapReduce ha lo scopo di stimare i seguenti indicatori chiave:

- **Numero di round R**, che misura il running time dell'algoritmo. La scelta è stata fatta perché all'inizio la performance del round era dominata asintoticamente dallo shuffle dei dati, quindi ogni round aveva un tempo di esecuzione quasi costante. Oggigiorno questo non è vero, ma per semplicità e coerenza si continua ad usare questa metrica
- **Spazio locale $M_L$**, che indica la massima quantità di memoria centrale (main memory) richiesta ad un worker in un qualsiasi round da una singola invocazione della funzione _Map_ o _Reduce_ usata in quel round per salvare l'input e ogni struttura dati richiesta dall'invocazione.
- **Spazio aggregato $M_A$**, ovvero lo spazio massimo richiesto per l'archiviazione delle coppie chiave-valore di input o generate da una qualsiasi fase Map o Reduce di un quasisasi round.

**Osservazioni**: gli indicatori sono stimati tramite una analisi asintotica in funzione della grandezza dell'istanza. Inoltre, $M_L$ da un limite minimo sulla quantità di _main memory_ (RAM) richiesta da ogni worker, mentre $M_A$ da un limite minimo sulla _quantità totale di spazio su disco_ che la piattaforma di esecuzione deve fornire.

## Example: Word Count

Il problema consiste nello contare l'occorrenza di ogni parola in un insieme di documenti. Formalmente, il problema si può descrivere come:

- **Input**: insieme di documenti di testo $D_1,..D_n$ contenenti _N_ occorrenze di parole. Ogni documento è una coppia chiave-valore, dove la chiave è il nome del documento e il valore rappresenta il suo contenuto.
- **Output**: insieme di coppie chiavi-valore $(w, c(w))$ dove $w$ è la parola che compare nei documenti e $c(w)$ è il numero delle occorrenze di $w$ nei documenti.
- **Round 1:**:
  - _Map Phase_: per ogni documento $D_i$ viene prodotto un insieme di coppie intermedie $(w, c_i(w))$, una per ogni parola $w \in D_i$, dove $c_i(w)$ è il numero di occorrenze di $w$ in $D_i$;
  - _Reduce Phase_: per ognin parola _w_, vengono raccolte tutte le coppie intermedie $(w, c_i(w))$ e viene ritornata la coppia di output $(w, c(w))$, dove $c(w)$ è la somma di tutti i $c_i(w)$.

### Analysis of Word Count

Definendo $N_i$ come il numero di parole in $D_i$ (contando le ripetizioni), ovvero $N = \sum_{i=1}^k N_i$, e assumiamo che ognni parola richieda uno spazio costante. Definiamo inoltre $N_{max} = max_{i=1,..,k}N_i$. Abbiamo:

- _R = 1_
- $M_L = O(max\{N_{max}, k\}) = O(N_{max}+k)$. Infatti, nella fase map, il worker che sta processando $D_i$ richiede spazio $O(N_i)$. Nella fase reduce, il worker incaricato della parola $w$ aggiunge il contributo di al massimo $k$ coppie $(w, c_i(w))$

- $M_A = O(N)$, dato che l'input size è $O(N)$ e $O(N)$ coppie addizionali sonno prodotte dall'algoritmo in tutto.

**Osservazione**: $N_{max} + K = \Theta(N)$, ovvero hanno la stessa dimensionalità dell'input, quindi si ha uno spazio lineare locale. In tal caso, molti dei vantaggi di MapReduce sono persi.

## Design goal for MapReduce.
Se si ha un problema risolvibile con un algoritmo sequenziale in spazio $S(|input|)$, esiste un algoritmo MapReduce da 1 round con $M_L = M_A = \Theta(S(|input|))$. Infatti, basta semplicemente far eseguire tutto il codice dell'algoritmo in un unico round. Tuttavia, questo non sfrutta la capacità e le ottimizzazioni fornite da mapreduce, soprattutto per quanto riguarda il parallelismo.

Infatti, un algoritmo MapReduce, per processare in modo efficiente dati molto grandi, dovrebbe puntare a _dividere la computazione nel minor numero possibile di round the eseguono diversi task in parallelo, e far si che ogni task lavori in modo efficiente su un piccolo sottoinsieme dei dati._
Formalmente:

- _Pochi round_ (es: $R = O(1))$);
- Spazio locale sublineare (es.: $M_L = O(|input|)^\epsilon$, dove $\epsilon \in (0,1)$)
- Spazio aggregato lineare (esempio: $M_A = O(|input|)$), oppure leggermente superlineare (perché già i dati sono tanti)
- Complessità polinomiale.

**Osservazione**: gli algoritmi molto spesso hanno un tradeoff tra performance indicators. Spesso, bassi $M_L$ abilitano un parallelismo molto alto ma possono comportare un alto $R$.

## Pro e contro di MapReduce

I fattori che rendono MapReduce adatto al processo di big data sono:

- **Visione data-centrica**: Il design degli algoritmi può focalizzarsi su trasformazioni di dati, puntando al soddisfacimento dei _Design Goal_ illustrati in precedenza. Inoltre, i framework di programmazione che supportano MapReduce (come Spark) spesso rendono l'allocazione dei task ai worker, il data-management, la gestione dei fallimenti totalmente trasparente al programmatore.
- **Portabilità/adattabilità**: Le applicazioni possono essere eseguite su piattaforme differenti e l'implementazione "under the hood" del framework cercherà di sfruttare al meglio il parallelismo e di minimizzare quanto più possibile i costi di movimentazione dei dati.
- **Costo**: Le applicazioni scritte in MapReduce spesso riescono a girare su hardware moderatamente costoso: non servono supercomputer

I contro sono:

- **Debolezza di R come performance measure**: il numero di round non considera il tempo di esecuzione di map e reduce e il volume effettivo dei dati scambiati (shuffled). Esistono misure di prestazioni più sofisticate, anche se meno usabili.
- **Curse of the last reducer**: potrebbe essere che uno dei reducer impieghi di più degli altri. Quando si progettano algoritmi bisognerebbe far si che il carico sia distribuito equamente tra i vari reducer, in modo che tutti impieghino più o meno lo stesso tempo. Tuttavia, questo non è sempre possibile.
