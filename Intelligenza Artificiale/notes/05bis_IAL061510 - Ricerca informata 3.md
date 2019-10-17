#Lezione 6 - Ricerca Informata (Cont'd x2)

## Simplified MA*

Questa versione di A\* espande la foglia migliore fino a quando la memoria è piena.

Quando è necessario aggiungere nodi nuovi, scarta dalla coda quelli meno promettenti.

In particolare:

- Viene sempre scartato il nodo foglia peggiore (quello con *f-valore* più alto);
- L'*f-valore* del nodo scartato viene riportato sul nodo padre, un po' come avviene con Best First;
- Si espande il nodo padre di un nodo già scartato solamente quando tutti gli altri cammini sono risultati peggiori.

**Problema**: possono esserci blocchi di foglie con lo stesso *f-valore*. Si rischierebbe di scegliere lo stesso nodo sia per la cancellazione, sia per l'espansione.

Viene quindi adottata una politica di "giovinezza", viene scartato il nodo più vecchio e viene espanso il nodo più recente.

Questo algoritmo è completo solo se la soluzione può essere contenuta in memoria, e risulta ottima solo se la soluzione rimane raggiungibile.



























