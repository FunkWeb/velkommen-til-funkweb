#toalettene og gangVedToalletter labels er i samme fil ettersom de begge var veldig små og relaterte. 

label toalettene:
    scene bg toaletter with fade

    "Godt å vite hvor toalettene er."

    menu :
        
        "Hva er inngangen til høyre for toalettene?":
            jump gangVedToaletter
        "Tilbake til lobby":
            jump lobby

label gangVedToaletter:

    scene bg gang spania with fade

    "Her finner du grupperom Spania og (Blank)"

    menu :
        "Tilbake til lobby":
            jump lobby