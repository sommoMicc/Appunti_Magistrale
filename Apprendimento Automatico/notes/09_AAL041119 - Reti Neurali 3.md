# Reti Neurali 3
Lunedì 4 Novembre 2019

## Rete di Perceptron

![](./immagini/l10-rete.png)

![](./immagini/l10-rete-parametri.png)

E rappresenta l'errore quadratico medio di tutte le unità di output.

### Calcolo dei pesi per le unità di output

Calcoliamo i pesi per le unità di output, considerando i livelli nascosti come se fossero degli ingressi.

$w_{\hat{k},\hat{j}}$ indica il "soggetto" della derivata parziale. Quindi $\hat{k}$ indica il neurone di output colorato in blu nella figura sottostante.

I $w_i$ adesso diventano $\Delta w_{\hat{k},\hat{j}}$ perché i pesi vengono calcolati per ogni collegamento da un'unità nascosta $j$ all'unità di output $k$.

![](./immagini/l10-rete-output.png)

Nel secondo passo sono state fatte due operazioni, prima viene tolta la sommatoria, perché quando viene fatta la derivata della sommatoria c'è un solo elemento diverso da ed è quello di indice *k^=k*.

### Calcolo dei pesi per le unità nascoste

![](./immagini/l10-rete-input.png)

2019: Aiolli ha spoilerato che non chiede all'esame la dimostrazione. Chiede invece lo scopo della dimostrazione

### Algoritmo di apprendimento

L'algoritmo di apprendimento lavora in due fasi: nella prima fase, detta **feed forward**, viene fornito in input alla rete un esempio del training set, in modo che questa possa provare a calcolare la funzione target per l'esempio. Una volta calcolata si passa alla fase di **backward progragation**, nella quale si aggiornarno i coefficenti delle unità di output e delle unità nascoste in base alla correttezza o meno della predizione. In questo caso l'apprendimento avviene a ritroso:
- Prima viene calcolato l'output (fase __forward__);
- Poi vengono aggiornati i coefficenti delle unità di output;
- Infine, vengono aggiornati i pesi dei livelli nascosti.

![](./immagini/l10-apprendimento-rete.png)

Il passo 2 dell'algoritmo rappresenta il calcolo della differenza tra l'output atteso e quello ottenuto, questo viene poi utilizzato per aggiornare a ritroso i valori dei nodi interni (passo 3).

L'algoritmo prende il nome di **back propagation stocastico** perché il valore dei $\Delta w_i$ viene aggiornato subito dopo aver valutato un esempio *x* e non solamente dopo aver valutato tutti gli esempi del training set.

Le possibili condizioni di terminazione sono le stesse che si hanno quando c'è un solo neurone.

## Discesa Batch vs. Stocastica
- __Batch__: è molto pesante computazionalmente
- __Stocastica__: per ogni esempio viene calcolato il suo contributo al gradiente. Tuttavia, è meno preciso perché il gradiente è un'approssimazione.
- __Mini-Batch__: vengono considerati pochi esempi per volta in batch, non tutto il training set!!

## Esempio di funzioni errore
Le funzioni che si ottengono sono molto complesse. Inoltre, minimizzare l'errore è difficile perché la funzione errore, in quanto complessa, ha molti minimi locali.

## Universalità delle reti multistrato
Le reti neurali sono dei buoni approssimatori: una rete neurale a tre strati (con un solo livello nascosto) riesce ad approssimare con una precisione arbitraria ($\epsilon > 0$) una qualsiasi funzione continua $f: \R^n \to \R$ usando almeno $M$ unità nascoste. Da notare che viene teorizzata l'esistenza di $M$ ma non viene data nessuna formula per calcolarlo (_Teorema di Pinkus).

## Alcuni problemi
- Il numero di unità nascoste determina la complessità dello spazio delle ipotesii
- La scelta di $\eta$ può essere determinante per la convergenza: valori troppo bassi determinano convergenze molto lente, mentre valori troppo grandi potrebbero portarci a divergere dall'ottimo (invece che convergere ad esso)
- L'apprendimento della rete è lento (quantomeno rispetto al calcolo dell'output)
- Presenza di minimi locali nella funzione errore. Per evitarli si può:
    - Aggiungere un termine (__momento__) alla regola di update dei pesi, che determina una "inerzia del sistema": al passo $t+1$ si tiene conto anche della direzione del gradiente del passo $t$.
    - Usare apprendimento stocastico, ovvero inserire una randomizzazione sugli esempi, che permette di "uscire" dal bacino dei minimi locali (rispetto all'apprendimento batch)

## Rappresentazioni dei livelli nascosti
Una caratteeristica importante delle reti neurali multistrato è che permettono di scoprire rappresentazioni alternative all'input dei dati di ingresso. Praticamente, ogni strato hidden della rete neurale prende come input una rappresentazione ulteriore diversa dell'input, che viene appresa automatcamente dall'algoritmo di backpropagation.

La rete neurale della slide ha input e output uguali e viene detta "auto-encoder".