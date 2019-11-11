# Lezione 14 - Funzioni Kernel 


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

