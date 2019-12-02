# Lezione 15 - Apprendimento Bayesiano

Si tratta di algoritmi di apprendimento basati sulla probabilità e sul teorema di Bayes.

## Scelta delle ipotesi

Tutto si basa sulla formula di Bayes.

$$ P(h|D) = \frac{P(D|h)\cdot P(h)}{P(D)}$$

L'obiettivo è quello di massimizzare _P(h|D)_, sapendo _P(D|h)_ che viene fornito dal supervisore e _P(h)_ che viene appresa.

Nel massimizzare si può tralasciare il termine _P(D)_ dal momento che è sempre costante.

$$h_{MAP} = argmax_{[h ϵ H]} P(h|D)P(D)$$

Si può inoltre assumere che tutte le ipotesi _h_ abbiano la stessa probabilità e nel mondo reale questa assunzione è tipicamente corretta, il problema di massimizzazione diventa:

$$h_{ML} = argmax_{[h ϵ H]} P(h|D)$$

A pagina 158 del Mitchel c'è un esempio che mette in evidenza come le probabilità a priori influenzino il risultato.

## Brute Force MAP Learning (interpretazione Find-S)

Si assumono fissate le istanze x1 ... xn.

Si assume D essere lìinsieme de_i valori derisderati D
= {c(x1)...c(xn)}

Considerando tutte le ipotesi equiprobabili: _1/|H|_

> P(D|h) = 1 se h è consistente con gli elementi di D
>
> P(D|h) = 0 altrimenti

Supponiamo inoltre che non sia presente del rumore.

In questo modo la probabilità _P(h|D)_ si ottiene applicando la regola di Bayes, in particolare:

> P(h|D) = 0 se h è non è consistente con D
>
> P(h|D) = 1/VS<sub>H,D</sub> se h è consistente con D

Quindi se tutte le ipotesi _h_ sono equiprobabili, allora qualsiasi ipotesi presente in _H_ va bene con probabilità _1/VS<sub>H,D</sub>_.

Se vengono cambiate le probabilità in modo che la probabilità di un'ipotesi più specifica sia più alta si ottiene che _P(h|D) = P(h)_.

## Apprendimento di una funzione a valori reali (ML)

$$ d_i = f(x_i) + e_i$$

dove e_i è l'errore che segue una probabilità gaussiana con media 0 di cui non si conosce la varianza.

> e_i = di - f(x_i)

Però si vuole valutare l'errore come se al posto di _f_ (che è sconsociuta) ci fosse _h_

> e_i = di - h(x_i)

La probabilità di _P(di|h)_, cioè che l'ipotesi _h_ classifichi correttamente d_i segue la distribuzione guassiana di e_i.

> h<sub>ML</sub> = argmax<sub>[h ϵ H]</sub> P(D|h)
>
> h<sub>ML</sub> = argmax<sub>[h ϵ H]</sub> (produttoria) P(di|h)
>
> h<sub>ML</sub> = argmax<sub>[h ϵ H]</sub> (produttoria) gaussiana di (di-h(x_i))

Dal momento che la gaussiana contiene un'esponenziale, conviene utilizzare il logaritmo, tanto per il problema di massimizzazione è la stessa cosa.

Da notare che, all'interno dell'argmax, $\frac{1}{\sqrt{2\pi\sigma^2}}$ è costante rispetto h, quindi può essere eliminato.

Anche $\frac{1}{{2\sigma^2}}$ è costante, quindi può essere evaporato.
**fai screen delle slide per i conti**

Segue quindi che

> h<sub>ML</sub> = argmin<sub>[h ϵ H]</sub> (sommatoria)(di-h(x_i))<sup>2</sup>

Quindi per trovare l'ipotesi **max_imum likelihood** è necessario minimizzare l'errore quadratico, sotto le ipotesi che la probabilità di ogni ipotesi è uniforme e assumendo che non ci sia rumore ne_i dati di training.

## Apprendimento di una ipotesi che predice probabilità

Data una funzione probabilistica (non deterministica) $f: X \to \{0,1\}$, voglio apprendere con una rete neurale $f^1: X \to [0,1]$, che predica la probabilità che $f(x) = 1$ per un dato $x$. Vogliamo quindi trovareu un criterio per trovare un'ipotesi di Maximum Likelihood per f'.

Per farlo, dobbiamo prima definire la probabilità di D dato h: $P(D|h)$.

$$ P(D|h) = \prod_{i=1}^{m} P(x_i, d_i|h) $$
che, dopo un po' di calcoli, diventa:

$$ P(D|h) = \prod_{i=1}^n h(x_i)^{d_i}\cdot (1-h(x_i))^{1-d_i} \cdot P(x_i) $$
Applicando la regola di maximum likelihood, posso eliminare $P(x_i)$ perché non dipende da h! Applicando anche il logaritmo, ottengo una formula che è simile all'entropia.

### Classificazione più probabile per nuove istanze

Finora abbiamo cercato l'ipotesi più probabile per i dati $D(h_{MAP})$, ma dato un nuovo esempio, qual'è la classificazione più probabile?

Supponiamo di avere $P(h_1|D)=0.4, P(h_2|D)=0.3, P(h_3|D)=0.3$, data una nuova istanza _x_ può succedere che $h_1(x) = (+)$ e $h2(x) = h3(x) = (-)$. Quindi considerando le tre ipotesi, la classificazione più probabile è $(-)$ e non $(+)$.

Segue che la **classificazione ottima di Bayes**:

$$ arg max_{v_j \in V} \sum_{h_i \in H} P(v_j|h_i)P(h_i|D) $$

Si va cioè a considerare tra tutte le ipotesi, pesate per la loro probabilità, e si considera come classe quella che compare più volte.

#### Classificazione di Gibbs

Il classificatore ottimo di Bayes potrebbe essere molto costoso da calcolare se ci sono tante ipotesi.

Si può tulizzare un'alternativa, scegliendo un ipotesi a caso, secondo la probabilità $P(h|D)$ e utilizzando quell'ipotesi per classificare la nuova istanza, si ottiene un errore medio minore del doppio dell'errore medio che si ottiene utilizzando il classificatore ottimo.

$$ E[errore_{Gibbs}] \le 2 \cdot E[errore_{OttimoBayes}]$$

Sempre assumendo probabilità uniforme per tutte le ipotesi del version space.
