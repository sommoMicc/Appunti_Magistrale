# Lezione 2
 > 03 ottobre 2019

 ## 5G requirements
 Per la definizione degli standard generazionali dei sistemi cellulari ci sono più gruppi di persone che collaborano:
 * __3GPPP__, che sono un gruppo di produttori (che pagano una tariffa per rimanerci). Ogni documento di standard viene prima creato da questo gruppo. Al suo interno ci sono i seguenti gruppi:
    * Technical Specification Group che, sia grazie all'apporto di individui che di organizzazioni/aziende partner, dichiarano gli standard. Ovviamente, se un'azienda propone un sistema da lei brevettato (Qualcomm ad esempio) e questo poi viene standardizzato, essa avrà diritto a un guadagno brevettuale. Per il 3G, ad esempio, per ogni singola unità di cellulare realizzata che supporta il 3G, il produttore deve dare qualcosa come $1 a Qualcomm (che detiene il brevetto). Facendo così in realtà si crea una sorta di giustizia, perché si prende soldi solo dalle tecnologie effettivamente utilizzate [ad esempio il WiMax che non è mai decollato non è redditizio];
    * Project Co-ordination Group, in cui partecipano anche i legislatori (stati);
 * __International Telecomunication Union (ITU)__, che realizzano gli standard in base a quanto "suggerito" dai **3GPP** (in pratica approvano le proposte del **3GPP**)

 Lo sviluppo dello standard (che ha portato al 5G) è in realtà un processo continuo. Basti pensare che il **3GPP** sta ancora apportando modifiche allo standard GSM, 3G, 4G ecc.. Ogni 6 mesi, il **3GPP** rilascia un documento chiamato "Release" (numerato in ordine crescente, attualmente siamo al 16), in cui si trova un'evoluzione dello standard. Ad esempio, nella *Release 15* viene definita una parte dell'architettura 5G (radio, architettura), mentre nella *Release 15* (che è work in progress) sta venendo definita l'architettura di rete di base e le funzioni della stessa.

 Alla fine, una release è un insieme di documenti chiamati **Technical Specifications** (*TS*) che raggruppa le funzionalità del sistema. Molto spesso gli standard riguardano solo la trasmissione/trasmettitori, non la ricezione (che è una sorta di conseguenza).

 ## What is 5G
 Il 5G nasce da un programma (chiamato IMT-2020) nato nel 2008 dall'agenzia statunitense specializzata in ITC (si chiama ITU). L'ITU definisce obiettivi abbastanza generali, talmente generali che alcune generazioni di WiFi possono essere considerate come 3G o 4G (basta che rispettino i datarate definiti e i requisiti di mobilità in pratica). 
 Gli obiettivi del 5G sono:
 * Un datarate elevato (nell'ordine dei Gigabit/s), quindi un incremento rispetto al 4G (seguendo il trend di aumento di velocità tipico di ogni nuova generazione)
 * La possibilità di supportare comunincazioni critiche, caratterizzate da un datarate basso ma da una altissima affidabiltà (poche perdite) e da una bassissima latenza (basso ritardo di recapito in pratica). Questa caratteristica, ad esempio, è usata per le macchine a guida autonoma
 * La possibilità di comunicazione tra un numero elevato macchine connesse (Massive Machine Type Communications) per l'IoT. Lo standard deve quindi deve supportare un numero elevato di comunicazioni, caratterizzato da un basso e sporadico datarate, un'alta efficenza energetica (ad esempio uno smartphone quando è connesso ad una stazione invia un sacco di bit di controllo, ma questo non è accettabile per un sensore con batteria limitata). 
 *  Rete più agile, "semplificando" la vita agli operatori, facendo si che essi possano inventare nuove modalità di utilizzo della stessa (coming soon...).

 Riepilogando:
 * La latenza deve essere <1ms (contro i 10ms medi del 4G)
    * Nel 4G la latenza è suddivisa in:
        * 4ms nello smartphone (per prepararsi alla comunicazione);
        * 4ms per la trasmissione nella rete: tempo di pachettizzazione dei bit, di codifica e di trasmissione del pacchetto. Il punto è che il tempo è diviso in slot, quindi possono essere trasmessi solo pacchetti di n-bit alla volta. Il ricevitore deve quindi aspettare di ricevere tutti gli n-bit del pacchetto prima di poterli decodificare e quindi processare (ritrasmettere). Questo processo aggiunge latenza;
        * anche 10ms per il transito nella rete core e in Internet.
    * Per il 5G invece:
        * La dimensione minima dei pacchetti è ridotta, quindi posso accellerare il processo di decodifica. Inoltre, vengono aggiunti dei self-correcting error bit che permettono di scoprire (e a volte correggere) gli errori. Questo dovrebbe permettere di arrivare ad una latenza <0.5ms per la trasmissione
        * Grazie all'edge-computing (mettere server vicini alla stazione base che replicano il servizio richiesto), la latenza per l'accesso al contenuto (che nel 4g è il tempo di accesso ad internet) è ridotta in modo considerevole.
 * Il traffico deve essere nell'ordine dei 50 Exabytes/mese (contro i 7.2 Exabyte/mese del 4G);
 * Il data rate massimo (di picco) deve essere nell'ordine dei 20Gb/s (contro il 1 Gb/s del 4G);
 * Lo spettro di frequenze disponibili deve eessere incrementato a 30 GhZ

Il target del 5G è abbastanza generico, anche perché le generazioni precedenti sono state fallimentari nella predizione degli usi: il 3G era nato per le videochiamate, il 4G per rimpiazzare l'ADSL di casa (entrambi gli scopi sono falliti in pratica). 

## 5G Architecture
* Prima di tutto, c'è una separazione tra l'*User Plane* e del *Data Plane*. Il primo è qualcosa che c'entra con i dati, mentre il secondo è qualcosa collegato con il controllo della rete (richiesto per il funzionamento della rete). Ad esempio, il contenuto dello stream IP appartiene al *Data Plane*, mentre l'overead di *IP* (tipo tutte le informazioni accessorie contenute in un frame IP) appartiene al *Control Plane*. Questa separazione di concetti serve per aumentare la scalibilità;
* Il design viene modularizzato, permettendo di astrarre alcune funzionalità e portarle a livello di rete, implementandole come servizi (ad esempio il network slicing) **PARTE CONFUSA**
* Minimizzare le dipendenze tra l'**Access Network** (l'antenna/cella) e la **Core Network** (la rete che c'è dietro l'access point). Questo serve anche ad aumentare l'interoperabilità tra due dispositivi (ad esempio antenne) fabbricati da due produttori diversi.
* Unificazione delle funzioni di rete: questo si è reso necessario perché, per ridurre la latenza, si fanno più operazioni "vicino ad essa", quindi c'è bisogno di standardizzare queste operazioni. Nel 4G tutto questo non è possibile perché tutto era concepito come una singola connessione ad Internet. Con la modularizzazione si è semplificata anche la vita degli operatori, poiché essi possono (ad esempio) cooperare/condividere parti dell'infrastruttura in maniera molto più semplice.

La modularizzazione causa anche la separazione tra i compiti: non c'è più solo l'operatore e l'utente, ma ci sono molti più strati in mezzo. Ad esempio, c'è il *Communication Service Provider* (che è il soggetto che fornisce un determinato servizio all'utente), il *Network Operator* (l'operatore di rete, che fornisce i servizi al communication service provider), il *Network Equipment Provider* (che fornisce l'infrastruttura di rete, come ad esempio le antenne), il *Data Center Provider* (importante perché i dati dovranno essere replicati vicino all'utente per ridurre la latenza).

Alcune delle funzionalità di rete previste sono:
* Network Exposure Function (NEF), grazie alle quali si può accedere dall'esterno alle funzionalità di rete. Ad esempio, grazie alla rete cellulare si può essere localizzati. Attualmente questo deve avvenire grazie ad un permesso concesso dallo smartphone, mentre grazie alle NEF questo potrebbe avvenire grazie ad una comunicazione diretta tra il server e la rete alla quale si è connessi ("saltando" il passaggio dello smartphone). Un altro esempio è la possibilità di switchare tra telefonate VoIP (tipo via WhatsApp) e tradizionali in modo automatico (non gestito dallo smartphone ma dal service provider, tipo WhatsApp).

Nota: *NG-RAN*: New Generation Radio Access Network

Il *Network Slicing* consiste nello "tagliare" la rete in pezzi, ciascuno delle quali ha un insieme di funzionalità. In pratica, divide la rete in sottoreti. I tipi di pezzi che sono stati definiti sono tre e sono:
* *Enhance Mobile Broadband*, che supporta un alto datarate (senza garanzie di latenza);
* *Ultra-Reliable Low Latency Communications*, che supporta comunicazioni molto affidabili con bassa latenza (ma senza un alto datarate);
* *Massive IoT*, che supporta molti utenti con bassa latenza (senza un alto datarate) e alta efficenza energetica.

Molti di questi pezzi condividono lo stesso hardware, ma il software è programmato in modo diverso. Quindi, per cambiare "tipo" di fetta basta solo riprogrammare/riconfigurare il software, ottenendo un'astrazione ancora maggiore.