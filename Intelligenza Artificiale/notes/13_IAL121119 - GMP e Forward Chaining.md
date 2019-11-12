# Lezione 13 - Generalized Modus Ponens e Forward Chaining
Martedì 12 Novembre 2019

## Modus Ponens Generalizzato

![](./immagini/l15-gmp.png)

Se i vari $p'_i\theta$ sono uguali ai $p_i\theta$ per una determinata sostituzione \theta allora si possono ridurre ad un unico $q\theta$, in modo simile a come avviene nella logica proposizionale, utilizzando una base di conoscenza in clausole definite.

Le **clausole definite** del primo ordine sono le clausole di Horn riportate nella logica proposizionale, con la differenza che possono includere delle variabili, le quali vengono considerate quantificate universalmente, dal momento che quelle quantificate esistenzialmente vengono sostituite con una costante di Skolem.

Come sostituzione conviene utilizzare quella più generale possibile in modo da trovare il maggior numero possibile di soluzioni ground.

### Correttezza di GMP

Bisogna dimostrare che se $p'_1...p'_n$ e $p_1 \lor ... \lor p_n \implies q$ allora si può inferire $q\theta$, dato che $p'_i\theta = p_i\theta$ per ogni $i$.

Lemma: per ogni clausola definita $p$ abbiamo $p |= p\theta$ per mezzo di UI:

1. $p_1 \lor ... \lor p_n \implies q |= (p_1 \lor ... \lor p_n \implies q)\theta = p_1\theta \lor ... \lor p_n\theta \implies q\theta$
2. $p'_1 ... p'_n |= p'_1 \lor ... \lor p'_n |= p'_1\theta \lor ... \lor p'_n\theta$

Dal momento che per ipotesi $p'_i\theta = p_i\theta$, sfruttando i risultati dei punti 1 e 2 si riesce a ricarvare $q\theta$ usando il Modus Ponens ordinario.

### Esempio di base di conoscenza

![](./immagini/l15-esempio-1.png)

![](./immagini/l15-esempio-2.png)
Mancano i quantificatori espliciti: la prima sentenza sarebbe:

$$\forall x,y,z American(x) \land Weapon(y) \land Sells(x,y,z)\land Hostile(z) \implies Criminal(x)$$

Inoltre, $Sells(x,y,z)$ indica "Il soggetto x ha venduto degli oggetti y al soggetto z"

$M_1$ è una costante di Skolem, creata per elimiinare il quantificatore esistenziale nella clausola $\exists x Owns(Nono,x) \land Missile(x)$. In realtà, queste sono due clausole di Horn unitarie (cioè contengono solo uno schifo).

La frase "Tutti i suoi missili gli sono stati venduti dal Colonnello West" non è proprio tanto deducibile dalla frase sopra. Sperduti dice che "è una licenza poetica che si è preso facendo le slide". In realtà, la frase potrebbe funzionare anche con "Esiste un missile che il colonnello West ha venduto alla nazione Nono".

Anche "I missili sono armi" e "Un nemico dell'america è 'ostile'" sono delle conoscenze di contorno, che sono necessarie per la comprensione/formalizzazione della situazione (ma non sono esplicitamente indicate nel testo di partenza).

## Forward Chaining in FOL

L'algoritmo è analogo a quello utilizzato nella logica proposizionale con la differenza che c'è da tener conto della presenza delle variabili e che queste vengono istanziate il più tardi possibile.

Partendo dai fatti noti si fanno scattare tutte le regole presenti nella KB le cui premesse sono soddisfatte, aggiungendo le varie conclusioni ai fatti noti. Si ripete il processo finché non si trova una risposta oppure non è più possibile aggiungere fatti.

La base di conoscenza è in forma di Horn, con i quantificatori esistenziali ($\exists$) istanziati e i quantificatori universali ($\forall$) non ancora istanziati. Anche la query $\alpha$ può avere dei predicati o delle variabili!

![](./immagini/l15-folfc.png)

**Standardizzazione separata**: serve per evitare conflitti con i nomi delle variabili. In pratica è quello che avevamo fatto nel priimo esempio di **Standardizing Apart**. Le variabili della query $\alpha$ rimangono con i loro nomi, mentre quelle che vengono cambiate sono quell della KB.

$\theta$ rappresenta un'istanziazione di $\alpha$ che è conseguenza logica della base di conoscenza.

### Esempio di applicazione

![](./immagini/l15-folfc-alb.png)

### Considerazioni

L'algoritmo è **corretto** e **completo** per le clausole definite di primo ordine, questo perché essendo clausole definite l'esecuzione dell'algoritmo termina sempre.

La correttezza deriva dal fatto che viene semple applicato il Modus Ponens Generalizzato che è corretto.

Se ci sono solo clausole definite del primo ordine e non c'è nessuna funzione (**datalog**) allora FC termina in un numero poninomiale di iterazioni: $p \cdot n^k$ che coincide con il massimo numero di fatti ground distinti che possono essere presenti nella KB. (*p* predicati *k*-ari e *n* costanti).

In generale l'algoritmo può non terminare se $\alpha$ non è una conseguenza logica e questo è inevitabile perché il problema è semi-decidibile.
Inoltre, la presenza di funzioni porta a generare un numero possibilmente infinito di clausole.

Si può osservare che non c'è bisogno di matchare una regola alla iterazione *k* se non è stata aggiunta una premessa alla iterazione *k-1*. Se ho una regola con 4 premesse con inizialmente nessuna delle 4 premesse è soddisfatta, all'iterazione successiva è diventata vera solo una premessa, è inutile che la consideri (perché non diventeranno vere le altre premesse)

Quindi conviene matchare ogni regola le cui premesse contengono un letterale appena aggiunto, questo per ridurre il numero di operazioni di match, dal momento che si tratta di un'operazione costosa.

Per velocizzare il match si può **indicizzare** la base di conoscenza in modo da permette il recupero di fatti conosciuti in *O(1)*.

Il matching di premesse congiuntive rispetto a fatti conosciuti è un problema NP-hard.

Da questo ne segue che FC è lagarmente utilizzato in basi di conoscenza deduttive (cioè che non hanno funzioni).


## Backward Chaining

In modo analogo alla logica proposizionale è possibile utilizzare il backward chaining.

![a](./immagini/l16-backward.png)

In questo caso l'algoritmo ritorna un **generatore di sostituzioni**, ovvero una funzione che ritorna più valori, ognuno dei quali rappresenta una sostitizione diversa.

L'algoritmo di ricerca può essere visto come un algoritmo AND/OR, dove nei nodi OR vengono valutate le clausole che potrebbero unificare con il goal, mentre nei nodi AND vengono valutati i congiunti della premessa delle regole.

Quindi, `FOL-CI-OR` esegue il fetch di tutte le clausole che potrebbero unificare con il goal, le standardizza, e se la parte destra *rhs* della regola unifica con il goal, verfica che tutti i congiunti della parte sinistra *lhs* siano soddisfatti, utilizzando `FOL-CI-AND`.
`FOL-CI-AND` prova quindi tutti i congiunti considerandoli come sotto-goal utilizzando `FOL-CI-OR`. 
Man mano che la ricerca prosegue l'algoritmo tiene traccia sia delle sostituzioni che sono state effettuate durante la ricerca, sia una pila di sotto-goal da verificare per soddisfare la query.

Nell'esempio delle slide, Missile(y) e Weapon(y) devono essere standardizzate: bisogna sostituire a y la variabile $x_1$ (standardizing apart) prima di poterle effettivamente utilizzare.

Trattandosi di una ricerca in profondità la complessità in spazio è lineare con la dimensione della prova ma c'è il rischio di effettuare cicli infiniti, è quindi necessario andare a controllare che il goal corrente non sia già nella pila dei goal.

Il tempo di esecuzione di questo algortimo può essere ulteriormente ridotto parallelizzando l'unificazione dei nodi OR (**OR-parallelism**), questo perché ogni clausola che può unificare con il goal partiziona lo spazio di ricerca e può portare ad una potenziale soluzione.
È possibile parallelizzare anche la risoluzione degli AND (**AND-parallelism**) però risulta più complessa da implementare.

Un altro problema di questo algoritmo è che non tiene in considerazione i sotto-goal ripetuti. L'algoritmo infatti può finire in un ciclo cercando di risolvere sempre gli stessi sotto-goal, oppure può risultare infefficente quando si trova a dover provare più volte lo stesso sottogoal.
Utilizzando una cache per sotto-goal già incontrati è si ottengono dei miglioramenti alle prestazioni, questa aggiunta prende il nome di **memoization**.

Prolog non utilizza questi due miglioramenti.
