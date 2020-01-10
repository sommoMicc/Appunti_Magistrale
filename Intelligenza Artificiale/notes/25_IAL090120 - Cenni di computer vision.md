# Cenni di Computer Vision

09 Gennaio 2019

## Difficoltà della computer vision

L'immagine è una proiezione su un campo 2D di un ambiente 3D. Pertanto, la rappresentazione delle immagini è soggetta a problematiche, quali:

- Rappresentazioni diverse in caso di sorgenti luminose diverse
- Percezione del colore dipendente dall'illuminazione
- Rumore causato dalle ombre
- Gli oggetti rappresentati, a seconda della loro posizione, possono risultare a scale diverse.
- La prospettiva cambia la percezione delle grandezze.
- Stesso oggetto ma punti di vista diversi portano ad avere accesso a parti diverse di esso e magari sotto luce diversa
- Entità uguali possono assumere forme completamente diverse: ad esempio un gatto può assumere pose diverse
- Occlusioni: il cervello umano riesce a compensare le mancanze dell'immagine (dietro il frutto c'è un volto umano).
- Riconoscere elementi all'interno di immagini con pattern complessi risulta problematico
- Oggetti della stessa classe (es.: sedie) possono avere forme e colori completamente diversi, pur servendo alla stessa funzione
- All'opposto, classi diverse potrebbero avere rappresentazioni molto simili: difficile distinguere un pastore tedesco da un lupo.

## Compito della computer vision

Cercare di riprodurre le capacità umane di percezione visiva. Passare dalla rappresentazione di un'immagine al suo significato non è cosa semplice per un computer.

Per rappresentare un'immagine si possono usare:

- Valori binari (immagini bianco e nero): pixel il cui valore è 0 o 1
- Livelli di grigio: pixel a valori interi da 0 (nero) a 255 (bianco)
- Colori: tre valori per ogni pixel (RGB) interi da 0 a 255. Indipendentemente dalla codifica, il computer vede tre immagini/canali diversi

Gli umani hanno la capacità di distinguere la profondità (più che altro di stimarla), grazie alla vista stereoscopica. Inoltre, grazie all'esperienza umana (interazione con il mondo) il modello 3D viene completato

Le informazioni che possiamo estrarre da un'immagine sono:

- Informazioni metriche 3D (dimensioni)
- Informazioni semantiche, ovvero cos'è rappresentata nell'immagine stessa

## Informazioni semantiche

Problema: al di là della difficoltà di distinguere gli elementi, persone diverse danno interpretazioni diverse. Per questo si estraggono dalle immagini informazioni utili ad un determinato compito/contesto/quesito.
