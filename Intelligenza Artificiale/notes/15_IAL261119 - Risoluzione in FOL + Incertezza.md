# Lezione 18 - Risoluzione in FOL + Incertezza

Martedì 26 Novembre 2019

Anche in FOL è possibile applicare la regola di risoluzione, con la differenza che vengono ridotti due predicati, che una volta unificati sono tra loro complementari. Ovviamente, se i due predicati non unificano, non si può applicare la regola di risoluzione.

## Conversione a CNF

Per poter applicare la risoluzione è necessario che la base di conoscenza sia in CNF.

Per passare alla CNF:

1. Eliminare le implicazioni. Nell'esempio, al passo 1, sono state eliminate due implicazioni: quella esterna e quella all'interno delle parentesi tonde dentro le quadre.
2. Spostare la negazione all'interno, tenendo conto dei vari quantificatori che possono essere negati. Nel senso, la negazione del $\forall$, cioè $\lnot \forall x, p$, è equivalente all'esiste della sentenza negata $\exists x \lnot p$
3. Standardizzare le variabili.
4. **Skolemizzare**: ogni variabile esistenziale viene sostituita con una costante di Skolem. Se la variabile esistenziale è all'interno di un quantifiatore esistenzale è necessario utilizzare una **funzione di Skolem**, che va a sostituire tutte le variabili esistenziali che sono all'interno di un qunatificatore universale. $F$ è un simbolo non presente nella base di conoscenza, e funge da "generatore" di costanti di _Skolem_.
   Nella quadra, la funzione "F" è la stessa tra _Animal_ e _Loves_ perché sostituiscono una variabile che si trova all'interno dello stesso scope (cioè la y è la stessa).
5. Rimuovere i quantificatori universali.
6. Distribuire ⋀ su ⋁.

![](./immagini/l18-conv-1.png)
![](./immagini/l18-conv-2.png)

Se un quantificatore esistenziale si trovata all'interno di due quantificatori esistenziali $\forall x,q$, le funzioni di Skolem devono ricevere due parametri $F(x,q)$.

L'algoritmo di inferenza rimane sempre lo stesso, per provare KB|=𝜶, si cerca di provare $KB \lor \lnot \alpha$, se viene generata la clausola vuota, allora KB|=𝜶.

## Esempio di risoluzione

![](./immagini/l18-esempio.png)

## Strategie di appplicazione della regola di risoluzione

Nella logica proposizionale si può puntare a raggiungere un punto fisso per provare a generare la clausola vuota, tuttavia applicare questa strategia nella logica del primo ordine porta ad un'esplosione combinatoria.

Con il tempo sono state quindi sviluppate varie strategie di risoluzione:

- **Unit clause**: si _preferisce_ effettuare la risoluzione con una delle sentenze costituite da un singolo letterale, in modo da avere diminuire la dimensione delle clausola risolvente. Questa strategia è **completa** perché preferisce la clausola unitaria, se non è possibile si continua in modo normale.
- **Unit Resolution**: si esegue la risoluzione coinvolgendo **sempre** una clausola unitaria (**incompleta** in generale, ma completa per le clausole di Horn).
- **Set of support**: utilizza un set di supporto dal quale vengono prelevate le sentenze e dove venogno posti i vari risolventi. Inizialmente il set di supporto è composto dal goal (!𝜶). L'idea è quella di effettuare delle risoluzioni che sono utili per arrivare alla clausola vuota. **Completo** perché vengono fatte solamente delle scelte che portano alla risoluzione.
- **Input resolution**: combina sempre una sentenza di input (KB e Query) con il risolvente corrente. **incompleta** in generale, ma completa per le base di conoscenza in forma di Horn.
- **Linear resolution**: come l'input resolution ma ammette anche la combinazione del risolvente con uno dei suoi avi, ottenendo così una strategia **completa**.
- **Subsumption**: elimina tutte le sentenze che sono _subsumed_ (più specifiche di altre), in modo da diminuire il numero di clausole da gestire. Es: se ho sia _P(A)_ che _P(x)_, posso rimuovere la clausola _P(A)_.

In ogni caso se la KB contiene una funzione e non implica 𝜶, allora l'algoritmo non termina.

## Completezza della Risoluzione

Non vediamo la dimostrazione completa.

![](./immagini/l18-dim.png)

La dimostrazione parte dal fatto che se l'insieme delle clasule _S_, espresse in FOL, è indosddisfacibile, per il teorema di Herbrand, esiste un sotto-insieme di clausole proposizionalizzate che è insoddisfacibile.

Dal momento che questo sotto-insieme è espresso nella logica proposizionale, si può utilizzare il **ground resolution theorem**: _se un insieme di clausole S è insoddisfacibile, allora la chiusura della risoluzione di tali clausole RC(S) contiene la clausola vuota_, così facendo si effettua la risoluzione del sottoinsieme di clausole per provare l'insoddisfacibilità.

Infine, per lemma di lifting, secondo il quale ad ogni prova per risoluzione nella logica proposizionale corrisopone una prova per risoluzione in FOL che utilizza le stesse sentenze, si si arriva alla prova per contrattizione dell'insoddisfacibilità.

## Uguaglianza (non fatta nel 2019)

Nessuno dei tre metodi di fare inferenza visti finora riesce a gestire le asserzioni del tipo _x=y_.
Per gestire questa situzione è possibile utilizzare tre approcci distinti:

1. **Assiomatizzazione**: si aggiungono degli assiomi che descrivono le proprietà dell'uguaglianza (simmetria, transitività, ecc.) ed assiomi opportuni per ogni predicato e funzione. Questa è la stategia più corretta a livello logico, però dal punto di vista computazinale è poco pratico.
2. **Demodulation** o **Paramodulation**: se _x=y_ e _Unify(x,z) = 𝝝_ allora rimpiazzo _z_ con _SUBST(𝝝,y)_.
3. **Estensione** dell'algoritmo di unificazione: i termini equivalenti vengono unificati in un unico termine.

## Riassunto

- La proposizionalizzazione e l'uso dell'unficazione permetteno di evitare l'istanziazione delle variabili coinvolte in una prova.
- Il modus ponens generalizzato usa l'unificazione e permette l'applicazione di forward e backward chaining su clausole definite.
- GMP è completo per le clausole definite, per dei Datalog il problema è sempre decidibile.
- Forward Chaining è completo e polinomiale per i Datalog, però effettua inferenze in modo indiscriminato.
- Backward Chaining è utilizzato in Programmazione Logica e viene "rinforzato" con delle opportune tecniche di compilazione.
- La risoluzione generalizzata è completa per le KB in CNF. Se si usa il principio di induzione non è più completa.

# Incertezza

Nel mondo reale ci sono vari problemi che causano incertezza:

- Osservabilità parziale, non si hanno tutte le informazioni, ad esempio le condizioni atmosferiche, i ritardi di trenitalia, incidenti, ecc.
- Sensori rumorosi
- Incertezza dell'esito delle azioni che possono fallire a causa di elementi esterni
- Immensa complessità nel modellare i vari eventi.

Pertanto utilizzare un approccio completamente logico potrebbe portare a soluzioni errate oppure richiede ipotesi molto forti.

Conviene quindi utilizzare delle asserzioni probabilistiche che riassumono sia elementi di pigrizia che di ignoranza, ovvero con un solo numero si va a riassumere tutte le evenzidenze senza doverle enumerare (pigrizia) oppure si riesce a lavorare senza avere a disposizione tutti i fatti (ignoranza).

Si va quindi a considerare la probabilità che un certo evento occorra, questo prende il nome di **probabilità soggettiva o bayesiana** e lega le proposizioni al propio stato di conoscenza.

> $P(A_{25}|nessun incidente) = 0.06$
>
> Ovvero la probabilità di arrivare in tempo partendo 25 minuti prima sapendo che non si è verificato un incidente è del 6%.

Utilizzando la probabilità a priori si riesce ad ottenere un aggiornamento continuo dei valori che vengono aggiornati man mano che la conoscenza dell'agente cambia.

Il problema diventa quindi quello di scegliere l'azione in base alla probabilità di successo

![](./immagini/l25-prob.png)

In questo caso la scelta dell'azione dipende dalle preferenze dell'agente, dal momento che non c'è una scelta migliore. Cioè, assieme alla probabilità dobbiamo considerare una funzione di utilità: partire 1440 minuti prima potrebbe implicare svegliarmi presto o non dormire affatto, azione deleteria (con utilità negativa).

La **teoria dell'utilità** è utilizzata per rappresentare e inferire preferenze, la **teoria delle decisioni** accorpa la teoria dell'utilità con le probabilità.

## Probabilità a priori e condizionale

A priori rapprenseta la probabilità incondizionata delle preposizioni sul dominio, ad esempio _P(Tempo = sole) = 0.72_, e corrispondo a gradi di credenza sull'arrivo di una nuova evidenza.

Vengono poi utilizzate delle distribuzioni di probabilità per fornire dei valori per tutti i possibili assegnamenti, ad esempio se _Tempo_ può assumere i valori _<sole, pioggia, nuvole, neve>_, _P(Tempo) = <0.72, 0.1, 0.08, 0.1>_, da notare che le distribuzioni di probabilità sono tutte **normalizzate**, ovvero sommano a 1.

Si parla inoltre di probabilità congiunta per un insieme di variabili alleatori, che fornisce la probabilità per ogni evento atomico su tali variabili.

![](./immagini/l25-tab.png)

Dal momento che si tratta di eventi indipendenti la probabilità congiunta è data dal prodotto delle probabilità.

La probabilità congiunta permette di effettuare l'inferenza probabilitstica, perché ogni elemento della tabella è la somma dei possibili eventi.

Per espriemere l'effetto di nuova conoscenza, è possibile utilizzare la **probabilità condizionale** o a posteriori per influenzare il valore, ad esempio _P(Cavità_ | _Mal_Di_Denti) = 0.8_, ovvero adesso che so di aver mal di denti la probabilità di avere una carie aumenta.

Inoltre, se arriva una nuova evidenza che aumenta la probabilità, la credenza meno specifica **rimane valida** ma non è necessariamente utilie, ad esempio _P(Cavità_ | _Mal_Di_Denti, Cavità) = 1_.

Infine è possibile che della nuova conscenza non influenzi la distribuzione di probabilità congiunta, ad esempio _P(Cavità|Mal_Di_Denti, Vince_Inter) = P(Cavità|Mal_Di_Denti) = 0.8_

![](./immagini/l25-prob-cond.png)

I fattori della **chain rule** possono essere semplificati se tra delle probabilità c'è una relazione di indipendeza, questo perché mantenere in memoria una distribuzione di $n$ variabile booleane richiede $2^n$ locazioni di memoria, questo perché devo considerare tutte le possibili di combinazioni. In realtà ne servono $2^{n-1}$ perché si può sfruttare il fatto che la somma deve essere 1.

Questa complessità, sommata al fatto che fare inferenza probabilistica è più complessa dell'inferenza logica rende la maggior parte dei problemi intrattabili. _forse è una cosa pessimistica, però il punto è che il problema è tanto complesso_.

## Inferenza tramite enumerazione

Una volta creata la tabella della distribuzione di probabilità congiunta permette di andare a calcolare le probabilità dei vari eventi.

![](./immagini/l25-tabella.png)

Se un evento atomico compare più volte, la sua probabilità viene considerata solo una volta.

![](./immagini/l25-tabella-2.png)

Così come si possono calcolare le probabilità condizionali

![](./immagini/l25-tabella-3.png)

### Normalizzazione

Quando si vuole calcolare la distribuzione di una probabilità di una variabile, si può considerare la probabilità normalizzata, ovvero moltiplicare le probabilità per una costante in modo che la somma sia 1.

Da notare che la **P** (in grassetto) indica la distribuzione di probabilità e _Cavity_ indica una variabile (non la sua istanza, cioè non indica che è vero che ho una cavità), notare l'iniziale maiuscola.

Con questo è possibile utilizzare la tabella delle probabilità congiunte per ottenere la distribuzione della probabilità per la variabile _Cavity_ sapendo di avere mal di denti.

![](./immagini/l25-tabella-4.png)

L'idea è quindi quella di calcolare la distribuzione sulla variabile della query (_Cavity_), fissando le variabili di evidenza, ovverro i fatti dati a priori (_tootache_) e sommando sulle variabili nascoste (_catch_) che vengono considerate non influenti per la distribuzione di probabilità della variabile.
