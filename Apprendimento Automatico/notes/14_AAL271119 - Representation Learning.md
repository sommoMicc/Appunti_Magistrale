# Representation Learning

27 Novembre 2019

L'apprendimento della rappresentazione è il problema di rappresentare i dati di input, di solito mediante trasformazioni, in modo da permettere che le azioni di classificazioni siano più semplici.

Avere una buona rappresentazione dei dati è un aspetto critico per:

- La performance del classificatore

Cosa rende una rappresentazione buona?:

- La smoothness: se ho due input simili tra di loro, mi aspetto che la funzione predetta sia simile
- Multiple explanatory factors: lo spazio degli input potrebbe dipendere da più fattori, che vanno estratti per rendere efficace la rappresentazione;
- Organizzazione gerarchica dei fattori di spiegazione: concetto simile al deep learning, cioé al tempo t si usano fattori del tempo t-1;
- Sparsità: si cerca di fare in modo che un determinato output dipenda da un sottoinsieme di fattori distinti.

## PCA

Dato un vettore, dare un'altra rappresentazione (esprimere in modo diverso i dati) dei dati, combinazione lineari della rappresentazione originale, che non ho capito un cazzo di niente.

Prima cosa, eliminare tutti i fattori che contaminano i dati stessi:

- Rumore
- Ridondanza: rappresentazioni diverse che offrono in sostanza le stesse informazione. Per calcolare quest'ultimo valore ci si avvale della formula della covarianza:

$$ S_x = \frac{1}{n-1}X\cdot X^T $$
Se ho poca ridondanza la matrice che ottengo sarà simile ad una diagonale: valori alti (tipo 1 penso) sulla diagonale (perché ogni elemento è correlato a se stesso) e valori molto bassi fuori (perché i fattori/parametri/elementi della matrice X sono poco correlati tra di loro). Nota: la divisione per $n-1$ è un fattore di normalizzazione inutile che Aiolli non sapeva spiegare.

## Autoencoders

Soluzione per usare reti neurali in problemi di apprendimento supervised, definendo dei task _fake_.
In pratica sono delle reti neurali che come input prendono la rappresentazione corrente e come output forniscono una rappresentazione alternativa dei dati di input.
Calcoli sembrano formule magiche.
