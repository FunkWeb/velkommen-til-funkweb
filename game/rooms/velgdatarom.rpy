label velgDatarom:
    menu aft_meny:
        "Det er to steder du kan besøke på vei til datarommene."
        "AFT kontor dør":
            jump aft
        "Kjøkken":
            jump gangKjokken
        "Gå videre":
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
        "Tilbake til lobbyen":
            jump lobby
        