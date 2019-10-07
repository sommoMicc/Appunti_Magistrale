# Lezione 3
Lunedì 7 ottobre 2019

## 5G Architecture
Una caratteristica peculiare del 5G è quella di avere delle metriche ben definite per ciascun servizio supportato. In pratica, la QoS è descritta in modo molto più preciso. 

Ad esempio, è specificato sia il datarate totale sia il numero di utenti per $km^2$. Questo perché, sebbene avere un utente che scarica a 10Gb/s o un milione che richiedono 1Kb/s sia lo stesso a livello di banda totale richiesta, la gestione di connessioni multiple implica un overhead di sistema che deve essere gestito.
Un'altra metrica definita è quella della *connection density*, ovvero il numero di dispositivi che possono essere connessi in un $km^2$. Un'alta connection density può essere gestita con un alto numero di celle a bassa portata (ad esempio una cella ogni $m^2$). 

## OFDM and SC-FDMA
Nell'architettura 5G, OFDM è usata in downlink e SC-FDMA in uplink.
Gli obiettivi di questi tecniche di modulazionie sono:
* Ottenere un alto datarate nelle reti wireless
* Essere flessibili nell'allocazione delle risorse (FDMA è una tecnica che permette l'acesso di un canale a più utenti)
* Avere una soluzione semplice ma molto efficente (soprattuto a livello utente, cioè lato smartphone ad esempio). Tuttavia, anche lato operatore, l'efficenza energetica è un aspetto che andrebbe considerato, soprattutto perché c'è (anzi, ci sarà) la necessità di avere sempre più celle (e quindi sempre più piccole).

### Wideband Channel
Dato un segnale, esso viene diviso in due parti (una reale e una immaginaria). La prima viene modulata (portata dalla frequenza "0" alla frequenza $f_c$, ovvero quella del *carrier*) con seno e l'altra con coseno, in modo da ottenere due segnali ortogonali. 

$$y(t) = \int x(\tau)h(t-\tau)d\tau$$
Il canale cambia nel tempo (??)

$$y(f) = X(f)H(f)$$

In caso di ritarto (delay) di trasmissione, si ha:

$$h(t) = \delta (t-t_0)$$
$$\int x(\tau)h(t-\tau)dt = \int x(\tau) \delta(t-\tau-t_0)d\tau = x(t-t_0)$$
considerando che $\tau = t-t_0$

https://it.wikipedia.org/wiki/Convoluzione




$$z(m) = \sum_{n-\infty}^{+\infty} h(m-n,m)x(n)$$

t (o T forse) = symbol period