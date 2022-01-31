label aftGangen:
    menu aft_meny:
        "Det er to steder du kan besøke på vei til datarommene."
        "AFT kontor dør - Venstre":
            jump aft
        "Kjøkken - Høyre":
            jump gangKjokken
        "Gå videre - Fremover":
            jump velgDatarom
           

label velgDatarom:
    scene bg gang tildatarom with fade
    pause 3        
    scene bg gang dataromdør with fade
    jump velg
    menu velg:
        "Hva vil du se først?"
        "Klasserom - Venstre":
            jump klasserom
        "Datarom - Fremover":
            jump datarom
        "Bibliotek - Høyre":
            jump bibliotek
        "Tilbake til lobby":
            jump lobby
        