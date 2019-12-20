# Lezione 23 - Natural Language Processing 2

## Classificazione di testi (pag 864 del libro, 878 del PDF del libro)

Spam vs ham: vogliamo buttare via la salsa schifosa e tenere il prosciutto.
Nei messaggi di spam sembrano esserci degli _n-gram_ più comuni, come "for cheap" e "you can buy", ma non necessariamente le mail che contengono quesste parole sono spam.

Quindi, per effettuare la classificazione possiamo:

- Tirar giù delle regole di classificazione codificate a mano. In questo approccio si valutano combinazioni di parole, presenza di link nella mail, mittente in blacklist ecc. Il problema è che se le tecniche usate dagli spammer cambiano, bisognerà riscrivere le regole. In questo approccio ci si può avvalere a supporti di basi di conoscenze già compilate.
- Utilizzare della modellistica linguistica e apprendimento automatico. Nel primo si definisce:

  - Un modello _n-gram_ nella cartella spam: $P(message|spam)$;
  - Un modello _n-gram_ nella cartella _posta in arrivo_: $P(message|ham)$. Questi due punti sono possibili perché io (utente) separo le mail di spam da quelle di ham, mettendo le prime nella cartella spam e lasciando le altre nella posta in arrivo.
  - Ogni messaggio viene classificato con la regola di bayes: $argmax_{c \in \{spam, ham\}} P(c|message) =\\ argmax_{c \in \{spam, ham\}} P(message|c) \cdot P(c)$ dove $P(c)$ è stimato contando il numero totale di _spam/ham_. Ovvero, in caso di $c=spam$, $P(c)$ indica il numero di messaggi di spam sul totale.
  - Generalmente si usa un classificatore **Naive Bayes**, che può essere costruito incrementalmente, ovvero le stime di probabilità possono essere aggiornate ogni volta che arrivano nuovi esempi.

Per il classificatore **Naive Bayes** si può eliminare il denominatore perché ci interessa l'argomento del valore massimo, non il valore in sé.

Quando la distribuzione di probabilità del prior $P(c), c \in C$ è uniforme (uguale per tutte le classi, $\frac1{|C|}$), conta solo la likelihood, quindi si fa una stima _maximum likelihood_.

Per calcolare la probabilità nel calcolo di $c_{MAP}$, ovvero $P(x_1,x_2,..,x_n |c)$ servirebbe una quantità di memoria ingente, una mega-tabella. Si può utilizzare un assunto di **indipendenza condizionale**, ovvero si suppone che $P(x_i|c)$ sia indipendente dalla classe $c, \forall i$. Questa idea sta alla base del classificatore _Multinomial Naive Bayes_:

$$ arg\, max_{c \in C} P(c) \prod_{x \in X} P(x|c)$$

Ci possono essere dei documenti, come gli articoli di giornale di cronaca sportiva, che potrebbero avere più di una etichetta/classificazione (cronaca e sport, nell'esempio).

Una rappresentazione alternativa agli _n-gram_: **Bag of Words**. In pratica, per ogni parola del documento si considera la frequenza con cui essa appare, e questa frequenza viene salvata in un vettore(es: $BoW_1 = \{John: 1, likes: 2, to: 1, watch: 1\}$ ). Il modello Bag of Words può essere applicato anche a bigram e trigram ecc, semplicemente considerando la frequenza con cui ogni bigramma, trigramma o n-gramma compare nel documento.

Se in associazione al BoW si usa un n-gram di ordine > 1, si mantiene un ordine locale delle parole ("John likes", "Likes to"), ma la complessità computazionale aumenta all'aumentare dell'ordine.

In Natural Language Processing le parole sono considerati simboli discreti, e ogni parola è equidistante da tutte le altre. Una rappresentazione **di una parola/simbolo** "compatta" molto frequente è quella _one-hot_: vettore con 1 solo in posizione corrispondente alle parole presenti (ottengo quindi vettori ortogonali). E' strano ma ogni parola è vista come un simbolo. Questo ci permette di avere una rappresentazione che non induce metriche di similitudine tra simboli.

Putroppo, nella lingua reale, le distanze tra parole sono diverse: ad esempio "Hotel" e "Motel" hanno due significati molto simili, ma hanno una codifica _one-hot_ completamente diversa.

## Rappresentare le parole in base al contesto

Il significato delle parole è dato dalle parole che spesso appaiono nelle vicinanze (a sinistra e a destra dell'occorrenza della parola).
Usando questi contesti si può creare un vettore denso (definito nel continuo, a valori reali) per ogni parola (non necessariamente grande come il dizionario), costruito in modo che sia simile ai suoi omologhi che compaiono in contesti simili.
Una tecnica per far questo è chiamata _Word2Vec (2013)_, che definisce il contesto tramite una finestra di lunghezza fissata a sinistra e a destra della parola: ad esempio, per finestre di lunghezza 2, si vanno a considerare le due parole prima e le due paole successive. Si salva quindi probabilità per ogni parola della finestra di comparire data la parola target (quella "centrale").
