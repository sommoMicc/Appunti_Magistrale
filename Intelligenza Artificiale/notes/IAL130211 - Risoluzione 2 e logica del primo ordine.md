#Lezione 13 - Riduzione 2 e logica del primo ordine

## Riassunto

Gli agenti logici applicano l'inferenza ad una base di conoscenza per derivare nuova informazione e prendere decisioni.

Forward e Backward chaining sono lineari, completi e corretti per le clausole di Horn, mentre la Risoluzione è completa e corretta, ma nel caso pessimo ha una complessità esponenziale.

Manca però del potere espressivo.

## Pro e contro della logica proposizionale

La logica proposizionale è dichiarativa e i pezzi di sintassi corrispondono a fatti.

Permette anche di esprimere informazione parziale/disgiuntiva/negata, al contrario di basi di dati o strutture dati dove vengono utilizzati solo i fatti.

La logica Proposizionale è composizionale, il significato di *B ⋀ P* è conseguenza del significato di *B* e di *P*, non ci sono valori di contesto che influenzano il valore di verità.

Il significato di questa logica è **indipendente dal contesto**, al contrario del linguaggio naturale dove il significato dipende dal contesto.

Tuttavia la potenza espressiva di questa logica è molto limitata.
Ad esempio non si può esprimere "*le trappole causano la brezza in quadrati adiacenti se non scrivendo*" ma è necessario utilizzare una sentenza per ogni quadrato.

##Logica del primo ordine

In quasta logica, come nel linguaggio naturale, si assume che il mondo contenga:

- **Oggetti**: persone, case, ecc...
- **Relazioni**: predicati che mettono in relazione gli oggetti tra di loro. Pssono essere unarie (proprietà) o n-arie. Es: è ventosa, è andiacente a, ...
- **Funzioni**: relazioni particolari che hanno un solo valore per ogni input. Es: miglior amico di, padre di, ...

###Sintassi

- **Costanti**: rappresentano gli oggetti come: ReGiacomo, 2, UP...
- **Predicati**: rappresentano le varie relazioni: Fratello, >,...
- **Funzioni**: Sqrt, GambaSinistraDi, ...
- **Variabili**: x,y,a...
- **Connettivi**: ⋁, ⋀
- **Ugualianza**: =
- **Quantificatori**: ∀, ∃

Ogni simbolo di funzione e di predicato ha una sua specifica arietà che specficia il numero di parametri che riceve

###Sentenze atomiche e complesse

**Termine**: *funzione(termine<sub>1</sub>,...)* o costante o variabile, cioè un'espressione logica che si riferisce ad un oggetto.

Un termine complesso è un modo di dare un nome ad un oggetto combinando uno o più termini semplici utilizzando una funzione.

Consideriamo un termine *f(t<sub>1</sub>, ..., t<sub>n</sub>)*, il simbolo di funzione *f* si riferisce ad una qualche funzione del modello che chiameremo *F*. I termini usati come argomento danno un riferimento agli oggetti del dominio che indicheremo con *d<sub>1</sub> ... d<sub>n</sub>*, nella sua interezza il termine indica quindi l’oggetto che corrisponde al valore della funzione *F* applicata a *d<sub>1</sub> ... d<sub>n</sub>*.

**Sentenza (formula) atomica**: *predicato(termine<sub>1</sub>, termine<sub>2</sub>, ...)* o *termine<sub>1</sub> = termine<sub>2</sub>*. Permettono di asserire dei fatti.

Una formula atomica è vera in un dato modello sotto una determinata interpretazione se la relazione a cui far riferimento il simbolo di predicato è verificata tra gli oggetti a cui fanno riferimento gli argomenti.

Le **sentenze complesse** sono delle combinazioni di sentenze atomiche create utilizzando i connettivi logici.

###Verità nella logica del primo ordine

Le sentenze sono vere rispetto ad un **modello** e ad una **interpretazione**.

Il **modello** contiene degli oggetti (elementi di dominio), delle relazioni definite tra essi e delle funzioni che possono esservi applicate.

L'**interpretazione** invece specifica i referenti per le costanti (oggetti), i predicati (relazioni) e le funzioni (relazioni funzionali). Forniscono cioè le informazioni di contesto. L'interpretazione specifica quindi una corrispondenza tra i simboli e il modello.

Una sentenza atomica *predicato(termine<sub>1</sub>, ..., termine<sub>n</sub>)* è vera se e solo se gli oggetti riferiti da *termine<sub>1</sub>, ..., termine<sub>n</sub>* sono nella relazione definita dal predicato. 

Risulta quindi difficile andare a calcolare tutte le conseguenze logiche possibili enumerando tutti i possibili modelli, perché si verifica un'esplosione combinatoria.

###Quatificatori universali e esistenziali

Con il quantificatore ∀ è possibile definire il concetto che un predicato *P* è vero per ogni *x* in un modello *m* se e solo se *P* è vero per ogni possibile valore di *x*.

> Chiunque è a Padova è intelligente
> 
> ∀x Luogo(x,Padova) => Intelligente(x)

In prima apporsimazione l'esistenza è equivalente alla congiunzione di istanziazioni di *P*. (Tutti devono essere veri)

Se nel modello è presente anche un solo simbolo di funzione, l'enumerazione delle possibili istanziazioni di *P* è infinita.

Tipicamente => è il connettivo principale utilizzato con i ∀, l'uso di ⋀ è tipicamente sbagliato:

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

####Proprietà dei quantificatori:

- ∀x ∀y è commutativo, così come ∃x ∃y;
- ∃x ∀y non è la stessa cosa di ∀y ∃x.

**Dualità**: ogni quantificatore può essere espresso usando la negazione dell'altro.

> ∀x Piace(x,Gelato) == ¬∃x ¬Piace(x,Gelato)

###Uguaglianza

Una sentenza atomica può essere anche un'uguaglianza tra due termini.

*termine<sub>1</sub> = termine<sub>2</sub>* è vero per una data interpretazione se e solo se *termine<sub>1</sub>* e *termine<sub>2</sub>* si riferiscono allo stesso oggetto.

Ad esempio, le sentenze *1=2* e _*(Sqrt(x), Sqrt(x) = x_ sono soddisfacibili, ovvero esiste un modello in cui sono vere. La sentenza *2=2* è invece valida inquanto risulta vera per ogni modello perché viene utilizzato lo stesso predicato.