# Agenti logici parte 2
Giovedì 31 Ottobre 2019

## Metodi di prova

Ci sono due tipologie di prove che si possono fare:

- **Model Checking**: viene fatta l'enumerazioe delle tabelle di verita, con una complessità esponenziale in *n* (numero di simboli nella KB), può essere migliorata con euristiche o Hill climbing, ma in questo caso si perde la completezza. 
- **Applicazione di regole di inferenza**: si inizia ad estendere la base di conoscenza utilizzando i dati attuali, se 𝜶 è tra queste nuove sentenze allora viene inferito, altrimenti ripeto il passo utilizzando le nuove informazioni inferite. L'utilizzo di questa strategia risulta più efficiente ma le sentenze devono essere scritte in una forma normale.

Un problema di logica è dato che il computer fa fatica a ricononscere due sentenze equivalenti ma scritte in maniera diversa:

$$ \neg S_1 \lor S_2 \land S_3; (S_1 \implies S_2) \land S_3$$

## Forward e Backword Chaining

Un algoritmo di inferenza si è **completo** quando riesce a derivare tutte le formule derivabili ed è **corretto** (o sounded) se preserva la verità delle formule.

**Forma di Horn**: KB espressa come congiunzione di clausole di Horn. In pratica è una forma normale che semplifica la complessità dell'inferenza logica (complessità polinomiale vs esponenziale). Tuttavia, la forma di Horn non permette di rappresentare tutte le formule logiche, ma una buona parte di esse si.

$$ C \land (B \implies A) \land (C \land D \implies B)$$ 
*espressione nella forma di horn*

**Clausola di Horn**: è un simbolo proposizionale o una congiunzione di simboli che implica un altro simbolo. Una formula è una clausola di Horn quando è una disgiunzione di letterali nella quale al massimo un letterale è positivo. Ogni clausola di Horn può essere scritta come un'implicazione in cui la premessa è una congiunzione di letterali positivi e la conclusione èè un singolo letterale positivo.

> $\neg A \lor \neg B \lor C$ è una clausola di Horn
> 
> (A ⋀ B) => C è la stessa clausola di Horn espressa come implicazione

Le clausole di Horn che hanno esattamente un letterale positivo sono chiamate clausole definite.
Il letterale positivo prende il nome di testa e quelli negativi formano il corpo della clausola.
Una clausola definita senza letterali negativi si limita ad asserire una determinata proposizione e viene chiamata fatto.
Una clausola di Horn senza letterali positivi può essere scritta in forma di implicazione la cui conclusione vale False (utili per definire dei vincoli di integrità, come quello che il Wumpus si trova in una sola stanza).

__Non posso esprimere ad esempio la forma $\neg B \lor \neg A$

**Modus Ponens**: per la forma di Horn: date due formule $\alpha \implies \beta$ e $\alpha$, si può inferire la formula $\beta$. (cioè se l’implicazione e la promessa sono vere, allora anche $\beta$ deve essere vera). È completo per basi di coscenza espresse nella forma di Horn.

La correttezza di questa regola si dimostra considerando i possibili valori di verità delle formule.

![](./immagini/l12-pones.png)

Questo modo dice che se le precondizioni di una regola sono vere allora è vera anche la regola.

Può essere utilizzato per fare *forward chaining* o *backward chaining*, che sono entrambi algoritmi con complessità lineare in tempo.

## Foward Chaining

![](./immagini/l12-albero.png)

L'idea è quella di applicare ogni regola le cui premesse sono soddisfattte nella KB, una volta fatto ciò può essere che alcune regole della KB hanno le promesse soddisfatte grazie alle nuove informazioni precedentemente inserite, fino a quando non viene raggiunto il goal.

Se questo non viene raggiunto vuol dire che la sentenza non è conseguenza logica della KB.

L'algoritmo è rappresentato in figura tramite un _grafo AND/OR_. L'archetto tra A e B dice che sia A che B devono essere veri affinché si possa raggiungere L (tramite un iper-arco, ovvero la freccia con la punta piena (di odio e terrore)).

```
function CP-CA-Implica(KB, q) returns true or false
    locals: conto, una tabella indicizzata per clausola, che contiene inizialmente in numero di premesse
            inferiti: una tabella indicizzata per simbolo in cui ogni elemento è inizialmente false
            agenda: una lista di simboli che contiene inizlamente quelli noti come veri nella KB
    while agenda non è vuota do
        p <- Pop(agenda)
        unless inferiti[p] do
            inferiti[p] <- true
            foreach clausola di Horn c in cui appare la premessa p do
                decrementa conto[c]
                if conto[c] == 0 then do
                    if Testa[c] == q then retrun true
                    Push(Testa[c],agenda)
    return false
```

`Testa[c]` rappresenta quello che la clausola di Horn implica.

Un'osservazione che si può fare su questo algoritmo è che non viene tenuto in considerazione il goal che si vuole raggiungere, semplicemente si va a dedurre il più possibile dalla KB nella speranza che il goal *q* sia deducibile da KB.

Però se nella KB la query *q* non è già soddisfatta (non è un fatto noto) e non ci sono regole di Horn che hanno come conseguenza la query, allora non c'è speranza di riuscire a dedurre *q* dalla KB e quindi l'algoritmo potrebbe terminare subito.

### Completezza

Il forward chaining applicato con il *modus ponens* deriva tutte le conseguenza della KB.

FC raggiunge un punto fisso dove nessuna nuova sentenza atomica è derivata, questo perché il numero di simboli è finito.

Lo stato finale che si raggiunge applicando l'algoritmo si può considerare come un modello *m*, assegnando vero o falso ai simboli che sono stati inferiti.

Ogni clausola definita nella KB originale è vera nel modello creato con questo algoritmo.
Per verificare questo punto basta assumere l’ipotesi opposta, e cioè che qualche clausola *a<sub>1</sub>⋀ ... ⋀ a<sub>k</sub> => b* sia falsa nel modello. 
Allora la premessa deve essere vera e *b* falsa, ma questo contraddice l’assunto che l’algoritmo abbia raggiunto un punto fisso.

Quindi *m* è un modello per KB e se KB |= q, allora q è vere in ogni modello della KB, incluso anche *m*.

## Backward chaining

L'idea è quello di lavorare all'indietro a partire dalla query *q*.

Per provare *q* attraverso la KB, prima si controlla che *q* non sia già conosciuta e nel caso questa non sia conisciuta, si provano trammite la KB tutte le premesse si una regola che deriva *q*.

È importante evitare i cicli, bisogna quindi controllare se un nuovo sotto goal è già presente nella pila dei goal.

Si può anche ottimizzare il lavoro, se ho un nuovo sottogoal posso controllare se l'ho già provato vero o se è già fallito.

Non è stato presentato un algoritmo a lezione perché una implementazione del Backward chaining è molto complessa.

## Forward VS Backward Chaining

Forward è più orientata ai dati e viene utilizzata per l'elaborazione incoscia e automatica, come il riconoscimento dei dati.

A causa dell'approccio utilizzato viene eseguito del lavoro irrilevante per il goal, cioé vengono dedotte molte conseguenze logiche che non sono rilevanti per il goal (come se fosse una ricerca a ventaglio).

Backward è invece focalizzato sul goal, per questo motivo è più adatto al problem solving e la complessità di questa strategia può essere molto minore che lineare nella complessità di KB, perché cerca di restringersi alle clausole rilevanti per raggiungere lo scopo (Forward è lineare). 
