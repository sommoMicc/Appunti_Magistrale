# Introduzione
Il fenomeno big-data è dovuto a:
- Progresso tecnologico, come l'aumento di capacità di storage, banda di comunicazione, capacità di elaborazione.
- Riduzione di costi ICT (come quello di fabbricazione delle componenti, ad esempio)
Il risultato è che la tecnologia informatica è penetrata in tutti i settori.

Si prevede che nel 2025 si arriverà ad avere 175ZettaByte di dati, corrispondenti a 23 file di DVD dalla terra alla luna.

Al termine **big-data** sono associate due problematiche distinte:
1. Il termine big data è spesso confuso con quello di "data analysis" (analisi dei dati). Molto spesso quindi le persone che dicono "devo fare analisi big-data" in realtà devono fare un'analisi di dati, ma la problematica degli stessi non è la loro grandezza
2. I dataset sono grandi, ovvero l'analisi con qualsiasi algoritmo (stato dell'arte) sarebbe *unfeasible*. Cosa si intende per "grande" dipende dalla fattispece del problema, ma in generale la challenge è lo sviluppo di nuovi framework di calcolo e nuove soluzioni algoritmiche.

Il corso si concentra sulla issue 2

## 4V
Termine introdotto da IBM per indicare le problematiche inerenti ai big data. Nello specifico:
- *Volume*: dimensione dei dati
- *Veracity*: dataset grandi che arrivano "dal mondo reale" è probabile contengano rumore o dati incerti, quindi la nozione di *accuracy* va rivista.
- *Velocity*: alcune volte i dati arrivano ad una velocità così alta che non possono essere salvati e processati offline, pertanto è richiesto l'uso del cosiddetto *stream processing* (ovvero processare i dati direttamente "nel flusso")
- *Variety*: in base alla caratteristica del dataset esistono dei tool migliori da scegliere. Dall'altra prospettiva, quando si sta realizzando uno strumento di analisi dei dati vanno anche considerate le caratteristiche dei dataset su cui esso andrà utilizzato.

=> è richiesto un cambio di paradigma rispetto al traditional computing.

# MapReduce
La motivazione alla base di MapReduce risale ai primi anni 2000. 
In quegli anni si verificava una necessità impellente di analizzare grandi quantitativi di dati.
I tool disponibili non riuscivano ad analizzare grandi dataset. Gli algoritmi di analisi, infatti, avevano una alta complessità polinomiale e i computer una limitata memoria interna. In casi estremi, persino solo leggere i dati diventava un'operazione molto onerosa (1000TB solo di pagine web)

L'uso di strumenti di calcolo molto potenti, che all'epoca era stato limitato a scenari molto specifici (calcoli scientifici) diveniva necessario per una larga serie di applicazioni.

Un **powerful computing system** è caratterizzato da tante unità di calcolo, molta memoria e in generale molta capacità computazionale. Questa può derivare da un'unico computer molto potente o da tanti computer meno potenti "combinati" (*loosley coupled*) assieme.

I loro problemi, però, sono:
- Il costo di acquisto e di mantenimento
- La rapidità con cui diventano obsoleti
- Il loro fault tolerance: più alto è il numero dei componenti utilizzati e minore sarà il tempo in cui uno si guasta (*Mean-Time Between Faiulres*, **MTBF**), cioé più alta è la probabilità di guasto. Quindi le applicazioni devono essere sofisticate a tal punto da permettere di non riavviare l'intero calcolo quando un componente fallisce.
- Lo sviluppo di software parallelo efficiente è molto difficile, e richiede algoritmi e capacità di ingegnerizzazione/programmazione molto sofisticate.

Per risolvere questi problemi (e i suoi problemi interni) Google nel 2004 introduce MapReduce, framework che permette l'analisi di big data su piattaforme distribuite.
Le caratteristiche principali del framework sono:
- L'uso di un approccio data-centrico: una map-reduce computation è una serie di trasformazioni sui dati ottenute applicando ripetutamente operazioni di *map* e *reduce*
- La facilità di sviluppo di algoritmi/programmi. Dettagli "tecnici" (come allocazione di task, distribuzione di dati, fault-tolerance, load-balancing) sono nascosti al programmatore, ovvero se ne occupa il framework. L'altro lato della medaglia è che non si possono tarare i parametri per ottenere performance miglori.

## Piattaforme
MapReduce gira tipicamente su piattaforme proprietarie dell'utente o su piattaforme cloud (come AWS e Azure). I servizi cloud possono essere *IaaS* (viene fornita solo la macchina e l'infrastruttura, ma non il software) o *PaaS* (oltre all'infrastruttura vengono forniti anche software).

L'architettura tipica di un cluster è composta da:
- **Rack di 16-64 calcolatori**, connessi intra rack e inter-rack da switch veloci
- **File system distribuito**, che deve garantire affidabilità e prestazioni massime. Tipicamente:
    - I file vengono divisi in *chunks* (ad esempio, da 64MB)
    - Ogni *chunk* viene replicato (es. 2x (due copie) o 3x (copie)) con repliche in nodi e rack differenti per assicurare massima affidabilità;
    - Come i *chunk* vengono distribuiti tra i nodi è definito nel **Master Node File**, che è a sua volta replicato. Una directory (che è a sua volta replicata) registra dove i nodi master si trovano.
    - Esempi sono Google File System e Hadoop Distributed File System

Il framework più popolare ed utilizzato per i Big Data è Apache Spark, che usa Hadoop Distributed File System e supporta MapReduce.

Il corso userà il paradigma MapReduce implementato tramite Spark.


## MapReduce Computation
Un calcolo in MapReduce è visto come una sequenza di round, in ognuno dei quali viene trasformato un insieme di dati chiave/valore in un'altro insieme sempre chiave/valore. Quindi, ogni round rappresenta una trasformazione sui dati. Ogni round si compone di due fasi:
- Fase *Map*, in cui una funzione *map* definita dall'utente viene applicata ad ogni input chiave-valore e produce un numero $\ge 0$ di altre coppie chiave-valore, chiamate **intermediate key-value pairs**
- Fase *Reduce*, in cui ogni *intermediate key-value pair* vengono raggruppati per chiave e una funzione *reduce* (definita dall'utente) è applicata separatamente ad ogni gruppo di coppie chiave-valore aventi la stessa chiave (in quanto appunto raggruppate secondo essa), producendo $\ge 0$ altre coppie chiave-valore, che sono l'output del round.

### Why Key-Value pairs
La necessità di rappresentare i dati mediante chiave-valore deriva dal fatto che MapReduce è un framework data-centric e si concentra su trasformazioni di dati che sono indipendenti da dove i dati sono residenti (cioè in che nodo). Le chiavi servono quindi per identificare gli oggetti, come se fossero indirizzi per i dati. Inoltre, nella fase *reduce*, le chiavi servono per raggruppare i dati ed applicare la funzione *reduce* separatamente.

Inoltre, così facendo, si spinge sul parallelismo: *Map* può essere applicata su ogni elemento indipendentemente e *Reduce* su ogni gruppo di elementi indipendentemente, pertanto il calcolo può essere parallelizzato.

Alcune considerazioni:
- La scelta della rappresentazione chiave-valore è cruciale
- Spark permette di gestire i dati senza usare le chiavi, anche se esse vengono rimpiazzate da valori (che servono come indirizzo) "invisibili" al programmatore.
