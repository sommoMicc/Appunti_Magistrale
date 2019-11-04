# Lezione 8 - Reti neurali 2
28 Ottobre 2019



Perceptron va bene ma non riesce ad apprendere la XOR perché non è linearmente separabile.

## Reti di Perceptron

L'idea è quindi quella di combinare più Perceptron tra loro, in modo che riescano ad apprendere una qualsiasi funzione boolena.

Il problema ora diventa come effettuare l'apprendimento con una rete di Perceptron, dal momento che non è più triviale come assegnare dei pesi alle unità nascoste. 
Una possibile soluzione è quella di rendere il singolo neurone derivabile e sfruttare la tecnica di Discesa del Gradiente per apprendere i pesi "giusti".

## Ripasso concetti matematici di base
Ripasso del concetto di derivata. Presentazione delle derivate notevoli. Osservazioni:
* Un trucco per cercare minimi e massmii delle funzioni è cercare i punti dove le derivate si annullano (punti critici). 
* Una funzione convessa (parabola) gode della proprietà di avere solo un minimo. Una funzione concava ($\cap$) ha un solo massimo.

Ripasso delle regole di derivazione:
* Derivata di $k\cdot f(x)$ è $k \cdot f'(x)$
* Derivata della somma è la somma delle derivate
* Derivata del prodotto e del quoziente le ometto
* $D(\frac{1}{g(x)}) = -\frac{g'(x)}{g(x)^2}$
* $D(g(f(x))) = g'(f(x))-f'(x)$. Ovvero $D(e^{x^2}) = 2e^{x^2}\cdot x$

### Discesa di gradiente

In breve, il gradiente $\nabla$ di una funzione a valori reali $f: \R^n \to \R$ è un vettore che ha come componenti le derivate parziali della funzione

Il problema di minimizzazione consiste nello trovare un vettore lungo $n$ (perché la funzione target va da $\R^n \to \R$) che, se passato come argomento alla funzione $f$, ci fa ottenere il suo valore minimo. In pratica: 

$$x^* \in \R^n, x^* = argmin_x f(x) $$

L'idea dell'algoritmo di discesa del gradiente è di seguire il segno della derivata prima di una funzione per raggiungere un massimo o minimo locale. Sia quindi $x_i$ il punto che sto considerando. Finché il gradiente è diverso da zero, l'algoritmo sposta il punto $x_i$ nella direzione di discesa (che corrisponde a sinistra se la derivata è positiva, destra se la derivata è negativa) di $\eta_i$ unità. Notare che se sbaglio a scegliere il learning rate (lo scelgo troppo grande), potrò non raggiungere mai il minimo perché continuerò a saltare tra un pendio e l'altro del minimo. Inoltre, l'algoritmo non ha nessuna garanzia sulla limitatezza del numero di passi necessari per la sua convergenza al punto di minimo locale $x^*$

## La regola Delta
La regola delta è una regola di aggiornamento dei pesi diiversa da quella del perception, che ci permette di ottenere una soluzione che approssima "al meglio" il concetto target. La regola delta usa la discesa di gradiente, cercando, tramite la minimizzazione di una funzione errore, un valore ottimo (massimo o minimo, in base al problema) della funzione target.

Se considero un Perception senza hard treshold (ovvero senza l'applicazione della funzione segno nella funzione $out$):

![](./immagini/l10-threshold.png)

La funzione obiettivo da minimizzare è la **funzione errore**, la quale rappresenta lo scarto quadratico medio del valore target predetto dal neurone (*funzione out*) ($t^{(i)}$ indica l'i-esimo dato di training).

Dal momento che si tratta di una funzione derivabile è possibile utilizzare la discessa di gradiente per raggiungere un minimo.

![](./immagini/l10-step.png)

Il valore $-\eta$ è lo step con il quale mi sposto e prende il nome di **learn rate**.

Per calcolare lo spostamento rispetto ad ogni $w_i$ per minimizzare la funzione obiettivo, vado a calcolare la derivata.
Una volta calcolati tutti i $\Delta w_i$ posso andare a sommarli tra loro e successivamente aggiornare il vettore *w*.

La seguente serie di calcoli mostra come è possibile calcolare i $\Delta w_i$ per tutti gli esempi presenti nel training set. 
Viene usato $out^{(d)}$ per indicare il valore calcolato dalla rete per il *d*-esimo esempio del training set e $t^{(d)}$ per indicare il corretto valore della funzione target per lo stesso esempio.

![](./immagini/l10-step-passaggi.png)

Da notare che $t^{(d)}$ non dipende da $w$, quindi ai fini del calcolo della derivata è considerata come una costante.
Il risultato della derivata assomiglia all'algoritmo di apprendimento del Perception.

#### Algoritmo di apprendimento

$\Delta w_i$ rappresenta lo spostamento dal $w_i$ iniziale. Inoltre, il passo $\Delta w_i = 0$ indica che tutti i $\Delta$ vanno inizializzati con 0.

![](./immagini/l10-algoritmo-gradiente.png)

In pratica prima viene esaminato tutti il training set per aggiornare i vari $\Delta w_i$, una volta finito di esaminare il training set si aggiornano i $w_i$ e si ripete fino a che non si verifica una  condizione di stop.

Possono essere utilizzate varie condizioni di stop:

- *E(w)* minore di una soglia prefissata
- *Δw_i = 0 ∀i*
- Il numero di iterazioni ha superato una soglia prefissata. 

### Discesa di gradiente con sigmoide
La versione di discesa del grandiente presentata precedentemente era "semplificata": non teneva conto della funzione segno presente nel vero calcolo ($sign(w \cdot x)$). La funzione segno renderebbe la funzione $out$ non derivabile. Si può ovviare al problema sostituendo alla funzione segno quella del sigmoide:

![](./immagini/l9-sigmoidale.png)

$$\sigma(z) = \frac{1}{(1 + e^z)}$$

La funzione è continua e compresa tra 0 e 1. Un'altra caratteristica interessante di questa funzione è che la sua derivata può essere espressa come una funzione dei valori di input. 
Cioè:

$$\frac{∂\sigma}{∂z} = \sigma(z)(1-\sigma(z))$$


![](./immagini/l10-sigmoidale.png)

In questo caso si può utilizzare lo stesso algoritmo di apprendimento visto in precedenza, cambia però come vengono aggiornati i $\Delta w_i$, dal momento che bisona tenere in considerazione la derivata della funzione sigmoidale.

![](./immagini/l10-derivata-sigmoide.png)

Nonostate la formula sembri molto minacciosa, i $\Delta w_i$ sono uguali a $\frac{-\eta∂E}{∂w_i}$, cioè il learn rate moltiplicato per la derivata appena calcolata.

