# Ripasso di Apprendimento Automatico
Un algoritmo di apprendimento automatico è un algoritmo in grado di apprendere come si risolve un problema. Gli ingredienti fondamentali sono: il *task*, la *performance measure* e l'*esperienza*.

### Task
Il task è descritto in termine di come gli esempi dovrebbero essere processati dall'algoritmo di apprendimento. Ogni elemento è descritto da delle feature, caratteristiche che l'algoritmo di apprendimento usa per fare "ingegneria inversa" del problema.

### Performance measure
Misura quanto "buono" è l'algoritmo, ovv ero quanto accurata è l'ipotesi ritornata dall'algoritmo. La ,isura di prestazioni dipende dal task:
- In caso di classificazione, accuracy
- In caso di regressione, MSE (Mean Squared Error) $\frac{1}{N} \sqrt{(t-o)^2}$, dove $o=$ valore predetto e $t=$ valore corretto.

### Experience
In pratica è il dataset, ovvero l'insieme di tutti gli esempi. Ogni esempio è definito da un insieme di feature.

## Ingredienti del ML
Usando i dati di training si cerca una ipotesi dallo *spazio delle ipotesi*. Il modo in cui l'ipotesi viene cercata è data dall'algoritmo di apprendimento, che è l'algoritmo di ricerca nello spazio delle ipotesi. Lo spazio delle ipotesi non può coincidere con l'insieme di tutte le funzioni, altrimenti avremmo un insieme infinito di funzioni uguali (rimembro di computabilità).

E' necessaria quindi un'approssimazione della funzione target, ovvero un *bias induttivo*.

## Paradigmi di apprendimento automatico
- *Supervisionato*: dato un insieme di esempi pre-classificati $Tr = {(x^i, t^i)}, apprendere una descrizione generale che cattura le informazioni contenute negli esempi (ovvero le loro caratteristiche intrinseche)
- *Non supervisionato*, ovvero usare le caratteristiche intrinseche dei dati per raggrupparli in base alle loro somiglianze
- *Con rinforzo*, dove esiste un agente intelligente avente uno stato, che si muove in un mondo e che può compiere azioni. Compiendo un azione, l'agente riceve una ricompensa e un nuovo stato. Lo scopo dell'agente è quello di massimizzare la somma delle ricompense, ovvero la ricompensa finale lungo la sua intera vita.

## Iperpiani in $R^2$
L'insieme $H = \{f_{\vec{w},b}(\vec{x})\}|f_{\vec{w},b}(\vec{x}) = sign(\vec{x}\cdot\vec{w}) + b\}$ rappresenta tutte le dicotomie introdotte dagli iperpiani in $R^2$

## Algoritmo del Perceptron
Algoritmo di apprendimento del 1958. Lo spazio delle ipotesi è quello degli iperpiani in $R^n$. Lo scopo dell'algoritmo è trovare un iperpiano che "divida" correttamente i dati di input in modo corretto (classificazione binaria).

L'algoritmo inizia inizializzando il vettore $w$ dei pesi a 0. Ripete fino a quando tutti gli elementi sono classificati correttamente: pesca un esempio di training ($\vec{x},t$) a caso e, se $o = sign(\vec{w}\cdot\vec{x}) \ne t$ allora aggiorna $\vec{w} = \vec{w} + \eta (t-o)\vec{x}$. 

In pratica ad ogni errore l'iperpiano viene mosso di un pochino (in base al learning rate $\eta$) in direzione dell'errore, in modo da avvicinarsi alla classificazione ottimale. Il *learning rate* regola la velocità di convergenza.

L'algoritmo del perceptron converge solo quando i dati sono linearmente separabili.