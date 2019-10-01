# Intellegenza Artificiale
01 Ottobre 2019
## Introduzione
<!-->
__Intelligenza artificiale forte__: si vuole sostituire all'uomo la macchina. IBM Watson si avvicina molto a questo ambito.

__Intelligenza artificiale debole__: abilità particolari che una macchina può riprodurre (robot, auto che si guidano da sole).
Attività che possono anche essere semplici da fare ma che sono difficili da eseguire con algoritmi stabiliti a priori.
-->
## Agente Intelligente

Un agente è una entità che percepisce un certo input e riesce a generare un certo output (agisce).

Quando si parla di intelligenza, si possono intendere più ambiti (intelligenza cognitiva, intelligenza emotiva..). Va quindi fissato un ambito in cui poi "specializzare" l'agente

Un agente razionale (o intelligente) cerca di raggiungere i suoi obiettivi data l'informazione disponibile. Non è detto che nel raggiungere il suo obiettivo, l'agente esegua sempre l'azione migliore, in quanto potrebbe non avere una certa conoscenza. In altre parole, esso deve sfruttare al meglio le informazioni che dispone (o che può acquisire) per arrivare alla soluzione migliore possibile correlata alle sue capacità (computazionali/di memoria). Quindi, la soluzione raggiunta dall'agente non è sempre la soluzione ottima assoluta.

Un agente può essere considerato come una funzione che da tutte le possibili sequenze di percezioni estrae delle azioni ammissibili.
> f \: P\* -> A

In questa funzione, la sequenza di percezioni P* rappresenta la conoscenza a disposizione dell'agente.

Tra tutte le classi di ambienti e compiti si va a cercare sempre l'agente che offre le prestazioni migliri, tenendo in considerazione anche tutte le limitazioni computazionali che impediscono la realizzazione di una razionalità perfetta.

Bisogna quindi cercare di progettare il miglior programma date le risorse disponibili.

### Agente e ambiente

L'agente riceve delle percezioni dall'ambiente delle informazioni mediante dei sensori e in base a queste percezioni esegue delle azioni con degli attuatori.

La funzione agente mappa quindi tutte le possibili sequenze di percezioni (_P*_) ad un insieme di azioni (_A_). Il dominio della funzione, quindi l'insieme delle possibili sequenze di percezione, è molto (troppo) grande: l'implementazione dovrà "dimenticarsi" di alcune informazioni non rilevanti (o poco rilevanti), in quanto le risorse a disposizione sono limitate. Se vogliamo, questa (la limitatezza, quindi la necessità di scegliere cosa tenere e cosa no) è la caratteristica per cui l'agente è considerato intelligente (è l' "intelligenza dell'agente").

E' sempre possibile fare assunzioni sull'ambiente in modo da semplificare l'agente, ma questo non sempre è conventiente in quanto l'agente diventa più fragile.

### Il mondo dell'aspirapolvere

Per l'esempio dell'aspirapolvere, le percezioni che dobbiamo considerare sono:
* La stanza in cui si trova il robottino
* La presenza (o l'assenza) di polvere

Le azioni che si possono intraprendere invece:
* Andare a destra
* Andare a sinistra
* Aspirare

<table>
<th>Percept sequence</th><th>Action</th>
<tr><td>[A,Clean]</td><td>Right</td></tr>
<tr><td>[A,Dirty]</td><td>Suck</td></tr>
<tr><td>[B,Clean]</td><td>Left</td></tr>
<tr><td>[B,Dirty]</td><td>Suck</td></tr>
<tr><td>[A,Clean],[A,Clean]</td><td>Right</td></tr>
<tr><td>[A,Clean],[A,Dirty]</td><td>Suck</td></tr>
</table>

Quello che è interessante è che conta solo l'ultima percezione: se la stanza in cui mi trovo è sporca, devo aspirare (a prescindere se la stanza in cui mi trovavo in precedenza era sporca o pulita). E' possibile dunque "scartare" tutti i record storici dalla memoria, cosicché con risorse limitate si ottenga un agente razionale che raggiunge lo scopo di pulire le due stanze (quando entrambe le stanze sono pulite, continua ad andare a destra e a sinistra finché non finisce la batteria but, it's a feature XD).

### Razionlità

Fissata una misura per la prestazione che valuta la sequenza di percezioni (una sorta di score/punteggio che indica in soldoni quanto bene sto andando), un agente razionale cerca di massimizzarne il valore. Nell'esempio precedente potremmo applicare: 
* +1 ad un determinato score per ogni spazio pulito in tempo T
* +1 per ogni spazio pulito in T ma -1 per ogni spostamento (penalizzo lo spostamento della stanza che ho già pulito)
* ...

Da notare che l'ultima opzione, che può sembrare la migliore è valida se le stanze sono sigillate (ovvero rimangono pulite per sempre) e se l'aspirazione riesce a pulire al 100% la stanza. Per questo la misura di prestazioni dipende molto dalle caratteristiche dell'ambiente!

La misura delle prestazioni deve essere effettauta sulla sequenza delle percezioni ottenute, questo perché l'agente deve essere valutato in basa alla sua conoscenza (non è omniscente/chiaroveggente).

Per lo stesso motivo la razionalità e le prestazioni non sono influenzate dal successo.

### PEAS - Performance Enviroment Actuatos Sensors

Sono le caratteristiche da tenere a mente quanto ci si trova a progettare un'ambiente intelligente.

__Pensando ad un taxi automatizzato__
* Misura delle prestazioni? **Obiettivo che l'agente deve ottenere:** _sicurezza, destinazione, profitto_
* Ambiente operativo? _strade, traffico, pedoni, condizioni meteo_
* Attuatori? **Azioni che può intraprendere** _volante, acceleratore, freni, ..._
* Sensori? **Informazioni che può acquisire** _telecamera, accelerometro, GPS, ..._












