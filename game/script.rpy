image johnny = im.Scale("johnny.png",480,900)
image anders = im.Scale("anders.png",480,900)
image ingeborg = im.Scale("ingeborg.png",480,900)
image reidar = im.Scale("reidar.png",480,900)

define j = Character("Johnny")
define a = Character("Anders")
define i = Character("Ingeborg")
define r = Character("Reidar")

default lobbyBesokt = False

label start:

    scene bg inngang    

    "Du har endelig kommet deg opp til femte etasje."

    "På døren ser du Funkweb logoen"

    "Det er første dagen din på arbeidsforberedene trening, eller AFT for kort."

    "På venstre siden av døren finner du en ringeklokke. Du trykker på den."

    "Her kommer Johnny inn og sier noe som Johnny ville si."
    show johnny at left with fade
    j "Heisan! Alltid hyggelig å få nye folk inn i AFT!"
    j "La meg vise deg rundt kjapt."

    jump lobby

label lobby:

    scene bg lobby

    if not lobbyBesokt:
        "Du går inn døren til et rom med sofaer og mange dører."
        show johnny at left
        j "Ta å desinfiser hendene dine før vi går videre."
        "Du tar tiden til å desinfiserre deg. Best å være sikker."

        j "Dette er lobbyen"
        j "Her finner du møterom (møterom navn her) og toaletter"
        "Alltid godt å vite hvor toalettene er"
    
    else:
        show johnny at left
        "Tilbake til lobbyen, hvor vil du besøke neste?"
    
    $ lobbyBesokt = True

    menu:
        "Gå til kantinen":
            jump kantine
        "Gå til klasserommet":
            jump klasserom
        "Gå til datarom":
            jump datarom
        "Ferdig for dagen":
            return

label kantine:
        
    scene bg kantine

    "Kantina ser ut som en ganske vanlig kontor kantine ved første blikk."
    "Når du ser deg litt rundt så ser du en del kjøleskap og kanskje noen pakker."
    show anders at left
    a "I kjølekapet lengst til venstre fra døren kan du legge mat du har med deg."
    a "Vanlig lunsj tid for kontoret er 11:30 til 12:00, men ikke føl et press for å spise her."

    menu:
        "Gå tilbake til lobby":
            jump lobby 

label klasserom:

    scene bg klasserom
    show ingeborg at right 

    "Forran deg er et stort rom med datamaskiner på rekke og rad"
    i "Dette rommet har veldig enkle chromebooks."
    i "Hvis du skal hovedsakelig skrive CV, søknader og kanskje ta noen online kurs kommer du til å sitte her."

    menu:
        "Gå tilbake til lobby":
            jump lobby

label datarom:
    scene bg datarom
    show reidar at left

    r "Her har du datarommet"
    r "Dette er rommet hvor AFT-deltakerene sitter og jobber med prosjekter"
    menu:
        "Gå tilbake til lobby":
            jump lobby

    
    
    

