#Lezione 10 - Giochi non deterministici e ad infomrazioni parziale

##𝜶-𝜷 pruning (best case)

Per avere il valore esatto di uno stato occorre conosce il valore estatto di utilità per uno stato figlio e conosce un bound sull'utilità di tutti gli stati figli rimanenti.

Mentre per derivare un buond sull'utilità di uno stato occorre conoscere il valore esatto di utilità di ogni stato figlio.


- *d*: distanza in ply dagli stati terminali
- *E(d)*: minimo numero di stati da considerare (esplorare) per conoscere il valore esatto di utilità di uno stato ad una distanza *d* play dalla frontiera
- *B(d)*: numero minimo di stati da considerare per conoscere il bound sul valore di utilità di uno stato a distanza *d* ply dalla frontiera.

> E(d+1) = E(d) + (b-1)B(d)
> 
> B(d+1) = E(d)

Espandendo per *E(d+2)*

> E(d+2) = E(d+1) + (b-1)B(d+1)
> 
> E(d+2) = (E(d) + (b-1)B(d)) + (b-1)E(d)
> 
> E(d+2) = bE(d) + (b-1)B(d)
> 
> E(d+2) = bE(d) + (b-1)E(d-1)

Considerando che *E(0) = B(0) = 1* e che *E(d-1) < E(d)*, ottengo che:

> E(d+2) < 2bE(d)

Da cui trovo che generalmente

> E(m) < (2b)<sup>m/2</sup> 

