label aftGangen:
    menu aft_meny:
        j "Det er to steder du kan besøke på vei til datarommene."
        "AFT kontor dør - Venstre":
            jump aft
        "Kjøkken - Høyre":
            jump gangKjokken
        "Gå videre - Fremover":
            jump velgDatarom
           

label velgDatarom:
    if not forbiDataromGang:
       scene bg gang tildatarom with fade
       pause 2        
    scene bg gang dataromdør with fade
    jump velg
    menu velg:
        "Hvilke rom vil du se?"
        "Klasserom - Venstre":
            $ forbiDataromGang = True
            jump klasserom
        "Prosjektrom - Fremover":
            $ forbiDataromGang = True
            jump datarom
        "Bibliotek - Høyre":
            $ forbiDataromGang = True
            jump bibliotek
        "Gå tilbake til resepsjonen":
            $ forbiDataromGang = False
            jump lobby
        