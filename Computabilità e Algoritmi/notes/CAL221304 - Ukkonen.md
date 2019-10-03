## Miglioramento dell'efficienza - Suffix link

Sia alfa una stringa e *x* un carattere.

Se in un albero dei suffissi esiste un nodo interno esplicito *u* con etichetta *xalpha* ed un nodo interno esplicito *s(u)* la cui etichetta è alpha, allora un **suffix link** tra *u* e *s(u)* è un puntantore che collega i due nodi.

![In questo caso alpha=a e x=d](./immagini/l22-fig1.png)

Così facendo durante la costruzione dell'albero, quando viene esteso il cammino ad una foglia, posso tornare indietro fino a che non trovo un nodo esplicito con un suffix link e posso riprendere la costruzione dell'albero a partire dal nodo collegato.

Però al momento non c'è la garanzia che da ogni nodo interno esplicito esca un suffix link.

### Lemma 5.4 - Esitenza del suffix link

Se, durante la fase *i*-esima, per estendere il suffisso *S[j,1]*, viene crato un nuovo nodo interno con etichetta *xalpha*, con *xalpha* prefisso di *S[j,i]*, allora o nell'albero esiste già un nodo splicito con etichetta *alpha* oppure tale nodo verrà creato estendeno il sufffisso successivo *S[j+1,i]*.

#### Dimostrazione

L'unico caso in cui viene creato un nodo interno *v* con etichetta *S[j,i] = xalpha* viene creato solo se il suffisso *S[j,i]* viene esteso con il caso 2.

```
quando nell’albero corrente il cammino etichettato S[j,i] termina in un nodo interno implicito e tale cammino continua con un carattere c diverso da S[i+1].
Quindi, nell’albero corrente, il cammino di etichetta S[j+1, i] = alpha ha una continuazione che inizia con il carattere c.
```

Questo perché entrambi i suffissi, terminando in nodi interni, sono prefissi di suffissi più lunghi.


...

### Costruzione dell'albero con i suffix link

### Skip/count