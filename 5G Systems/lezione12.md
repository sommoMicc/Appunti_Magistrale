# MIMO 3 (2 l'ho saltata per compitino IA)

25 Novembre 2019

## Spatial Multiplexing

In ogni antenna viene trasmesso un simbolo. Le interferenze presenti lato ricevente sono:

$$ y = Hx + w $$

I calcoli sono complicati perché H non è sempre quadrata, in quanto si possono utilizzare un numero di antenne lato trasmittente diverso da quello ricevente. Si usano quindi delle "pseudo-inverse".
Siccome l'equazione sopra è in fin dei conti un sistema, non si possono avere meno antenne lato ricevente che antenne lato trasmittente. Questo perché bisogna avere più (o lo stesso numero) equazioni che variabili, e il numero di equazioni è dettato dall'altezza di H, ovvero il numero di antenne riceventi.
Con lo **Zero-Forcing Receiver**, facendo tutte quelle inverse per cercare di eliminare completamente le interferenze, si rischia di aumentare il rumore. Al contrario, con **Minimum-Mean Square Error**, si accettano delle interferenze, ma $W \cdot w$ avrà meno potenza, quindi cii sarà meno influenza del rumore.

Siccome l'assunzione è che per ogni antenna vengono trasmessi dati **indipendenti**
