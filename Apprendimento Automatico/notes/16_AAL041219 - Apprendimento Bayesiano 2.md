# Metodi Bayesiani - Naive Bayes e EM

## Naive Bayes

Ha la caratteristica di essere molto efficente (e molto semplice). Questo lo ha reso popolare su particolari applicazioni (diagnosi, classificazione di documenti testuali), in quanto efficace quanto altre soluzioni più complesse.
Per poterlo utilizzare servono:

- Insieme di dati abbastanza grande (come tutti i metodi basati sulla distribuzione di probabilità);
- Gli attributi che descrivono le istanze sono condizionalmemente indipendenti data la classificazione: se un argomento parla di sport, allora la probabilità che in un documento ci sia una parola è indipendente rispetto la probabilità che ce ne sia un'altra. Questo punto è _opinabile_: cioè Naive Bayes funziona bene anche senza rispettare questa caratteristica. In realtà mi interessa solo che la probabilità della classe corretta sia maggiore della probabilità delle altre classi (l'ordine deve essere preservato, mentre non è necessario riuscire a stimare esattamente la probabilità della classificazione).

### Dettaglio

$f: X \to V$ , con istanze x descritte da attributi $⟨a_1,a_2,...,a_n⟩$.
L'obiettivo è massimizzare in tutte le classi la probabilità di ottenere $v_j$ dati $a_1,..,a_n$. Si ha che:

$$ v_{MAP} = arg\,max_{v_j \in V} P(v_j|a_1,..,a_n)$$
alla fine, applicando Bayes, ottengo:

$$ v_{MAP} = arg\, max_{v_j \in V} P(a_1,..,a_n|v_j) \cdot P(v_j)$$

Il problema qua è che devo stimare $k^n$ probabilità diverse: per ogni combinazione di un valore di $a_1$, $a_2$ e $a_n$ dovrò stimare la loro probabilità. Di conseguenza, devo avere un numero ancora più grande di dati di training!

L'approccio che si usa su Naive Bayes è l'assunzione di indipendenza: assumiamo che la probabilità che un certo attributo abbia un certo valore è indipendente rispetto la probabilità di un altro attributo di avere un altro valore. Questa assunzione consente di fattorizzare le probabilità:

$$ P(a_1,a_2,..,a_n|v_j) = \prod_i P(a_i|v_j)$$

Così facendo dovrò calcolare "solo" $k \cdot n \cdot q$, dove $q$ è il numero di valori che può assumere un attributo: diminuisce il numero di probabilità che bisogna calcolare!

Congiungendo il tutto si ottiene che la classe che massimizza la probabilità a posteriori è:

$$ v_{MAP} = arg\,max_{v_j\in V} P(a_1,a_2,..,a_n|v_j) \cdot P(v_j)$$ se $ P(a_1,a_2,..,a_n|v_j) = \prod_i P(a_i|v_j)$

quindi il classificatore Naive Bayes è:

$$ v_{NB} = arg\,max_{v_j\in V} \prod_i P(a_i|v_j)$$

### Algoritmo

Per ogni valore target:

- Si stima il valore di $P(v_j)$ (quantità di istanze di classe $v_j$ rispetto al totale);
- Per ogni possibile valore dell'attributo a:
  - Sulle istanze di classe $v_j$, andiamo a vedere quante istanze hanno valore di i attributo $a$
- Quando ho stimato i valori di tutti gli attributi, posso ritornare tali valori

Quindi, l'ipotesi Naive Bayes è $v_{NB} = arg\,max_{v_j\in V} \hat{P}(v_j) \prod_i \hat{P}(a_i|v_j)$

### Esempio del tennis

La classe è "PlayTennis", quindi "Si" o "No". Dobbiamo decidere in base all'istanza degli attributi se è il caso di giocare a tennis quel giorno.

Il numero di valori sono:

- 3 per "Outlook"
- 3 per "Temperature"
- 2 per "Humidity"
- 2 per "Wind"

I possibili valori sono quindi 36. Abbiamo da stimare 36 \* 2 + 2 (probabilità delle classi) valori di probabilità.

La probabilità di "Yes" è $\frac9{14}$, quindi quella di "No" è $\frac5{14}$.

La probabilità di outlook=sunny dato "Yes" è $\frac29$ (somma del numero di righe in cui "outlook" = "Sunny" e "PlayTennis" = "Yes" fratto il numero di righe di "PlayTennis" = "Yes").

### Considerazioni

L'assunzione di indipendenza è spesso violata: quando è "sunny", la temperatura tende ad essere più alta, ad esempio.

Quindi, perché funziona? Perché a noi non serve che la stima $\hat{P}(a_i|v_j)$ sia corretta, ma basta che:

$arg\,max_{v_j\in V} \hat{P} \prod_i \hat{P}(a_i|v_j) =  arg\,max_{v_j\in V} {P} \prod_i P(a_i|v_j)$

Inoltre, avere un solo valore di probabilità nullo significa avere l'intera stima di $v_j$ nulla.

Una soluzione tipica è l'utilizzo della _m-stima Bayesiana_:

$$ \hat{P}(a_i|v_j) = \frac{n_c+mp}{n+m} $$
Dove $m$ è un peso che si da a certi esempi "virtuali": l'idea è aggiungere nuovi esempi virtuali (che non esistono) a cui viene assegnato un valore per l'attributo $a$ secondo una certa distribuzione (distribuzione $p$). Il caso più semplice del valore di $p$ è la probabilità uniforme su tutti i valori degli attributi di $a$: $\frac{1}{|a|}$.

In pratica fare questa operazione comporta aggiungere altri $m$ esempi e assegnare il valore dell'attributo $a$ a caso tra i $k$ (cioè $|a|$, cardinalità di $a$) possibili valori di $a$.

## Applicazioni di Naive Bayes su documenti testuali

Si usa per identificare il tipo/l'argomento dei documenti.

Ogni documento è rappresentato come un vettore di parole, e ogni posizione del vettore avrà un valore (la parola che compare in quella posizione del documento). Il mio concetto target è una funzione $f$ che dato un qualsiasi documento siffatto restituisce "+" o "-" (è il mio target o non è il mio target).

L'assunzione che si fa è che le parole, una volta scelta la classe del documento, vengano estratte "coerentemente" con la stessa (termini sportivi in documenti di sport, "Trump" o "Parlamento" in documenti di impronta politica ecc).

Un'assunzione addizionale fatta è che la probabilità che compaia un termine in una data posizione del documento non comporta niente per i termini successivi (non li condiziona): per ogni posto del documento, la probabilità che una determinata parola venga estratta è sempre la stessa. Ovvero: $P(a_i = w_k|v_j) = P(a_m = w_k|v_j)\,  \forall i,m$

## Expect Maximization

In un'applicazione spesso si hanno dati non osservabili. Ad esempio, le due Gaussiane presenti nelle slide presentano dei parametri non noti (ad esempio, conosciamo la varianza ma non la media delle gaussiane).
Inoltre, non si sa, per ogni istanza $x_i$ quale sia stata la gaussiana che l'ha generata (valore non osservabile). Il task di questo esempio è di stimare il meglio possibile le medie $\mu_1,..,\mu_k$.
