# SC-FDMA
Giovedì 24 Ottobre 2019

Siccome se client e base station sono desincronizzati si verifica inter-carrier interfearence, in upload (client -> base station) esiste una tecnica chiamata "__time advance__" che consiste nella trasmissione anticipata da parte del client, in modo tale da dare alla base station il "tempo" di ascoltare.

## Resurce allocation SC-FDMA
In download si aveva solo una constraint (potenza totale di cui la stazione base può disporre per la trasmissione), mentre in uplink c'è una power constraint per utente. 
Quindi, siccome ogni utente ha una propria power-constraint e ha un numero di sottportanti allocate, per risolvere il problema ogni utente deve applicare l'algoritmo del waterfiling. Ovviamente, l'importante è che una sottoportante non sia allocata a più di un utente, altrimenti si verificano interferenze (capitan ovvio, gelato banana).
Infine, come per il download, la resource allocation non è standardizzata: non definisce come la stazione base o l'utente finale può risolvere il problema dell'allocazione.