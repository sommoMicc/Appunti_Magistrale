# Introduzione
Intelligenza artificiale, machine learning, neural network e Deep Learning sono dal generale allo specifico.
Le reti neurali sono un argomento "vecchio", ma recentemente sono state "riscoperte" grazie al Deep Learning: reti neurali profonde, con un elevato numero di livelli nascosti.

## Machine Learning
La definizione rispecchia l'idea di apprendimento "umano": l'esperienza è quella che apprendiamo, la "performance measure" è il modo che abbiamo per capire se le nostre azioni sono "buone" o "deleterie".

Esempi:
- Giocatore di scacchi
- Riconoscimento di immagini:
    - $P = $ percentuale di immagini classificate correttamente
    - $T = $ riconoscere le cifre manoscritte
- Self-driving car: esempio di apprendimento supervisionato. In pratica la macchina viene guidata e le azioni compiute dal guidatore reale vengono registrate ed entrano a far parte dell'esperienza.
- Object Detection

## Why Deep Learning
L'inizio dell'adorazione per il deep learning avviene nel 2012. In pratica ogni anno c'è una "challenge" il cui task è quello di classificare delle immagini (in 1000 classi). Nel 2012 appunto, per la prima volta, viene utilizzato un classificatore basato su reti neurali deep (anche se non tanto deep, 8 *hidden layers*). Ovviamente, anche prima del 2012, ogni anno gli approcci "vincenti" miglioravano le performance dei precedenti, ma di poco (2/3%). Nel 2012, grazie al deep learning, si passa dal 26% di errore al 16%. Nel 2015 si è riusciti ad arrivare a 3.5% dell'errore, che è al di sotto del 5% di errore umano. Siccome le etichette sono assegnate dagli umani, il task è da ritenersi "completato".


## Linear Algebra Basics
### Hyperplanes
La base dell'algebra lineare è la definizione di *Iperpiano* in $R^n$, ovvero un insieme di punti che soddisfano la seguente equazione: $w_1 \cdot x_1 + w_2 \cdot x_2 + ... + w_n \cdot x_n$

Se $\vec{w} = [w_1 w_2]$, $\vec{x} = [x_1 x_2]$, allora possiamo scrivere l'equazione dell'iperpiano come $\vec{w}^T \cdot \vec{x} = b$. Per ogni punto $x_p$  nell'iperpiano vale $w_1\cdot x_{p1} + w_2 \cdot x_{p2}+ .. + w_n \cdot x_{pn} - b = 0$

### Matrices
Sia $A \in R^{n \times n}$ una matrice. Definisco $(A^T)_{i,j} = A_{j,i}$, ovvero l'elemento in posizione $(i,j)$ della matrice trasposta è quello in posizione $(j,i)$ della matrice originale.

#### Prodotto riga per colonna
Il prodotto tra due matrici, es: $C = A B, A \in R^{x\times n}, B \in R^{n \times q}$ (quando non c'è operatore ci si riferisce al prodotto riga per colonna), è una matrice di dimensione $n \times n$ i le cui celle sono formate da:

$$
C_{1,1} = a_{1,1} + b_{1,1} + a_{1,2} + b_{2,1} + ..
$$
Ovvero la somma degli elementi di una riga di $A$ con i corrispondenti elementi di una colonna di $B$:

$$
C_{i,j} = \sum_k A_{i,k} \cdot B_{k,j}
$$

Il prodotto riga per colonna gode delle seguenti proprieta:
- **Distributiva**: $A(B+C) = AB + AC$
- **Associativa**: $A(BC) = (AB)C$
- **Trasposta**: $(AB)^T = B^T A^T$
- Non gode invece della proprietà commutativa, cioè $AB \ne BA$

#### Prodotto di Hadamard
Un altro tipo di prodotto è quello di Hadamard: $A \circ B = C$, dove $\forall i,j, c_{i,j} = a_{i,j} \cdot b_{i,j}$.

L'equivalente del prodotto di hadamard sui vettori è il **dot product**, denotato come $<x,y>$ o $x^Ty$ (se $x$ e $y$ sono vettori) $= x_1 \cdot y_1 + x_2 \cdot y_2 + .. + x_n \cdot y_n$

#### Sistemi di equazioni lineari
Molto spesso sono scritti nella forma $A \vec{x} = \vec{b}$.
Per risolvere un sistema lineare è necessaria la nozione di matrice inversa:

$A^{-1} A = I_n$, dove $I_n$ è la matrice di identità di dimensione $n \times n$

Nel contesto dei sistemi lineari, posso usare l'inversa per calcolare i valori di $x$:

$$
A\vec{x} = \vec{b}\\
A^{-1}A\vec{x} = A^{-1}\vec{b}\\
I_n \vec{x} = A^{-1}\vec{b}\\
\vec{x} = A^{-1}\vec{b}
$$

#### Norma
Dato $x$ un vettore, la sua norma è:
$L^p = ||{\vec{x}}||_p = \sqrt[p]{\sum_i |x_i|^p}$. $L^2$ è chiamata *norma euclidea*.

Se A è una matrice, la sua norma di *Frobenius* è definita come:
$||A||_f = \sqrt{\sum_{i,j} A_{i,j}^2}$

Il *dot product* tra due vettori può essere definito rispetto alla norma euclidea:

$$
\vec{x}^T \vec{y} = ||\vec{x}||_2 \cdot ||\vec{y}||_2 \cdot cos(\theta)
$$

#### Vettori e matrici speciali
- Matrice diagonale, con tutti zeri tranne che valori nella diagonale. Può essere riscritta come un vettore, i cui elementi sono i valori nella diagonale corrispondente $diag(\vec{v})$
- Vettori unitari, ovvero aventi norma euclidea $||\vec{x}||_2 = 1$
- Vettori ortogonali $\vec{x}^T\vec{y} = 0$
- Vettori ortonormali, ovvero vettori ortogonali di norma 1
- Matrici ortogonali: $A^TA = AA^T = I \implies A^{-1} = A^T$

#### Decomposizione in autovettori
Gli autovalori di una matrice quadrata sono tutti quei $\vec{v}$ tali che:
$A\vec{v} = \lambda \vec{v}$, dove $\lambda$ è un autovalore

$A = V diag(\vec{\lambda}) V^{-1}$

#### Decomposizione in valori singolari (singular value decomposition)
Definita per tutte le matrici

$A = U D V^T$, con $D$ diagonale, $U$ e $V$ ortogonali. 

#### Pseudo-inversa di Moore Penrose
Si prendono solo gli elementi della diagonale