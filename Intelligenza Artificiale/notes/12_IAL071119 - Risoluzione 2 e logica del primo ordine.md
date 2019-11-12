# Lezione 13 - Riduzione 2 e logica del primo ordine
Giovedì 7 Novembre 2019

## Riassunto

Gli agenti logici applicano l'inferenza ad una base di conoscenza per derivare nuova informazione e prendere decisioni.

Forward e Backward chaining sono lineari, completi e corretti per le clausole di Horn, mentre la Risoluzione è completa e corretta, ma nel caso pessimo ha una complessità esponenziale.

Manca però del potere espressivo.

## Pro e contro della logica proposizionale

La logica proposizionale è dichiarativa e i pezzi di sintassi corrispondono a fatti specifici. Dal punto di vista computazionale diventa ingestiblie quando si vogliono andare a trattare tante situazioni riguardanti le entità

Permette anche di esprimere informazione parziale/disgiuntiva/negata, al contrario di basi di dati o strutture dati dove vengono utilizzati solo i fatti.

La logica Proposizionale è composizionale, il significato di *B ⋀ P* è conseguenza del significato di *B* e di *P*, non ci sono valori di contesto che influenzano il valore di verità.

Il significato di questa logica è **indipendente dal contesto**, al contrario del linguaggio naturale dove il significato dipende dal contesto.

Tuttavia la potenza espressiva di questa logica è molto limitata.
Ad esempio non si può esprimere "*le trappole causano la brezza in quadrati adiacenti se non scrivendo*" ma è necessario utilizzare una sentenza per ogni quadrato.

## Logica del primo ordine

In quasta logica, come nel linguaggio naturale, si assume che il mondo contenga:

- **Oggetti**: persone, case, ecc...
- **Relazioni**: predicati che mettono in relazione gli oggetti tra di loro. Pssono essere unarie (proprietà) o n-arie. Es: è ventosa, è andiacente a, ...
- **Funzioni**: relazioni particolari che hanno un solo valore per ogni input. Es: miglior amico di, padre di, ...

### Sintassi

- **Costanti**: rappresentano gli oggetti come: ReGiacomo, 2, UP...
- **Predicati**: rappresentano le varie relazioni: Fratello, >,...
- **Funzioni**: rappresentano relazioni di tipo funzionale: Sqrt, GambaSinistraDi, ...
- **Variabili**: x,y,a...
- **Connettivi**: ⋁, ⋀
- **Ugualianza**: =
- **Quantificatori**: ∀, ∃

Ogni simbolo di funzione e di predicato ha una sua specifica arietà che specficia il numero di parametri che riceve

I modelli ottenibili per il vocabolario di una data KB sono talmente tanti che è quasi impossibile enumerarli, e comunque farci delle elaborazioni sopra è controproducente

### Sentenze atomiche e complesse

**Termine**: $funzione(termine_1,...)$ o costante o variabile, cioè un'espressione logica che si riferisce ad un oggetto.

Un termine complesso è un modo di dare un nome ad un oggetto combinando uno o più termini semplici utilizzando una funzione.

Consideriamo un termine *f(t_1, ..., t_n)*, il simbolo di funzione *f* si riferisce ad una qualche funzione del modello che chiameremo *F*. I termini usati come argomento danno un riferimento agli oggetti del dominio che indicheremo con *d_1 ... d_n*, nella sua interezza il termine indica quindi l’oggetto che corrisponde al valore della funzione *F* applicata a *d_1 ... d_n*.

**Sentenza (formula) atomica**: *predicato(termine_1, termine_2, ...)* o *termine_1 = termine_2*. Permettono di asserire dei fatti.

Una formula atomica è vera in un dato modello sotto una determinata interpretazione se la relazione a cui far riferimento il simbolo di predicato è verificata tra gli oggetti a cui fanno riferimento gli argomenti.

Le **sentenze complesse** sono delle combinazioni di sentenze atomiche create utilizzando i connettivi logici.

### Verità nella logica del primo ordine

Le sentenze sono vere rispetto ad un **modello** e ad una **interpretazione**.

Il **modello** contiene degli oggetti (elementi di dominio), delle relazioni definite tra essi e delle funzioni che possono esservi applicate.

L'**interpretazione** invece specifica i referenti per le costanti (oggetti), i predicati (relazioni) e le funzioni (relazioni funzionali). Forniscono cioè le informazioni di contesto. L'interpretazione specifica quindi una corrispondenza tra i simboli e il modello.

Una sentenza atomica *predicato(termine_1, ..., termine_n)* è vera se e solo se gli oggetti riferiti da *termine_1, ..., termine_n* sono nella relazione definita dal predicato. 

Risulta quindi difficile andare a calcolare tutte le conseguenze logiche possibili enumerando tutti i possibili modelli, perché si verifica un'esplosione combinatoria.

### Quatificatori universali e esistenziali

Con il quantificatore $\forall$ è possibile definire il concetto che un predicato *P* è vero per ogni *x* in un modello *m* se e solo se *P* è vero per ogni possibile valore di *x*.

> Chiunque è a Padova è intelligente

$$\forall x Luogo(x,Padova) => Intelligente(x)$$

In prima apporsimazione l'esistenza è equivalente alla congiunzione di istanziazioni di *P*. (Tutti devono essere veri)

Se nel modello è presente anche un solo simbolo di funzione, l'enumerazione delle possibili istanziazioni di *P* è infinita.

Tipicamente => è il connettivo principale utilizzato con i $\forall$, l'uso di $\wedge$ è tipicamente sbagliato:

> ∀x Luogo(x,Padova) ⋀ Intelligente(x)

vuol dire che chiunque è a Padova e chiunque è intelligente e non è la stessa cosa che si voleva dire.

Diverso è il discorso per il quantificatore esistenziale ∃.

*∃x P* è vero in un modello *m* se e solo se *P* è vero essendo *x* un qualche possibile valore di un oggetto nel modello.

> Qualcuno a Bologna è intelligente
>
> ∃x Luogo(x,Bologna) ⋀ Intelligente(x)

In prima apporsimazione l'esistenza è equivalente alla disgiunzione di istanziazioni di *P*. (Basta che ce ne sia uno di vero).

Anche in questo caso la modellazione delle istanziazioni mediante enumerazione risulta infinita nel caso il modello contenga una funzione.

Il connettivo principale da usare con l'esistenza è ⋀ e tipicamente utilizzare => è sbagliato.

#### Proprietà dei quantificatori:

- $\forall x \forall y$ è commutativo, così come $\exists x \exists y$;
- $\exists x \forall y$ non è la stessa cosa di $\exists y \forall x$ (C'è una persona che ama chiunque nel mondo - Ognuno nel mondo è amato da almeno una persona).

**Dualità**: ogni quantificatore può essere espresso usando la negazione dell'altro.

> $\forall x$ Piace(x,Gelato) $\implies$ $\lnot\exists x \lnot$ Piace(x,Gelato)

### Uguaglianza

Una sentenza atomica può essere anche un'uguaglianza tra due termini.

*termine_1 = termine_2* è vero per una data interpretazione se e solo se *termine_1* e *termine_2* si riferiscono allo stesso oggetto.

Ad esempio, le sentenze *1=2* e _*(Sqrt(x), Sqrt(x) = x_ sono soddisfacibili, ovvero esiste un modello in cui sono vere. La sentenza *2=2* è invece valida inquanto risulta vera per ogni modello perché viene utilizzato lo stesso predicato.

# Inferenza nella logica del prim'ordine
## Istanziazione unviersale (UI)

Nel caso del quantificatore universale è possibile dare una rappresentazione con un enumerazione di tutte le possibili istanzazioni del termine, in ⋀ tra loro.

In questo caso si va a sostiturire ogni vabiarbile *v* con i vari **termini ground** (termini in cui non compaiono variabili).

![](./immagini/l14-sostituzione-1.png)

Il risultato diella trasfomrazione viene rappresentato con `Subst(𝜃,𝜶)` e indica il risultato dell’applicazione della sostituzione 𝜃 alla formula 𝜶.

![](./immagini/l14-sostituzione-2.png)

Se non ci sono simboli di funzione allora il numero di istanziazioni è finito.

## Istanziazione esistenziale (EI)

L'idea è quella di andare a generare una nuova costante *k* che non appartiene alla base di conoscenza, la quale va a prende il posto del simbolo che soddisfa l'esistenza.

Non è noto quale sia l'entità associata a *k*, ma si sa che *k* riferisce un'entità che soddisfa la condizione esistenzale.

Questo perché la formula esistenziale afferma che esiste un qualche oggetto che soffisfa una certa condizione e l'istanziazione va a dare un nome a questo oggetto, senza specificare di che oggetto sia.

![](./immagini/l14-sostituzione-3.png)

![](./immagini/l14-sostituzione-4.png)

Se una sentenza contiene entrambi i quantificatori, in particolare *∀y ∃x*, non è possibile utilizzare una singola costante di **Skolem** per istanziare *x*, questo perché dovrei avere infinite costanti, in questo caso viene usata una **funzione di Skolem** che genera le varie costanti. (*verrà approfondito più avanti*)

L'istanziazione esistenziale può essere applicata una sola volta per sentenza esistenziale e la nuova KB non è equivalente a quella vecchia, ma è soddisfacibile se e solo se la vecchia KB era soddisfacibile.

Mentre l'istanziazione di un quantificatore universale può essere applicata più volte per aggiungere nuove sentenza alla base di conoscenza e la nuova KB è logicamente equivalente a quella vecchia.

## Infereza mediante riduzione alla inferenza proposizionale

L'idea è quella di istanziare i vari quantificatori, per poi considerare i vari predicati applicati ai termini ground come se fossero dei letterali nella logica proposizionale.
Questo procedimento prende il nome di **proposizionalizzazione**.

L'istanziazione del quantificatore esistenziale avviene utilizzando una costante di Skolem, mentre per quello universale avviene applicato tutte le possibili sostutizioni di termini ground presenti nella KB.

Il tutto funziona se non sono presenti simboli di funzione, perché nel caso ci siano delle funzioni possono essere generati infiniti simboli.

Questo processo garantisce che una sentenza ground è conseguenza logica della nuova KB se e solo se è conseguenza logica della KB originaria.
Di fatto, ogni KB espressa nella logica di primo ordine può essere proposizionalizzata in modo da preservarne le conseguenze logiche.

L'idea è quindi quella di andare a proposizinalizzare sia KB che la query, applicare la riduzione e restituire il riusltato.
Quest'idea è corretta per il teorema di Herbrand.

> **Teorema di Herbrand**: se una sentenza 𝜶 è conseguenza logica di una FOL KB (*base di conoscenza espressa nella logica del primo ordine*) essa è conseguenza logica di un sottoinsieme finito della KB in versione proposizionale.

Per gestire la presenza di funzioni, si considerano solo le costanti della FOL-KB e si verifica se 𝜶 è conseguenza logica. Se questa non lo è si prendono in considerazioni anche i termini ground generati da una sola invocazione di funzioni, e se anche in questo caso non è conseguenza logica, si considerano fino a due invocazioni di funzioni, e così via finché non si trova che 𝜶 è conseguenza logica.

Questo metodo di fare inferenza è sia **corretto** che **completo** per le basi di conoscenza che non hanno funzioni. Corretto perché utilizza tecniche di inferenza per la logica proposizionale che sono corretto, e completo in caso non ci siano funzioni perché in questo caso il numero di proposizioni generabili è finito.

Inoltre, prima o poi questo algorito riesce a dimostrare che 𝜶 è conoscenza logica, ma se 𝜶 non è conseguenza logica l'algoritmo non termina, non si può ottenere un risultato migliore in quanto la soddisfacibilità booleana è un problema semi-decidibile.

Con *p* predicati *k*-ari e *n* costanti, ci sono *p \* n<sup>k</sup>* istanziazioni, considerando inoltre che l'algoritmo di riduzione ha complessità esponenziale, la situazione è disastrosa.

C'è anche un'altro problema con la proposizionalizzazione ed è legato al fatto che i quantificatori universali generano tanti fatti che sono irrilevanti.
Conviene quindi andare ad applicare l'istanziazione universale solo quando è strettamente necessario.

## Unificazione
Concetto di non andare a proposizionalizzare dall'inizio tutta la base di conoscenza ma di applicare l'istanziazione universale solo quando necessarie. In questo modo si preservano le variabili, e di fatto è come istanziare alcune variabili e altre le lascio istanziate perché tutte le istanziazioni ground per quelle variabili vanno bene. Risparmio quindi sia spazio che tempo.

Si può ottenere l'inferenza immediatamente se è possibile trovare una sostituzione 𝜃 tale che `Re(x)` e `Avido(x)` corrispondano a` Re(Giovanni)` e `Avido(y)`.

![](./immagini/l14-unificazione-1.png)

Questo perché può capitare che variabili che si trovano in "*scope*" diversi abbiano lo stesso nome.

L'unificazione è quel processo che trova le sostituzioni che rendono identiche espressioni logiche diverse.

Applicando l'unificazione può capitare che si ottenga solamente l'uguaglianza sintattica, con dei predicati che contengono termini che non sono ground. 
In questo caso l'algoritmo funziona comunque, tant'è che il predicato ottenuto appplicando la sostituzione rappresenta un sottinsieme dei termini ground, che può essere anche infinito.

Con le sostituzioni che hanno dei termini non ground c'è un'ordinanento parziale dato dalla quantità di termini ground generabili a partire dalle varie sostituzioni.

**Quando c'è la scelta tra più sostituzioni conviene tenere quella più generale in modo da avere maggiori possibilità di scelta (most general unifier).**

Si dice che una sostituzione 𝜃<sub>1</sub> è più generale di una sostituzione 𝜃<sub>2</sub> se 𝜃<sub>1</sub> impone meno vincoli sul valore delle variabili, per ogni coppia di di espressioni unificabili esiste un singolo unificatore più generale MGU.

In questo modo è possible rimandare il più possibile l'istanziazione del quantificatore universale.

### Algoritmo di unificazione

**Standardizzazione separata** (_standardizing apart_): può capitare che in due formule distinte ci siano variabili con lo stesso nome, durante il processo di unificazione questo può creare dei problemi, è necessario quindi standardizzare prima le formule in modo che non ci siano conflitti sul nome delle variabili. In pratica, le variabili sono in due "scope" diversi (come avviene per le variabili all'interno di una procedura).

Dati due predicati:

- *Predicato<sub>1</sub>(arg<sub>1,1</sub>, ...arg<sub>1,n</sub>)*
- *Predicato<sub>2</sub>(arg<sub>2,1</sub>, ...,arg<sub>2,m</sub>)*

Per poter unificare è necessario che i due predicati siano uguali sintatticamente e che abbiano la stessa lunghezza (*n = m*).

Bisogna poi porre uguali tra loro i vari argomenti dei predicati, tenendo in considerazione che la stessa variabile può compararire in più argomenti dello stesso predicato.

![](./immagini/l14-unificazione-alg.png)

La notazione è la seguente. Data una variabile $x \equiv f(g(z), b)$, $x.OP = f$, $x.ARGS = [g(z),b]$. Per "Composta/Compound" si intende una scrittura predicato, quindi non variabili sciolte (x è un predicato/scrittura predicato).

L'algoritmo analizza i due predicati, termine per termine, cercando di unificarli con `Unify-Var`.

La funzione `Controlla-Occorrenza` verifica che la variabile `var` che si vuole unificare non compaia nel termine `x`, questo serve per bloccare l'unificazione tra due terminiti come *T1(a)* e *T1(T1(a)*.

Questo algoritmo ritorna sempre la **MGU**

Due sostituzioni possono essere tra loro composte, applicando prima una sostituzione all'altra e poi andando ad aggiungere alla prima gli elementi della seconda sostituzione.

Per poter comporre due sostsituzioni è necessario che queste siano compatibili tra di loro.

L'algoritmo può essere reso più efficente andando ad applicare la sostituzione corrente alle due liste di variabili prima di andare ad unificare. 
Ovvero sostituire

```
return Unify(
            Resto[x], 
            Resto[y], 
            Unify(Primo[x], Primo[y], 𝜃)
        )
```

con

```
return Unify(
            Subst(𝜃,Resto[x]), 
            Subst(𝜃,Resto[y]), 
            Unify(Subst(𝜃,Primo[x]), Subst(𝜃,Primo[y]), 𝜃)
        )
```

Inoltre, all'interno di `UnifyVar`, anziché aggiungere direttamente la nuova sostituzione a 𝜃, conviene utilizzare il metodo `Compose({var/x}, 𝜃)` che prima di aggiungerla applica la nuova sostituzione alla sostituzione corrente. In pratica, "add {var/x} to $\theta$" è l'equivalente di una composizione di funzione

