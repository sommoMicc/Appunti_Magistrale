#Lezione 16 - Backward Chaining e Prolog


## Programmazione Logica: Prolog

Come anticipato utilizza backward chaining con clausole di Horn.

Un programma Prolog è un'insieme di clausole che definiscono la base di conoscenza.

Le clausole sono scritte "al contrario":

```
test :- letterale_1, letterale_2, ..., letterale_n.

criminal(X) :- american(X), weapon(Y), sells(X,Y,Z), hostile(Z).
```

Da notare che le variabili sono scritte in maiuscolo e i predicati tutti in minuscolo.

I fatti vengono rappresentati come predicati senza implicazione.

```
american(West).
```

Una volta inserita la base di conoscenza vengono inviate delle query al programma. La ricerca in backward viene fatta real time, se il programma viene interpretato, mentre nel caso il programma sia compilato vengono effettuate delle ottimizzazioni.

Compilando un programma Prolog è possibile, trammite **open coding**, aumentare l'efficenza andando a modificare l'algoritmo di unificazione per le query che il programma può ricevere, diminuendo così il tempo necessario per trovare una soluzione.

C'è anche un meccanismo di recupero efficente per le clausole attivabili per mezzo di **direct linking**.

Per risolvere le query Prolog utilizza il backward chaining in *depth first, left to right*. Questo è importante per vari motivi, ad esempio con una regola ricorsiva è necessario definire prima il caso base e poi l'invocazione ricorsiva:

```
# Ok
path(X,Z) :- link(X,Z).
path(X,Z) :- path(X,Y), link(Y,Z).

# Sbagliato, entra in un ciclo infinito
path(X,Z) :- path(X,Y), link(Y,Z).
path(X,Z) :- link(X,Z).
```

In Prolog è possibile usare l'operatore `is` per assegnare un valore a delle variabili e di utilizzare alcune espressioni aritmetiche, ma non è possibile utilizzarlo per risolvere delle equazioni:

```
X is 4 + 3. # OK. {X/7}
5 is X + Y. # Fallimento
```

Tuttavia se viene aggiunto alla base di conoscenza il teorema di Peano, anche la seconda query viene calcolata correttamente.

###Assunzione del mondo chiuso

In Prolog solo le sentenze inferibili dalla base di conscenza sono considerate vere, tutto il resto e tutto quello che fallisce viene considerato falso. 
Ovvero, se la dimostrazione che la query sia implicata dalla KB fallisce, allora la query viene considerata come falsa. 

Questa assunzione causa la così detta **negation as failure**. Considerando il seguente programma:

```
person(jim).
person(jane).
man(jim).

woman(X):- \+( man(X) ). # \+ è il not
```

Le query `woman(jim)` fallisce come prevedibile, tuttavia la query `woman(X)` fallisce e ritorna falso.

Questo perché la query `woman(X)` ha successo solo se la query `\+( man(X) )` fallisce, ma l'interprete riesce ad unificare `man(X)` con `man(jim)`, quindi `woman(X)` fallisce e la variabile `X` rimane non assegnata, mentre ci si potrebbe aspettare `{X/jane}` come risposta, dal momento che `man(jane)` fallisce.

Questo fallimento è dovuto al fatto che Prolog, in seguito alla closed world assumpition, non distingue il fallimento causato da un termine falso e il fallimento causato dall'ignoranza.

###Esempio di programma

```
append([],Y,Y).
append([X|L], Y, [X|Z]) :- append(L,Y,Z).
```
L'operatore `|` su una lista separa il primo elemento dal resto della lista.

La prima clausola dice che l'append ad una lista vuota di una variabile da come risultato la variabile stessa.

La seconda regola dice che data una lista con almeno un elemento e una lista Y, la concatenazione è una lista che inizia co il primo elemento e che continua con una lista. Questa lista è ottenuto partendo concatenando il resto della prima lista e la lista `Y`. 

Quindi se `Z` è l'append di `L` con la lista `Y`, `[X|Z]` è l'append di `[X|L]` con `Y`.

Su questa base di conoscenza è possibile fare la query `append(A,B,[1,2])?`, cioè chiedere se `[1,2]` è la concatenazione di `A` e `B`.

Prolog esegue quindi l'unificazione secondo l'ordine in cui compaiono le clausole:

```
append(A,B,[1,2])?
append([],Y,Y)

𝜃 = {A/[], B/Y, Y/[1,2]}
```

Vengono però ritornate solamente delle sostituzioni che hanno variabili della query, quindi `𝜃 = {A/[], B/[1,2]}`.

Dopodiché si continua a cercare, assumendo che quelle già valutate siano fallite, in modo da trovare altre soluzioni

```
append(A,B,[1,2])?
append([X|L], Y, [X|Z]) :- append(L,Y,Z).

𝜃_2 = {A/[X|L], B/Y, X/1, Z/[2]}

Il nuovo goal diventa quindi:

append(L,Y,[2])? //Adesso si riparte da capo con il processo di ricerca
append([],Q,Q) 

𝜃_2,1 = {L/[], Y/Q, Q/[2]} = {L/[], Y/[2]}

Viene quindi composta 𝜃_2 con 𝜃_2,1

𝜃_2 𝜸 𝜃_2,1 = {A/[1|[]], B/[2]} = {A/[1], B/[2]}

Dopodiché assumo falsa la clausola usata e ne provo un'altra

append(L,Y,[2])?
append([X|F], G, [X|Z]) :- append(F,G,Z)

𝜃_2,2 = {L/[X|F], Y/G, [X|Z]/[2]} = {L/[2|F], Y/G, X/2, Z/[]}

Il nuovo goal diventa quindi: 
append(F,G,[])? e si riparte da capo
append([], K, K)

𝜃_4 = {F/G, G/K, K/[]} = {F/G, G/[]}

Combinando 𝜃_4 e 𝜃_2_2 = {...}

Bisogna poi assumere falsa la prima clausola e provare con la seconda.
Durante la ricerca con la seconda non si riesce a trovare una sostituzione, l'algoritmo quindi temrina.
```

*Tutte le ricerche dovrebbero essere standardizzate con un pedice e non con le lettere, per motivi pratici questo non viene fatto nell'esempio.*

Le variabili della query possono essere istanziate a piacere. Ad esempio alla query `append([],[1],[1])?` Prolog risponde con un `True`.