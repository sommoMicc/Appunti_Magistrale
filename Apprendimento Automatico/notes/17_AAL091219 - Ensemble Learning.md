# Ensemble Learning
L'idea è prendere delle predizioni/classificazioni da più modelli e poi aggregarle. Quindi, un classificatore **ensemble** è un insieme di classificatori base.

L'esempio della mucca ci racconta come, sebbene le persone andavano tendenzialmente lontano dall'indovinare l'esatto peso della mucca, la media delle predizioni era terribilmente simile al valore corretto.

## Why parallel ensemble should work?

L'esponente di $e^{-\frac T 2 (2\epsilon-1)^2}$ tende velocemente a $-\infty$, quindi l'espressione tende velocemente a 0. Il problema è che i predittori di per sé non sono indipendenti (fai apprendimento sempre sullo stesso insieme di dati, e ), quindi in realtà si raggiunge un _plateau_ e si deve puntare a **minimizzare l'indipendenza** tra i predittori.

## Bootstrapping
Una possibilità è quella di usare lo stesso algoritmo ma allenato su insiemi diversi di dati. Quindi, dato il training set si fa un sampling con replacement, permettendo di estrarre anche lo stesso esempio più volte e ottenendo quindi più sottoinsieme. Questi poi vengono dati in pasto a diversi classificatori, che quindi si spera diano una tipologia di errore diversa tra i vari predittori.

Un'altra possibilità è chiamata **feature randomization**, ovvero allenare predittori diversi su un sottoinsieme di feature differenti.

L'algoritmo più importante è chiamato **Bagging**. L'idea è semplice:

* Creare _k_ insiemi di boostrap;
* Allenare un classificatore diverso per ognuno dei _k_ insiemi;
* Fare l'ensemble dei modelli.

Questo funziona perché:

1. Mediare più classificatori riduce la varianza;
2. Anche nel caso in cui le singole ipotesi non siano tra loro troppo indipendenti, l'effetto è la continua riduzione della varianza ma un contemporaneo incremento del bias. Se vengono usati modelli con bias più piccolo, in teoria il _bagging_ permette di mantenere il bias piccolo e la varianza bassa.

Il metodo è stato applicato per la prima volta sui _decision tree_. Il bagging funziona male se i modelli sono stabili, ovvero se cambiano poco dopo pochi dati di training.

## Boosting

Si cerca di ottenere nuove ipotesi "deboli" usando sottoinsieme di dati (o feature) come con il _Bagging_ ma dando dei pesi diversi ai vari _weak predictor_. In particolare:

1. Dal training set estrapolare un predittore debole;
2. Ripesare gli esempi di training, mettendo più peso su gli esempi che sono stati classificati male nel predittore precedente. In pratica, si possono assegnare priorità di estrazione più elevate agli esempi a cui si vuole dare più peso, oppure far valere di più gli errori relativi agli esempi con il peso più alto;
3. Ripetere il tutto _n_ volte;
4. Combinare le ipotesi semplici in un'unica più accurata.

Il boosting funziona se __per ogni possibile sottoinsieme dei dati__ i classificatori deboli definiti sono migliori del _random guessing_ (lancio della moneta) di un $\epsilon$, ovvero $accuracy > 0.5 + \epsilon$ (o, in altre parole, $error \le 0.5 - \epsilon$).

L'_AdaBoost_ è l'algoritmo di classificazione binaria boosting che andiamo ad analizzare. La sua ipotesi è:

$$
H(x) = sign(\sum_t \alpha_t h_t(x))
$$

Ad ogni iterazione, l'obiettivo del week learner è quello di massimizzare l'accuracy pesata, ovvero minimizzare l'errore pesato $\epsilon_t = P_{i \sim D_t}(h_t(x) \ne y_i])$, dove $\sim$ indica che i è estratto dall'insieme $D_t$.

Si può dimostrare che la funzione che andiamo effettivamente ad ottimizzare è la funzione loss: $E = \sum_{i=1}^n e^{-y_i H(x_i)}$, che prima o poi va a 0.

Da esperimenti fatti utilizzando AdaBoost, il training error va velocemente a 0, ma la cosa sorprendente è che anche il test error, anche quando il training error è già a 0, tende a diminuire!.

Da un certo punto di vista, _bagging_ e _boosting_ sono complementari. _Bagging_ va usato su predittori singoli a piccolo bias. Viceversa, per il _boosting_ bisogna cercare di concentrarsi su ipotesi deboli con alto bias (tipo _decision stamp_) ma bassa varianza.

## Stacking

?

