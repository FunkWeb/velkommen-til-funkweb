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
        "Datarom":
            jump datarom
        "Klasserom":
            jump klasserom
        "Tilbake til lobby":
            jump lobby
        