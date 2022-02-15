#toalettene og gangVedToalletter labels er i samme fil ettersom de begge var veldig små og relaterte. 

label toalettene:
    scene bg vei til toaletter with fade
    pause 2
    scene bg toaletter with fade

    "Her er toalettene. Rett utenfor Spania."

    menu :
        
        "Hva er inngangen til høyre for toalettene?":
            jump gangVedToaletter
        "Tilbake til lobby":
            jump lobby

