# Lezione 22 - Natural Language Processing 2

> Nota bene: la prima parte l'ho saltata (era in coda alla lezione 21) causa discussione di Ludo.

## Modello n-gram

Il testo scritto è composto da caratteri (lettere, spazi e punteggiatura). Il modello basato su caratteri è _n-gram_: è il modello di linguaggio definito come distribuzione di probabilità su una sequenza di caratteri

$P(c_{1:N})$ = La probabilità di una sequenza di N caratteri, da $c_1$ a $c_n$.

Una sequenza di simboli scritti di lunghezza $n$ è chiamata _n-gram_. Ci sono dei casi speciali: unigram, bigram e trigram (1, 2 e 3 caratteri "precedenti" salvati). Ad esempio, su una pagina web in inglese i caratteri più frequenti saranno i "the", quindi P("the") = 0.027, mentre P("zpq") = 0.0000000002.

In generale, quando si parla di un modello _n-gram_, si parla di una catena di _Markow_ di ordine $n-1$. In pratica, la probabilità di un carattere $c_i$ si assume dipendere solo dalla probabilità dei caratteri immediatamente precedenti (indipendenza condizionale: il carattere $c_{i}$ è condizionalmente indipendente da quelli che lo seguono, dati $c_{i-1}$ e $c_{i-2}$). Ad esempio, in un modello di trigram (catena di Markow di ordine 2) abbiamo $P(c_i|c_{1:i-1}) = P(c_i|c_{i-2 : i-1})$
Possiamo definire $P(c_{1:N})$ sotto il modello del trigram fattorizzando con la regola della catena e quindi usando l'assunto di Markov:

$$
P(c_{1:N}) = \prod_{i=1}^N P(c_i|c_{1:i-1}) = \prod_{i=1}^N P(c_i|c_{i-2:i-1})
$$

Con i modelli _n-gram_ si può:

- Identificare una lingua (L) costruendo i modelli statistici per le varie lingue che ci interessano. Per ognuna di esse costruiamo un modello contando i trigrammi in un blocco di testo di quella lingua specificia, e questo ci da la probabilità $P(Testo|lingua)$. Per selezionare la lingua più probabile si cerca la $L$ per cui è massimizzata l'espressione $P(L)\cdot P(c_{1:N}|L) = P(L) \cdot \prod_{i=1}^N P(c_i|c_{i-2:i-1}, L)$. Ci sono due problemi:

- Sono necessari "corpus" abbastanza lunghi
- Difficile stimare la priorità a priori della lingua, quindi $P(L)$

Per quest'ultima, si possono utilizzare pagine web prese a campione (casuale). I modelli _n-gram_ possono essere utili anche nella:

- Correzione ortografica (soprattutto inversione di caratteri, come "csaa" invece che "casa");
- Determinazione del topic del documento ("politico" o "storico" o "tecnico").

Il problema sta nel campionamento di trigrammi rari: se non riusciamo mai a campionarlo, la sua probabilità stimata sarà 0, quindi manda tutto in barba con la fattorizzazione (si moltiplica il tutto per 0). Soluzione? Lo smoothing!

## Smoothing

L'idea è quella di regolarizzare la probabilità dei conteggi a bassa frequenza su una probabilità piccola diversa da zero. Un approccio molto semplice è lo smoothing di _Laplace_: se una variabile booleana X è falsa in **tutte** le $n$ osservazioni, allora $P(X = true)$ sarebbe 0. Posso però "immaginarmi" di avere fatto altre due estrazioni immaginarie trovando tutti i valori del dominio (ovvero un'estrazione ha dato "true" e una "false"). Quindi, $P(X = true) = \frac1{n+2}$. Questo ci garantisce che non avremmo mai stime di probabilità a 0: tanto più piccolo sarà $n$, tanto più piccola sarà la probabilità $P(X = true)$.

Un approccio migliore è il modello di backoff. Si inizia stimando i conteggi di _n-gram_. Se in una sequenza di _n_ caratteri ha un conteggio basso o nullo, torniamo a _n-1 - gram_.
Il _linear interpolation smoothing_ è un modello di _backoff_ che combina trigram, bigram e unigram per interpolazione lineare:

$\hat{P}(c_i | c_{i-2:i-1}) = \lambda_3 P(c_i | c_{i-2:i-1}) + \lambda_2 P(c_i | c_{i-1}) + \lambda_1 P(c_i)$

con $\lambda_3 + \lambda_2 + \lambda_1 = 1$

## Valutazione del modello

Per fare la stima di bontà di un modello non avendo tanti dati è fare la cross-validation: l'idea è quella di suddividere i dati in "fold" più o meno della stessa dimensione (_k-fold_ Cross Validation divide il training set in _k_ partizioni). Una volta fatto questo, si va ad allenare il modello in tutti i $k-1$ fold, tenendo il fold escluso come _test set_ e andando a cambiare il fold usato come test set ad ogni iterazione ($k$ iterazioni ovviamente!). Si vanno poi a combinare gli errori e si ottiene un errore totale.

## Perplexity

Gioco di Shannon: dato un pezzo di frase, prevedere la prima parola mancante.

## Chain-rule per n-gram

Obiettivo: calcolare la probabilità di una frase (sequenza di parole): $P(W) = P(w_1 w_2 w_3..w_n)$. Un modello di linguaggio è un modello che calcola $P(W)$ oppure $P(w_1 w_2 w_{n-1})$

arrivato fino a "Classificazione di testi" esclusa
