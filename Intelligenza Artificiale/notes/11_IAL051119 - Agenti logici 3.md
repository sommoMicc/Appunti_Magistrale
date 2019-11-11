# Agenti logici 3
Martedì 5 Novembre 2019

## Regola di risoluzione

**Forma normale congiuntiva (CNF)**: forme di scrittura che utilizza congiunzione di disgiunzione di letterali (dove la disgiunzione di letterali è una clausa di Horn).

$$ (A \vee \neg B) \wedge (B \vee \neg C \vee \neg B) $$

La **risoluzione** è una regola di inferenza per CNF completa e corretta per la logia proposizionale.

![](./immagini/l12-risoluzione.png)

dove $P_{i,j}$ sta per "pit" in posizione $i,j$ (nel mondo dei Wompoos).

In pratica si va a togliere un $l_i$ e $m_j$ che sono tra loro complementari (lo stesso letterale sia negato che non).

Questo procedimento esegue la verifica del modello perché vuol dire che se *L* e *M* sono vere, anche la proposizione che si deduce è vera, quindi vuol dire che il letterale tolto non influenzava la verità di *L* e *M*.

La **correttezza** di questa regola è semplice, se tolgo dalla clausola *L* il letterale *l* e dalla clausola *M* il letterale *m* che è complementare a *l*, allora se *l* è vero allora *m* è falso e quindi *M* deve essere vero e non a causa di *m*. Se *l* è falso, allora *L* deve essere vero senza *l*. Il valore di *l* quindi non incide ne in una clausola ne nell’altra, quindi la sua eliminazione non altera il valore delle clausole.


### Conversione in CNF

> B<sub>1,1</sub> <==> (P<sub>1,2</sub> ⋁ P<sub>2,1</sub>)

C'è brezza in posizione 1,1 se e solo se c'è un Pit in posizione 1,2 o c'è un Pit in posizione 2,1

1. Eliminare il se e solo se, rimpiazzandola con $(\alpha \implies \beta) \wedge (\beta \implies \alpha)$
> (B<sub>1,1</sub> => (P<sub>1,2</sub> ⋁ P<sub>2,1</sub>)) ⋀ ((P<sub>1,2</sub> ⋁ P<sub>2,1</sub>) => B<sub>1,1</sub>)

2. Eliminare il => rimpiazzando A => B con !A ⋁ B
> (!B<sub>1,1</sub> ⋁ P_1,2 ⋁ P_2,1) ⋀ (!(P_1,2 ⋁ P_2,1) ⋁ B_1,1) 

3. Spostare la negazione all'interno delle parentesi usando le regole di De Morgan (con la negazione di una sentenza, i connettori si invertono: AND diventano OR e OR diventano AND)
> (!B<sub>1,1</sub> ⋁ P<sub>1,2</sub> ⋁ P<sub>2,1</sub>) ⋀ ((!P<sub>1,2</sub> ⋀ !P<sub>2,1</sub>) ⋁ B<sub>1,1</sub>) 

4. Si applica la legge distrubutiva dell'OR sull'AND
> (!B<sub>1,1</sub> ⋁ P<sub>1,2</sub> ⋁ P<sub>2,1</sub>) ⋀ (!P<sub>1,2</sub> ⋁ B<sub>1,1</sub>) ⋀ (!P<sub>2,1</sub>) ⋁ B<sub>1,1</sub>) 

A questo punto abbiamo la CNF.

### Algoritmo risolutivo

La **regola di risoluzione** è le regola di inferenza precedentemente vista, l'algoritmo di risoluzione è quello che applica più volte la regola di risoluzione per andare a risolvere il problema.

L'algoritmo funziona per contraddizione, cioè va a dimostrare che $KB \wedge \neg \alpha$ è insoddisfacibile.

Se risolvendo $KB \wedge \neg \alpha$ viene trovata la clausola vuota, allora vuol dire che $KB \wedge \neg \alpha$ è insoddisfacibile e di conseguenza KB |= 𝜶.

Da notare che l'algoritmo dice se 𝜶 è conseguenza logica o meno dalla KB, senza fornire una prova del risultato.

```
function CP-Risoluzione(KB, 𝜶) return true oppure false
    clausole <- insieme di clausole nella rappresentazione CNF di $KB \wedge \neg \alpha$
    new <- {}
    loop do
        foreach C_i C_j in clausole do
            resolvents <- CP-Risolvi(C_i, C_j)
            if resolvents contiene la clausola vuota then return true
            new <- new ∪ resolvents
        if new ⊆ clausole then return false
        clausole <- clausole ∪ new
```

`CP-Risolvi(C_i, C_j)` restituisce l'insieme dei risolventi ottenuti applicando la regola di risoluzione in tutti i modi possibili per le due clausole. Questo perché data una coppia di clausole è possibile risolverle in più modi diversi. 

Per prima cosa è necessario convertire il tutto in CNF, quindi si applica la regola di risoluzione alle clausole risultati. 

Ogni coppia che contiene letterali complementari è risolta per produrre una nuovo clausola che viene aggiunta all’insieme.

Il processo continua finché:

- non è più possibile aggiungere alcuna clausola, in questo caso KB non implica 𝜶
- la risoluzione applicata a due clausole da come risultato la clausola vuota, in questo caso KB implica 𝜶

La clausola vuota, una disgiunzione senza alcun disgiunto è equivalente a *False* perché una disgiunzione è vera solo se è vero almeno uno dei disgiunti.

L'algoritmo è un po' meta, quindi non dice effettivamente che strategia adottare per risolvere le clausole (cioè l'ordine di espansione). Per trovare una contraddizione, dobbiamo trovare "la clausola più corta di tutte" (la clausola vuota). In una derivazione, l'unico modo per ridurre il numero delle clausole è avere una delle due sentenze composta da solo una clausola.

La complessità dell'algoritmo di risoluzione è esponenziale per il numero di simboli nella base di conoscenza e in 𝜶.

## Esempio di risoluzione
L'$\alpha$ e $\neg P_{1,2}$, quindi $\neg \alpha$ è $P_{1,2}$. Le regole che compaiono sono risultati della derivazione effettuata precedentemente (qualche slide più inidietro) ottenuta applicando le CNF. Il resto dell'esempio è praticamente un degheio, ma alla fine si genera una contraddizione, quindi $\alpha$ è conseguenza logica della base di conoscenza

## Completezza della Risoluzione

**Completezza**: riesce a dedurre tutto quello che può essere dedotto dalla base di conoscenza.

Il teorema di completezza per la risoluzione nella logica proposizionale è chiamato **ground resolution theorem**: se un insieme di clausole S è insoddisfacibile, allora la chiusura della risoluzione di tali clausole RC(S) contiene la clausola vuota.

Nel nostro caso S è la base di conoscenza in ⋀ con la negazione di 𝜶.

**insoddisfacible**: non esite un modello per l'insieme di clausole, ovvero non esiste una combinazione dei letterali che rende vero l'insieme delle clausole.

La dimostrazione di questo teorema si ottiene dimostrando (per assurdo) che se la chiusura RC(S) non contiene la clausola vuota, allora S è soddisfacibile.

Se la chiusura di S **non contiene** la clasusola vuota si può costruire un modello per S, perché se c'è una clausola vuota vuol dire che c'è una contraddizione e quindi non è possibile costruire un modello.

Si può provare quindi a costruire un modello a partire dai vari letterali $P_1$, ..., $P_k$ che compaiono in S.

Quindi, per ogni $P_i$:

- Se esiste una clausola in RC(S) contiene $\neg(P_i)$ e tale che tutti gli altri letterali della clausola sono falsi a causa dei valori di verità già assegnati ai P precedendi, allora assegna il valore di verità falso a $P_i$.
- altrimenti assegna a $P_i$ vero.

Questo perché sto cercando di creare un modello per RC(S) e ad ogni passo cerco un valore per $P_i$ in modo che non ci siano clausole che non sono soddisfatte.

Tenendo presente che in RC(S) non c'è la clausola vuota per ipotesi, rimane da dimostrare che tale procedura termina sempre e produce un modello per S.

Questo si dimostra per induzione su i: supponiamo che sia possibile costruire il modello parziale per i simboli fino a $P_{i-1}$ e mostriamo che tale modello può essere esteso fino a $P_i$>.

**Caso base: i = 1**

In questo caso, in RC(S) non possono essere presenti sia $P_1$ sia $\neg P_1$, perché altrimenti l'applicazione dell'algoritmo di risuluzione non sarebbe terminata, questo perché le due clausole $P_1$ e $\neg P_1$ possono essere risolte con la clausola vuota. Quindi è presente solo o $P_1$ o $\neg P_1$ e di conseguenza $P_1$ vale falso se è presente $\neg P_i$, altrimenti vero. 

Questa scelta è vincolata perché stiamo cercando di costruire un modello per S. 

**Caso induttivo:**

Consideriamo una clausola C in RC(S) che contiene $P_i$, si hanno dei problemi ad assegnare un valore di verità a $P_i$ solo se C equivale a B ⋁ $\neg P_i$, con B clausola che contiene solo simboli $P_j$ con *j < i*, cioè simboli ai quali ho già fissato un valore di verità, ed esiste C' in RC(S) ed equivalente a B' ⋁ $P_i$ con B' clausola che contiene solamente simboli $P_j$ con *j < i*.

Il problema della scelta del valore è che, per rendere vera sia C che C', $P_i$ dovrebbe essere sia vero sia falso, e quindi non si sa cosa scegliere.

Ma, se esistono queste due clasuole, in RC(S) deve essere presente anche la clausola B ⋁ B' altrimenti RC(S) non è la chiusura, questo perché se riduco C con C' ottengo B ⋁ B'.

Per l'ipotesi induttiva, l'assegnamento parziale fino a $P_{i-1}$ non può rendere falsa sia B che B' (questo per come sono stati scelti i valori).

Quindi, se B è falsa allora $P_i$ è falso e se invece B' è falso allora $P_i$ è vero, ottenendo così un modello parziale fino all'indice *i*.

Quando *i* coincdice con *k* si ottiene un modello completo per *S* e di conseguenza *S* è soddisfacibile.

