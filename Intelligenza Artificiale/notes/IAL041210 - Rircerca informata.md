#Lezione 4 - Rircerca informata e non

Tabella riassuntiva delle proprietà degli algoritmi non informati:

![alt text](./immagini/l4-riassunto.png "Tabella riassuntiva")

## Ricerca non informata - stati ripetuti

Se non si utilizzano delle strategie per evitare di visitare più volte lo stesso stato si possono generare un numero esponenziale di stati.

Possono essere usate alcune strategie per gestire questo problema:

- Si può evitare di generare il nuovo nodo se lo stato del nuovo nodo è ugale allo stato del nodo corrente o di uno dei successori del nodo corrente. La complessità di questa strategia è costante o al più lineare rispetto al numero dei successori del nodo corrente. Se viene trovato due volte lo stesso stato è necessario aggiornare i costi in modo di tenere il nodo migliore. In questo modo non è garantita l'assenza di ripetizioni.
- Si può evitare di generare un nuovo nodo se ha lo stesso stato di uno degli avi (ha lo stesso stato di un nodo presente nel cammino che ha portato al nodo corrente). La complessità questa volta è lineare rispetto alla lunghezza del cammino e non garantisce ancora che lo stesso stato non venga ripetuto, dal momento che lo stesso stato può ancora comparire in due cammini diversi.
- Si può evitare di generare un nuovo nodo se è già stato generato (si può fare con una hash table). La complessità di questa strategia è lineare rispetto al numero totale degli stati, ma garantisce che lo stesso stato non venga incotrato più volte.

### Ricerca su grafo

Al posto di creare un albero con la replica degli stati si va a sostituire l'albero con un grafo dove i nodi rappresentano gli stati e gli archi sono dati dal collegamento dei due stati.

```
function RicercaGrafo(problema,frontiera) returns una soluzione o il fallimento
	chiuso = insieme vuoto //insieme dei nodi già esplorati
	frontiera = Inserisci(CreaNodo(StatoIniziale[problema])),frontiera)
	loop do
		if Vuoto(frontiera) then return fallimento
		nodo = RimuoviPrimo(frontiera)
		if TestObiettivo[problema](Stato[nodo]) then return Soluzione(nodo)
		if Stato[nodo] non è in chiuso then
			aggiungi Stato[nodo] a chiuso
			frontiera = InserisciTutti(Espandi(nodo,problema),frontiera)
	end
```



























