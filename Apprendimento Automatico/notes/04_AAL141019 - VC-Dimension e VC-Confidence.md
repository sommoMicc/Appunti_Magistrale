# Lezione 5 VC-Dimension e VC-Confidence
14 Ottobre 2019

## A simple experiment
Da una cesta formata da varie palline, che possono essere rosse o blu, andiamo a fare $N$ estrazioni. La probabilita di estrarre una pallina rossa $P(R) = \pi$, mentre la probabilità di estrarne una di colore blu $P(B) = 1-p$ (sono eventi indipendenti, variabili di Bernoulli). Io non conosco $\pi$, ma conosco $\sigma$, ovvero il numero di palline rosse pescate nelle $N$ estrazioni. Di fatto però, $\sigma$ non da un'informazione certa, in quanto le estrazioni avvengono in maniera casuale e totalmente scorrelata. Tuttavia, mi aspetto che la frequenza del campione $\sigma$ sia simile a $P(R)$, cioè $\pi$, (al netto di un errore $\epsilon$) soprattutto quando il sample $N$ è grande. A riguardo, esiste un teorema (Hoeffding's Inequality):

$$ P(|\sigma - \pi| > \epsilon) \le 2e^{-2\epsilon^2N}$$
dove $|\sigma - \pi| > \epsilon$ è chiamato "bad event" (ovvero il sample considerato si discosta di "molto" rispetto al comportamento reale).

Questo teorema ci dice che tenendo $N$ tanto alta (facendo tante estrazioni), il valore dell'esponenziale tenderà a 0 (perché $e^{-\infty} \to 0$). In ogni caso, $\epsilon$ e $N$ sono legati da una relazione quadratica: diminuendo $\epsilon$ di 1/10, $N$ aumenta di 100 volte per compensare tale riduzione. Quindi l'equazione $\sigma = \pi$ è P.A.C. (Probably Approximately Correct): si verifica poco spesso che abbiamo un $N$ così tanto grande.

Siccome l'equazione del bad event è simmetrica rispetto a $\sigma$ e $\pi$ (per la presenza del modulo), si può dire che $\pi$ approssima $\sigma$ e $\sigma$ approssima $\pi$.

## Connection to Learning
Nell'esempio precedente, $\pi$ è l'incognita. Nel caso dell'apprendimento, invece, la vera incognita è la funzione target ($f: X \to Y$), che è quello che vogliamo approssimare. Il recipiente dell'esempio precedente è "equivalente" all'input space $X$, mentre le palline sono relative alle ipotesi: __fissata un'ipostesi $h$__, se la pallina è verde allora l'esempio è corretto, ovvero $h(x) = f(x)$, mentre se la pallina è rossa l'esempio è errato, ovvero $h(x) \ne f(x)$. Quindi, $\pi$ non è altro che l'errore ideale (la proporzione di errori nell'instance space, recipiente), mentre $\sigma$ è l'errore empirico.

Il problema è che qua abbiamo fissato una ipotesi $h$ (di cui valutiamo le performance), quindi questo rappresenta il processo di verifica, non di apprendimento. Nel processo di apprendimento, invece, oltre a testare una particolare $h$, dobbiamo prima sceglierla tra un'insieme di ipotesi $H$. Per ciascuna possibile scelta, avrò un diverso $\pi$ e un diverso $\sigma$. 

Cambiando un attimo notazione, abbiamo:
* in-sample error (errore del campione) $\sigma \to E_i(h)$
* out-of-sample error $\pi \to E_o(h)$
* quindi, $P(|E_i(h)-E_o(h)| > \epsilon) \le 2e^{-2\epsilon^2N}$ (e invece no!!)

La reale situazione in un setting di apprendimento è avere tanti bidoni tutti uguali (in capienza) ma con i colori disposti in maniera diversa. Da notare che ogni pallina rappresenta la stessa $x$ in $f$. Per ciascuno di questi recipienti conosco solo l'errore _in-sample_ $\sigma = E_i(h)$. L'algoritmo di apprendimento va a scegliere una $h$ con un determinato errore _in-sample_ (ad esempio, prendere una $h$ che lo minimizzi).

Analogamente a quanto succede con il lancio di monente (l'esempio delle 10 teste consecutive), la probabilità del _bad-event_ aumenta all'aumentare del numero dei campioni: è inapplicabile la _disuguaglianza di Hoeffding_

La formula che considera tutto questo è l'__union bound__:

$$P(|E_i(g) - E_o(g)| > \epsilon) \le \sum_{m=1}^M P(|E(h_m)-E_o(h_m)| > \epsilon) \le 2Me^{-2\epsilon^2N}$$

il problema è che $M$ indica il numero di ipotesi presenti in $H$ (cioè la sua cardinalità, che può essere anche infinita), quindi da __taaaaanto__ fastidio!

Con tanta fatica si è dimostrato che la $M$ può essere sostituita con $m_H(N) \le 2^N$, che è correlata con la complessità dello spazio delle ipotesi. Ricordando che $P(E \cup F) = P(E) + P(F) - P(E \cap F)$, abbiamo che quando i bad event si sovrappongono molto, $m_H(N)$ scende di molto. Cercheremo quindi il caso in cui $m_H(N)$ sia polinomiale rispetto a $N$ (e non esponenziale)


## Esempi di spazi delle ipotesi

Seguono alcuni esempi di spazi per le ipotesi nei problemi di apprendimento supervisionato, cioè quei problemi in cui si vuole stabilire se un elemento *x* appartiene o meno ad una classe.


## Misurare la complessità dello spazio delle ipotesi

Considerato un determinato spazio delle ipotesi *H*, questo contiene sempre:

- L'**ipotesi più specifica**: ipotesi più stretta, consistente con i dati, nell'esempio del disco è il disco più stretto in grado di contenere tutti i punti negativi.
- L'**ipotesi più generale**: quella più grande, consistente con i dati, sempre nell'esempio del disco, è quello del disco più grande possibile e che non contiene punti positivi.

**shattering**: (_frammentazione_), dato $S$ sottoinsieme dello spazio delle istanze, si dice che $S$ è frammentato dallo spazio delle ipotesi $H$ se:

$$ ∀ S' ⊆ S, ∃ h ∈ H | ∀x \in S, h(x) = 1 \iff x \in S'.$$

Cioè $H$ realizza tutte le possibili dicotomie (suddivisione in due valori $S$).

$H$ frammenta un certo insieme $S$ se è possibile trovare un iperpiano che raccoglie tutti i punti dell'insieme $S$. Ovvero per tutte le dicotomie di $S$ esiste un iperpiano che riesce a realizzarle.

### VC (Vapnik-Chervonenkis) Dimension

La VC-Dimension è la dimensione di uno spazio delle ipotesi *H* definito su uno spazio delle istanze *X* ed è data dalla cardinalità del sottoinsieme più grande frammentato da *H* (massima cardinalità di punti $x$ in $X$ tale che $X$ può essere frammentato da $H$).

>$VC(H) = max(_{S ⊆ X})|S|$ tale che $H$ frammenta $S$
>
>$VC(H) = \infty$ se S non è limitato

Ad esempio nello spazio delle ipotesi dato dagli iperpiani su $\R^2$

Se nello spazio delle istanze ho 2 punti, questo viene frammentato da $H$, perché posso sempre trovare una retta che riesce a realizzare tutte le possibili dicotomie di due punti su un piano.

Se nello spazio delle istanze ho 3 punti, riesco comunque a realizzare tutte le dicotomie.

Se nello spazio delle istanze ho 4 punti qualsiasi non si riesce a trovare un iperpiano che realizza la dicotonomia, quindi $VC(H) = 3$.

Segue che, prendendo uno spazio delle ipotesi di cardinalità finita si ha che:

$$VC(H) ≤ log_2(|H|)$$

# HA FINITO QUA!!!

Questo perché per ogni *S* frammentato da *H*, abbiamo *|H| >= 2<sup>|S|</sup>*, cioè per ogni dicotomia in *S* esite un ipotesi in *H* che la realizza, ovvero devono essere disponibili in *H* tante ipotesi quanti sono le dicotomie in *H*.

Scegliendo un *S* tale che *|S| = VC(H)*, si ottiene *|H| >= 2<sup>VC(H)</sup>*, prendendo il logaritmo si trova quello che si stava cercando, ovvero *VC(H) <= log<sub>2</sub>(|H|)*.

**Dal libro**:

Se un dataset contiene *N* elementi, questi *N* elementi possono essere etichettati con degli 0 e 1 in $2^N$ modi diversi.

Se per ognuno di questi modi è possibile trovare un ipotesi *h ∈ H* che separa tutte le istanze negative da quelle positive allora si dice che *H* frammenta il dataset *N*. Il che vuol dire che il dataset *N* può essere appreso con un errore empirico nullo.

Il massimo numero di punti che possono essere frammentati da *H* è detto *VC(H)* e fornisce una misura della capacità di *H*.

## Bound sull'errore di generalizzazione

Considerando un problema di apprendimento binario, con: 

> Training set $S=\{(x_i,y_i)\}, i=1...N$</sub>
>
>Spazio delle ipotesi $H=\{h_0(x)\}$

Supponendo di avere un algoritmo di apprendimento *L* che restituisce l'ipotesi $h_0(x)$ che minimizza l'errore empirico su *S* espresso come $errore_S(h_0)(x))$.

È possibile derivare un bound (limite superiore) per l'errore ideale o errore di generalizzazione, valido con probabilità *(1 - δ)* con *δ* piccolo a piacere:

> errore<sub>D</sub>(h<sub>𝜃</sub>(x)) ≤ errore<sub>S</sub>(h<sub>𝜃</sub>(x)) + g(N, VC(H), δ)
oppure

$$error(g) < error_S(g) + F(\frac{VC(H)}{n},\delta)$$

In questo caso F è una funzione che ha come parametri la VC dimension dello spazio delle ipotesi H, n e delta (coefficente arbitrariamente piccolo).

#### Analisi del boud
I due termini del bound sono:
* $A = error_S(g)$, che dipende dall'algoritmo di apprendimento (è il minimo errore empirico osservato sui dati)
* $F(VC(H)/n,\delta)$ (chiamata __VC-confidence__), che dipende dal numero di esempi: all'aumentare del numero di esempi, l'approssimazione che ottengo dall'errore empirico si avvicina sempre di più all'errore reale. Viceversa, la *VC-dimension* dello spazio delle ipotesi è proporzionale alla complessità dello spazio delle ipotesi, quindi alla _VC-confidence_: al suo aumentare, aumenta il lasco del bound. Infine, all'aumentare di $\delta$, la _VC-confidence_ diminuisce ($\delta$ indica "bound vero con alta probabilità").

##### ROBA VECCHIA ########

Il primo termine *errore<sub>S</sub>(h<sub>𝜃</sub>(x))* dipende dall'ipotesi restituita dall'algoritmo di apprendimento L.

Il secondo termine *g(N, VC(H), δ)* non dipende da *L*, ma dal numero di esempi di training utilizzati (inversamente proporzionale), dalla *VC-dimension* (direttamente proporzionale) e dalla confidenza, ovvero dal termine *δ*.

Il termine *g(N, VC(H), δ)* viene anche chiamato **VC-confidence** e risulta essere monotono rispetto al rapporto *VC(H)/N*.

##### FINE ROBA VECCHIA ######

## Structural Risk Minimization (SRM)

Approccio per la scelta dello spazio delle ipotesi proposto da Vapnik che cerca di trovare un compromesso tra l'errore empirico e la VC-Confidence.

Si considerano spazi delle ipotesi sempre più piccoli H<sub>1</sub> ⊆ H<sub>2</sub> ⊆ ... ⊆ H<sub>n</sub> tali che VC(H<sub>1</sub>) ≤ VC(H<sub>2</sub>) ≤ ... ≤ VC(H<sub>n</sub>)

Si seleziona lo spazio delle ipotesi $H_i$ che ha il valore del bound sull'errore di generalizzazione più piccolo. Nell'immagine sottostante, ad esempio, verrebbe scelta la $g$ con spazio di ipotesi $H_2$ (perché l'obiettivo dell'aprrendimento è minimizzare l'errore ideale, non quello empirico!)

![](./immagini/l5-srm.png)