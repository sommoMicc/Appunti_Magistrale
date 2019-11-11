# Lezione 14 - Funzioni Kernel 


##Tipologie di Kernel

Per **vettori** si possono utilizzare come kernel:

- **lineare**: *k(x,z) = x \* z*
- **polinomiale**: _k(x,z) = (x * z + c)<sup>d</sup>_
- **gaussiano** (RBF): _k(x,z) = exp(-𝜸||x-z||<sup>2</sup>)_, ha la caratteristica di essere sempre compreso tra 0 e 1.

Il fatto che il kernel sia sempre maggiore di 0, implica che i due vettori sono nello stesso ottante (tra i due vettori c'è un angolo minore di 90°).

Se *k(x,x)* è uguale a 1 si dice che il kernel è **normalizzato**, ovvero tutti i vettori del feature space sono normalizzati. La matrice kernel definita con un kernel normalizzato ha tutti 1 nella diagonale.

È sempre possibile normalizzare un kernel *k(x,z)* dividendolo per la radice quandrata di _k(x,x) * k(z,z)_

Come kernel per le **stringhe** si possono contare tutte le sequenze di una cerca lunghezza e costruire un vettore delle feature delle occorrenze, questo si fa con le tecniche di programmazione dinamica.

Per gli alberi si possono utilizzare delle tecniche analoghe, considerando i sotto alberi in comune.

C'è un libro **Kernel Methods for Pattern Analysis** che spiega molto bene questa tecnica.

##Operazioni sui Kernel

Una combinazione lineare positiva di kernel è anchessa un kernel, quindi

> k(x,z) = ak_1(x,z) + bk_2(x,z)

Se quna sequenza di kernel converge puntualmente ad una funzione *f*, allora anche *f* è un kernel.

Ma c'è di più, i kernel possono essere tra loro composti per ottenere altri kernel.

Tutto questo si può andare a combinare per ottenere un kernel migliore.
Dato un insieme *S* di kernel si può definire

> k(x,z) = Sommatoria_[S=1,Q]μ_sk_s(x,z)

Dove μ è un vettore tale che la loro sommatoria sia 1.

L'idea del Multiple Kernel Learning è di definire degli algoritmi per apprendere i valori di μ_s della combinazione che migliorino le prestazione di una SVM usando il kernel combinato, rispetto alle SVM ottenute utilizzando i kernel individuali.

