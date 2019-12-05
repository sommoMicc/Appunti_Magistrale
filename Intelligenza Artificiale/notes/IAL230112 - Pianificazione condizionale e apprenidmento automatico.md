#Lezione 23 - Pianficiazione condizionale e cenni di Apprendimento automatico

Per vari motivi può esserci un **fallimento**, cioè le precondizioni del resto del piano non sono più soddisfatte, ad esempio a causa delle azioni di un altro agente.
L'agente quindi arriva in un punto in cui il resto del piano non può essere eseguito.

È quindi necessario andare a monitare costantemente lo stato dell'ambienete e nel caso di fallimento riprendere l'algoritmo POP a partire dallo stato corrente.

##IPEM - Integrate Plannin Execution e Monitoring

Viene aggiornato continuamente lo stato _Start_ man mano che vengono eseguite le azioni, in questo modo si tiene traccia dei cambiamenti subiti dal mondo.

Quandi l'algoritmo si accorge che dallo stato corrente non riesce ad andare avanti perché ci sono delle condizioni non valide e quindi ripianifica a partire dallo stato corrente.

Questo comportamento cicla fino al successo ed _emerge_ dalla interazione tra agente del tipo monitorizza/ripianfica e ambiente non cooperativo.

Ad esempio l'ambiente può invalidare alcune delle precondizioni più volte, in questo caso l'agente deve controllare di non ciclare all'infinito.
