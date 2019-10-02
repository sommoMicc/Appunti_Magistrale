# Apprendimento automatico
> 02 Ottobre 2019

> L'esame è a domande aperte. Durante l'anno vengono proposti degli esercizi per acquisire "punti esperienza", che servono a skippare il progetto.
In caso, il progetto è cumulabile ai punti esperienza. Siccome la parte pratica (punti esperienza/progetto) vale 8 punti, l'esame da al massimo 22 punti.

## Introduzione
Il funzionamento del machine learning si basa su un ragionamento induttivo. Ecco un excursus sui vari tipi di ragionamento

## Evoluzione dei ragionamenti
### Ragionamento Deduttivo
Il primo tipo di ragionamento (coniato da Aristotele) è chiamato ragionamento deduttivo. Si parte da assunzioni vere (in quanto dimostrate o assiomi) e si deducono nuovi teoremi mediante dimostrazione.
L'esempio più comune è:
* __Regola__: Tutti gli uomini sono mortali
* __Caso__: Socrate è un uomo
* __Risultato__: (quindi..) Socrate è mortale!

un altro esempio è:
* __Regola__: Tutti i malati di lupus muoiono in 5 giorni
* __Caso__: Il paziente ha il lupus
* __Risultato__: (quindi..) il paziente muore in 5 giorni

Queste tecniche sono usate nell'intelligenza artificiale classica
### Ragionamento induttivo
Il secondo tipo di ragionamento, quello più utilizzato al giorno d'oggi, è l'induzione, coniato dal filosofo F.Bacon (cazzo me ne frega):
* __Caso__: Socrate è un uomo
* __Risultato__: Socrate morì
* __Regola__: (quindi...) Tutti gli uomini sono mortali

un altro esempio è:
* __Caso__: Il paziente ha il lupus
* __Risultato__: Il paziente è morto in 5 giorni
* __Regola__: (quindi...) Tutti i pazienti ammalati di lupus muoiono in 5 giorni

In questo tipo di ragionamento viene fatta una generalizzazione: si parte da un caso particolare (la morte di socrate) che fornisce evidenze a sostegno della conclusione (tutti gli uomini sono mortali). Siccome viene fatta una generalizzazione, potrebbero essere introdotti degli errori di approssimazione, quindi partire da premesse "corrette" e giungere a risultati errati.
Questo tipo di ragionamento è usato nel ML.

### Ragionamento abduttivo
L'utlimo tipo di ragionamento, quello abduttivo, è stato coniato a metà 800 da uno sfigato qualsiasi. Qua si suppone che le implicazioni valgano bidirezionalmente (a -> b quindi b -> a). Ad esempio: 
* __Regola__: Tutti gli uomini sono mortali
* __Risultato__: Socrate morì
* __Caso__: (quindi...) Socrate è un uomo

un altro esempio è:
* __Regola__: Tutti i malati di lupus muoiono in 5 giorni
* __Risultato__: Il paziente è morto dopo 5 giorni
* __Caso__: (quindi...) Il paziente aveva il lupus

è un po' tipo la diagnosi del dottore: partendo da una regola (malattia) e dalla sua conseguenza (sintomi), si cerca di risalire alla causa (virus/batterio responsabile della stessa).

## Cos'è il Machine Learning
Il machine learning può essere sia un task di descrizione di dati (classificazione di dati) che di predizione degli stessi (se si presenta un dato mai visto prima, capire di che tipo è) [specifico meglio dopo].

In ogni caso, deve esistere un processo (anche stocastico) che regola i dati che osserviamo, ovvero che li "spieghi", che ne dia un significato. Lo scopo del 
machine learning è quello di approssimare al meglio possibile il processo (non necessariamente uguale, ma una replica che sia utile a raggiungere l'obiettivo), senza dover per forza riprodurlo (come la metafora dell'uccello e dell'aereo).

*Stocastico*: random a probabilità

L'obiettivo finale del machine learning è quello di definire dei criteri
da ottimizzare in modo che sia possibile andare a migliorare dei modelli
definiti su certi parametri.
Questi modelli possono essere:

* **Preditivi**: per fare previsioni sul futuro (es: filtro anti-spam)
* **Descrittivi**: utilizzare dei dati per ottenere maggiori informazioni (data mining)

Nel machine learning ci sono varie definizioni. Le più importanti sono:
* << Il Machine Learning è il campo di
  studio che dà ai computer l’abilità di
  apprendere (a realizzare un compito)
  senza essere esplicitamente
  programmati a farlo>>
* << Un programma impara da un’
  esperienza E rispetto a dei compiti T
  ottenendo una performance P, se
  quest’ultima migliora con l’esperienza E>>

Il machine learning nasce da dei "buchi applicativi" lasciati dagli algoritmi. Formalmente, un algoritmo è "una sequenza ordinata e finita di passi (operazioni o istruzioni) elementari che conduce a un \emph{ben determinato} risultato in un tempo finito".

Infatti, non sempre è possibile utilizzare degli algoritmi per risolvere un problema, per vari motivi:
* non sempre si può formalizzare un determinato problema
* ci sono delle situazioni di incertezza
* risulta troppo complesso trovare una soluzione oppure sono richieste troppe risorse

Alcuni esempi sono: riconoscimento facciale, filtro anti-spam.

In questi casi gli algoritmi (sequenza finita di passi che portano ad un risultato determinato in un tempo finito) non funzionano (o sono talmente tanto complessi da essere quasi impossibili da implementare o altamente inefficienti) ed è quindi preferibile fornire una soluzione "*imperfetta*".

In apprendimento automatico si studiano i metodi per trasformare l'informazione empirica (dati del problema) in conoscenza. In generale, in ML, quando i dati sono pochi la soluzione non funziona.

Grazie alle reti di computer (soprattutto internet), oggi si hanno a disposizione molti dati, anche per questo le tecniche di machine learning funzionano "meglio".



## Le basi

Perché il machine leargning funzioni deve esserci un processo (stocastico o deterministico) che spiega i dati che osserviamo, in modo da riuscire a costruire un'approssimazione di tale processo che può anche risultare imperfetta dal momento che il processo che si vuole approssimare non è noto.

*Stocastico*: random a probabilità

L'obiettivo finale del machine learning è quello di definire dei criteri da ottimizzare in modo che sia possibile andare a migliorare dei modelli definiti su certi parametri.


Esempi applicativi:

* Software OCR
* Estrapolazione di dati a partire dal linguaggio naturale
* Riconoscimento facciale
* Giochi con informazione incompleta (Gaist? gioco con fantasmi rosso/blu, tedesco)

## Problemi tipici dell'apprendimento automatico
[Non serve neanche saperli in realtà, sono più per curiosità]
* **Classificazione binaria**: dato un input dire se appartiene ad una determinata classe o meno. Esempio: data una cifre dire se è uno 0 o meno.
* **Classificazione multiclasse**: dato un input lo assegno ad una determianta categoria. Es: identificare una cifra manoscritta.
* **Regressione**: dato un insieme di valori, trovare una funzione che li approssimi.
* **Ranking di classi** (non sarà affrontato): data una serie di dati, dire quali sono più rilevanti, ovvero, data una serie di documenti ordinarli nel modo migliore secondo una determinata preferenza, es: motore di ricerca.
* **Novelty detection**: riconoscimento delle irregolarità a partire da una serie di dati. es: frode bancaria su una serie di transazioni, controllo degli accessi, ecc.
* **Clustering**: raggruppamento di dati in modo gerarchico, basandosi su alcune caratteristiche che li accomunano o meno.
* **Associazioni**: quello che fa Amazon con "altri utenti hanno comprato"
* **Reinforcement Learning**: valutazioni di strategie, quando si ha una serie di stati e possibili azioni, si vuole valutare la qualità complessiva, es: movimenti di un robot.

Esistono un po' di casi in cui il machine learning ha "mostrato il meglio di sé", ad esempio partite a scacchi o a giochi del cazzo. Ultimamente però va molto di moda il __Generative Adversarial Learning__, ovvero apprendimento con lo scopo di "allenare" reti neurali (Generative Adversarial Network, **GAN**) che creano nuovi contenuti. Ad esempio, con le GAN si è riuscito a scrivere poesie. All'interno delle GAN in realtà ci sono due reti neurali:
* Una generatrice, che genera appunto contenuti
* Una discriminante, che si occupa di capire quali contenuti sono "originali" e quali invece sono stati creati artificialmente dalla rete "generatrice".

Il funzionamento di queste reti è abbastanza "semplice" (concettualmente): la rete generatrice deve creare dei contenuti che "passino inosservati" alla discriminante, ovvero che vengano catalogati da quest'ultima come "originali".