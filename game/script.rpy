# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Johnny")

bool lobby

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg inngang    

    "Du har endelig kommet deg opp til femte etasje."

    "På døren ser du Funkweb logoen"

    "Det er første dagen din på arbeidsforberedene trening, eller AFT for kort."

    "På venstre siden av døren finner du en ringeklokke. Du trykker på den."

    "Her kommer Johnny inn og sier noe som Johnny ville si."
    show Johnny
    j "Heisan! Alltid hyggelig å få nye folk inn i AFT!"
    j "La meg vise deg rundt kjapt."

    jump lobbyBesøkt

    return

label lobby:

    scene bg lobby

    if !lobbyBesøkt:
            "Du går inn døren til et rom med sofaer og mange dører."
        j "Ta å desinfiser hendene dine før vi går videre."
        "Du tar tiden til å desinfiserre deg. Best å være sikker."

        j "Dette er lobbyen"
        j "Her finner du møterom (møterom navn her) og toaletter"
        "Alltid godt å vite hvor toalettene er"
    
    if lobbyBesøkt:
        "Tilbake til lobbyen, hvor vil du besøke neste?"



label kantine:
        
    scene bg kantine

    "Kantina ser ut som en kanskje vanlig kontor kantine ved første blikk egentlig."
    "Når du ser deg litt rundt så ser du en del kjøleskap og kanskje noen pakker."
    j "I kjølekapet lengst til venstre fra døren kan du legge mat du har med deg."
    j "Vanlig lunsj tid for kontoret er 11:30 til 12:00, men ikke føl et press for å spise her."

label klasserom:

    "Forran deg er et stort rom med datamaskiner på rekke og rad"
    j "Dette rommet har veldig enkle chromebooks."
    j "Hvis du skal hovedsakelig skrive CV, søknader og kanskje ta noen online kurs kommer du til å sitte her."
    ""

label datarom:

    
    
    

