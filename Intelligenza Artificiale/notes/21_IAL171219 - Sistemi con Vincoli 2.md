# Lezione 21 - Sistemi con vincoli parte 2

> nota: ho saltato la lezione precedente e non capisco un cazzo. Ma dovrebbe esserci tutto sul libro!!

## Struttura dei sottoproblemi

Se riesco a suddividere il problema in diversi sottoproblemi, la complessità diminuisce a lineare (da esponenziale).

## CSP con struttura ad albero

Rappresentando i vincoli come un grafo, se quello che otteniamo è aciclico, la complessità scende a $O(n\cdot d^2)$

L'algoritmo di creazione dell'albero (è non radicato, quindi non ha una radice!) è molto semplice:

1. Si sceglie una variabile come radice
2. Si ordinano le variabili dalla radice alle foglie in ordine topologico (ogni nodo è preceduto dal suo genitore): in pratica si scrivono i nodi a mo di lista rispettando l'ordine topologico

## Algoritmi iterativi per CSP

L'obiettivo del sistema con vincoli è trovare dei valori delle variabili per cui i vincoli sono soddisfatti: non ci interessa quindi il cammino ma solo lo stato "goal" (ovvero l'assegnazione che soddisfa i vincoli del sistema).

Il problema dell'Hill-Climbing e del Simulated Annealing è che lavorano con stati completi, ovvero con tutte le variabili assegnate. Di fatto, per applicare questi algoritmi, dobbiamo cercare degli assegnamenti che non soddisfano i vincoli e provare a migliorarli.

Più formalmente:

- La variabile da migliorare è selezionata a caso tra una delle variabili in conflitto;
- L'euristica che andiamo a considerare è il numero minimo dei vincoli violati, ovvero usa $h(n)$ = numero minimo di vincoli violati.

Problemi:

- La ricerca locale (come Hill Climbing e Simulated Anealing) è soggetta ai minimi locali. Quando il problema è particolarmente complesso, però, ci possiamo accontentare di minimi locali (quindi un'approssimazione della soluzione).

## Esempio delle 4 regine

Nel caso delle 4 regine, esse vengono mosse solo per riga (rimangono nelle stesse colonne) perché inizialmente sono già disposte una per colonna. Ecco che si muove la regina nella cui colonna c'è il valore minore di $h$.

In questo caso ci accorgiamo se il minimo in cui siamo è locale o globale in base al numero di vincoli violati: se anche solo un vincolo è violato, siamo in un minimo locale! E' possibile applicare qualche tecnica di restart per migliorare le prestazioni => in problemi complessi è molto usata la ricerca locale.

Si è visto che i problemi difficili sono quelli che hanno né pochi né troppi vincoli ($R = \frac{Numero\, di\, vincoli}{Numero\, di\, variabili}$): con pochi vincoli ci sono tante soluzioni, mentre se il sistema ha tanti vincoli la ricerca con backtracking fallisce rapidamente (quindi capsce rapdamente che il problema non ha soluzione).
