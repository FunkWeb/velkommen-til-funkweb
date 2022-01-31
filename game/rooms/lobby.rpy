
label lobby:

    scene bg lobby with ease

    if not lobbyBesokt:
        "Du går inn døren til et område med sofaer og fler dører."
        show johnny at right

        j "Ta å desinfiser hendene dine før vi går videre."
        scene bg antibac
        "Til venstre for døren ser du midler for å desinfisere hender og munnbind hvis du trenger det. Du kan også henge fra deg jakker her."
        scene bg lobby
        show screen lobbyScreen
        show johnny at right
        j "Dette er lobbyen."
        j "Her finner du møterom (møterom navn her) og toaletter."
        "Alltid godt å vite hvor toalettene er."
    
    else:
        show screen lobbyScreen
        show johnny at left
        "Da er vi tilbake til lobbyen, hvor vil du besøke neste?"
    
    $ lobbyBesokt = True

    menu lobby_menu:
        "Gå til kantinen":
            hide screen lobbyScreen
            jump kantine
        "Gå til datarom, klasserom og bibliotek":
            hide screen lobbyScreen
            scene bg gang tilaft with fade 
            pause 3.0
            jump aftGangen
        "Hvor er toalettene?":
            hide screen lobbyScreen
            jump toalettene
        "Ferdig for dagen":
            return
