# Introduzione al corso
Il datamining è il processo di individuazione di pattern e relazioni tra i dati raccolti in insiemi (database o dataset) di dimensioni potenzialmente molto elevate, anche a fini di previsione di andamenti futuri.

Ci sono molte definizioni "diverse" di data-mining, ma in tutti c'è il concetto ricorrente di riconoscimento di pattern e aver a che fare con dataset/database di grandi dimensioni.

Il datamining suscita interesse perché ultimamente si sono diffusi i *data warehouses*, ovvero "grandi magazzini" di dati (commerciali, bancari, finanziari) ad raccolti ad alta frequenza (ovvero poca distanza temporale tra l'inserimento dei record, quindi dati molto frequenti, quindi tanti). Analogamente, in ambito scientifico, esistono dati raccolti tramite ricerche scientifiche. Molto importante processare i dati velocemente e in modalità parallela.

Data-mining non è una disciplina "isolata", ovvero si rapporta con altre discipline per due motivi:
- *Gli strumenti e le metodologie alla base del DataMining* derivano per molti aspetti dalla statistica. Tuttavia, statistica non è datamining, e datamining non è statistica! Secondo Hand, la statistica si occupa della **primary data analysis** (la raccolta dati è mirata allo studio/risoluzione di un problema), mentre nel data-mining prima i dati vengono raccolti, poi si analizzano e si cercano relazioni tra essi (**secondary data analysis**). Il problema è che, analizzando tanti dati a posteriori, si è molto suscettibili al rumore dei dati.
- Data la natura dei dati gestiti, il data-mining è a contatto con database, machine-learning, IA e in generale molte discipline informatiche

## Data Mining vs Machine Learning
Entrambe le discipline hanno come obiettivo quello di estrare informazioni dai dati che trattano, ma sono due cose diverse. In particolare:
- Lo scopo del *machine learning* si occupa della creazione di algoritmi che estraggono informazioni dai dati in **modo automatico**. In generale, *ML* si concentra sul costruire software che impara in modo automatico dai dati. 
- Lo scopo del *data mining* è quello di cercare caratteristiche interessanti di grandi insiemi di dati, cercando appunto relazioni e schemi tra variabili, validando i risultati su nuovi insiemi di dati e fornendo previsioni. L'analisi è condotta **da un soggetto che ha in mente un obiettivo**, sia esso la spiegazionedi caratteristiche dei dati o la previsione.

A volte ML e DM usano strumenti simili, ma ciò non vuol dire che le discipline siano equivalenti!

## Esempio 1: Walmart
Walmart è una catena di grande distribuzione, e raccoglie una caterva di dati ogni ora (2.5 petabyte di dati ogni ora!). Le strategie di datamining adottate hanno lo scopo di:
- Individuare le modalità di offerta migliore negli store e nell'online
- Valutare le strategie di stoccaggio di prodotti, per soddisfare sempre la domanda di prodotti evitando di accumularne alcuni inutili
- Prevedere le variazioni di acquisto in base ad eventi esterni, come il **coronavirus**, il **Super Bowl**, **Tornado** ecc..
- Individuare offerte ritagliate sulle caratteristiche di acquisto del cliente in base alla sua cronologia degli acquisti.
- Individuare nuovi prodotti da inserire negli store sulla basedelle informazioni circolanti sui social media


## Esempio 2: EOSDIS
Earth Observing System Data and Information System: funzionalità della NASA con lo scopo di archiviare, gestire e distribuire dati raccolti sulle scienze della terra, raccolti in modo automatico da satelliti, veivoli e strumenti di misurazione al suolo. In media, ogni giorno EOSDIS distribuisce 28TB di dati a circa 11 mila utilizzatori nel mondo.

## Esempio 3: Valutazione del rischio di credito
In base alle analisi che la banca svolge su ogni soggetto, viene classificato in buono o insolvente

## Esempio 4: Microarrays
I DNA Microarrays sono dataset che contengono risultati di esperimenti ricavate da 5mila-40mila geni misurati su 50-100 campioni biologici.Il risultato è una Heatmap che mostrano l'espressione genica di ogni campioni. Lo scopo, ad esempio, potrebbe essere quello di individuare i campioni tumorali.

## Altri esempi
Cose inutili!!

# Software R
Software che nasce per rispondere alle esigienze di analisi statistiche. [Questa](www.r-project.org) è l'homepage del software. La figata di R è che è gratuito ed open-source multipiattaforma.

La versione da scaricare è quella base + libreria ISLR (che contiene, tra le altre cose, i dataset).