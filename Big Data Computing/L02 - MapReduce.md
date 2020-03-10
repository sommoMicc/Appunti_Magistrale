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
