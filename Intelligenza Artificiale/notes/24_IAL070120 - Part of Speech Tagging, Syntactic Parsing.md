# Part of Speech Tagging, Syntactic Parsing con Deep Learning

Martedì 7 gennaio 2020

## Natural Language Processing

Un modello BoW non è abbastanza buono per la comprensione del testo, perchè il contesto delle parole viene perso.
Il primo task è il tagging delle parti del parlato: riconoscere il ruolo delle parole all'interno della struttura della frase. A questo segue un'analisi sintattica, a cui dovrebbe seguire (ma siamo ancora lontani!) un'analisi semantica soddisfacente e infine, considerando più sentenze unite, determinare la struttura del discorso.
Il Deep Learning ha boostato i progressi ma è disruptive rispetto ai metodi sviluppati in passato.

## Parts of Speech (POS, Parti del discorso)

Sono sostantivi, verbi, aggettivi, preposizioni, avverbi (in pratica quello che alle medie chiamavo analisi grammaticale). Nota: POS = Part Of Speech.

Nella slide viene mostrato un esempio di etichettatura, dove la prima colonna rappresenta l'etichetta attribuita (N, V, AJD), la seconda la descrizione in inglese dell'etichetta e l'ultima contiene esempi per quell'etichetta.

Una Part of Speech è una parola/gruppo di parole che condividono la stessa funzione nella sentenza. Distinguiamo:

- Classi **closed**, definite e immutabili. Caratterizzano la struttura della frase, quindi differiscono in maniera più marcata tra una lingua ed un'altra;
- Classi **open**, che possono mutare nel tempo: ad esempio posso inventarmi un nuovo nome proprio mai visto prima, o neologismi (petaloso) ecc. In questa casse ci sono nomi, aggettivi, avverbi.

Le parti del discorso sono molteplici, quindi serve un criterio per raggrupparle. Per farlo bisogna scegliere un set standard di tag (tagset) con cui lavorare. Esistono molteplici tagset, sia a grana molto grossa (pochi raggruppamenti, tipo "nomi, aggettivi, verbi e pronomi") che a grana molto fine.
Una via di mezzo è il Penn TreeBank tagset, che comprende 45 tag.

## Etichettatura (tagging)

Processo di assegnazione di un marcatore di parte del disocrso o di classe lessicale a una parte del corpus. Il problema è che, in base al contesto, le parole hanno spesso più di un POS. Ad esempio, per la parola **back**:

- The back door: JJ
- On my back:
- .....

Su un corpus di esempio, si nota come circa l'11% delle parole hanno un'etichetta POS ambigua.

Le tecniche per il POS tagging sono:

- Il **rule-based tagging** procede per eliminazione: una volta selezionato il dizionario, si assegnano tutti i tag possibili alle parole del dizionario, e poi grazie a regole "scritte a mano" (decise staticamente/a priori) vengono eliminati selettivamente i tag "in più".
- Un **approccio statistico semplice**, che seleziona per ogni parola il tag più frequente (quindi quello più probabile).
- Un **approccio statistico semplice alternativo**, che cerca di trovare la sequenza di etichette in modo che la probabilità a posteriori che le etichette siano corrette sia massimizzata. Per questo si usano il teorema di Bayes e le catene di Markov (indipendenza condizionale rispetto alla posizione delle parole). La catena di Markow però restringe il contesto, in quanto considera solo quanto scirtto a sinistra della parola.
- Un **approccio basato su classificazione con _sliding window_**: l'idea è usare un corpus di sentenze per allenare un classificatore che determina qual'è il tag da assegnare alla parola in base al contesto. Il contesto in questo caso è contenuto nella sliding window, che contiene la parola precedente, quella corrente e quella successiva.
- Un **approccio basato su classificazione con output in input**: se al posto delle parole avessimo già la POS corretta della parola precedente e successiva, il compito di classificazione è più semplice/efficace. Tuttavia, l'apposizione di queste etichette è esattamente il compito del classificatore, quindi esse non sono disponibili a priori. Pertanto esistono degli approcci che funzionano a "passate":
  - Con una prima passata si assegnano i POS, avendo come input le parole (come nella sliding window);
  - Con delle passate successive si usano i POS precedentemente assegnati per rifinire la classificazione.

## Syntactic Parsing

Teorie linguistiche della sintassi:

- Constituency: cerca di identificare le componenti fisiche della frase, per poter poi attribuire ad esse una data semantica;
  - Consideriamo gruppi di parole che possono essere mostrati come singole unità: frasi nominali, "a course"....
- Dependency: identifica il ruolo delle parole all'interno della POS.
  - Considerano le relazioni binarie tra singole parole in una frase. Ad esempio "Missed -> I"

## Constituency

La struttura della frase organizza le parole in componenti annidate. L'idea quindi è di utilizzare una grammatica per cercare, bottom-up, di ricostruire l'albero di parsing. Ahimé non c'è un unico modo di generare la stessa sentenza. Ovvero, le grammatiche sono ambigue e quindi ci sono più alberi di parsing per una sola sentenza.

## Dependency

Un albero/grafo di analisi delle dipendenze è una struttura ad albero o grafo non radicato in uci:

- I nodi sono parole con POS già applicati
- Gli archi sono dipendenze tra parole. L'etichetta di un arco specifica il tipo di dipendenza:

  - **argument**: subject, object, indirect object,..
  - **modifier**: determiner, noun modifier, ..

## Algoritmi di parsing per _constituency_

Gli approcci classici utilizzavano grammatiche + lessici, ad esempio grammatiche Context-Free (CFG), oppure grammatiche più ricche (ma portano ad un'esplosione combinatoria, quindi di fatto sono computazionalmente più proibitive).

Il problema è che questi sistemi non scalano, quindi sono potenzialmente difficili da usare, e inoltre hanno una scarsa copertura, cioè hanno molte sentenze che non appartengono al linguaggio generato dalle grammatiche di partenza (circa il 30%) (per questo motivo le grammatiche CFG sono state arricchite da un po' di info sul contesto).

Più recentemente si è passati ad usare approcci statistici, basati su Probabilistic CFG. In pratica si usano grammatiche meno vincolate, che quindi producono più parsing (troppe, senza dare indicazione di quale albero di parsing generato è migliore degli altri). Utilizzando la teoria della probabilità, si cerca il parsing più probabile.

Problema: come stabilire le probabilità?
Vengono usate stime da corpus di sentenze. In particolare, in questo contesto dobbiamo definire in che modo calcoliamo la probabilità per gli alberi di parsing e per le stringe di parole:

- P(t) è il prodootto delle probabilità di tutte le regole di produzione di _t_
- P(s) è la somma delle probabilità che producono _s_ come output.

## Concke-Kasami-Younger Parising (CKY)

Per gestire tutto quanto si usa un parsing bottom-up con programmazione dinamica per evitare di ripetere più volte la stessa elaborazione. Un algoritmo è CKY e ha complessità $O(n^3|G|)$. No implementazione

## Algoritmi di parsing per dependency

Per le dipendenze si usa un grafo:

- Connesso
- Aciclico
- Ogni parola ha al massimo una testa sintattica (ognuno ha un solo genitore)

Gli algoritmi di parsing utilizzano la programmazione dinamica, andando a cercare in maniera efficente tra lo spazio degli alberi da ottimizzare, con dipendenze tramite componenti (stile CKY) e sticazzi.

## Deep Learning per Machine Translation

Me so perso.
