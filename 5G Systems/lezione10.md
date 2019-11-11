# Synchronization for Multicarriier Systems
Lunedì 4 Novembre 2019

Sincronizzazione indica la regolazione di tempo e frequenza da parte del ricevente in modo che sia coerente con il trasmittente. Esso infatti deve sapere quando la trasmissione avverrà e quando sarà ricevuto il simbolo corretto.

Prima che avvenga la sincronizzazione non si possono fare assunzioni sul canale.

Con OFDM il problema della sincronizzazione trascende dall' "esatto momento in cui campionare il segnale". In OFDM la sincronizzazione è importante quando si fa la DFT. Distinguiamo 4 casi:
1. Perfetta sincronizzazione: inizio a fare la DFT appena finita la ricezione del cyclic prefix. In questo caso la DFT restituirà i valori esatti input dell'IDFT lato trasmittente
2. Leggero anticipo: inizio a fare la DFT poco prima che la riceziione del Cyclic Prefix (CP) finisca, ma tardi abbastanza da non ricevere la parte di cyclic prefix "influenzata" dal blocco precedente. A livello di performance, non succede niente!!
3. Inizio la DFT talmente in anticipo che viene considerato il pezzo di CP influenzato dal blocco precedente.
4. Inizio la DFT in ritardo in modo da "prendere dentro" anche il CP del blocco successivo.

Nei casi 3 e 4 si avrà dell'inter-block e inter-channel interference. La DFT infatti restituirà un blocco i cui simboli iniziali (o finali) sono quelli del blocco precedente o successivo (in base al caso 3 o 4), quindi il cyclic prefix "non funziona" (non avviene la magia). Siccome il cyclic prefix è "rotto", si capteranno anche simboli trasmessi in sottoportanti differenti (inter-channel interference).

Affinché avvenga una corretta sincronizzazione, si deve ambire ad essere nel caso 2. Il caso 1 (sincronizzazione perfetta) è troppo fragile. Essendo nel caso 2, se inizio la DFT un po' prima od un po' dopo non cambia (tolleranza). Per farlo:
- Usare un cyclic prefix più lungo della lunghezza minima, in modo da creare una "confort zone" che tolleri meglio le desincronizzazioni.
- Cercare di iniziare la DFT nel mezzo tra $\Tau_g$ e $\tau_{max}$, in modo da tollerare allo stesso modo anticipo e ritardo.


## Samplinig Clock Frequency Offset
La frequenza di campionamento lato ricevente è sfasata rispetto quella con cui i simboli vengono trasmessi. Il clock tra il trasmittente e il ricevente è quindi sbagliato. ll risultato è uno shift (rotazione) progressiva della fase, che appunto si accumula nel tempo.
Si risolve skippando qualche simbolo ogni tanto.

## Carrier (Clock) Frequency Offset
Questo sfasamento avviene quando trasmittente e ricevente sono allineati su due frequenze differenti. Questo può essere dovuto alle differenze tra gli oscillatori e/o all'effetto Doppler (__Doppler Shift__), cioè lo spostamento del segnale nel dominio delle frequenze.
L'impatto dell frequency offset dipende da quanto sono spaziate le sottoportanti ($\Delta f$):

$$ \epsilon = \frac{f_{offset}}{\Delta f}$$

Si possono fare delle distinzioni basate sul valore di $\epsilon$:
- Se è intero, la frequenza in cui siamo caduti è semplicemente quella di un'altra sottoportante
- Per la parte frazionaria, cioè $|\epsilon|<1$, ci sono un sacco di calcoli. In pratica, alla fine si ottiene della inter-carrier interference.