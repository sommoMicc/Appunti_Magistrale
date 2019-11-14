def prova(obbligatorio, *argomenti, **tanti):
    (primo, secondo) = argomenti
    print(f"Primo: {primo}; Secondo: {secondo}")
    print(f"Tanto: {tanti['si']}")



prova("ciao", "asd", "come", si="Pintus")