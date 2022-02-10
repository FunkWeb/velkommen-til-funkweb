
label lobby:

    scene bg lobby with fade

    if not lobbyBesokt:
        "Du går inn døren til et område med sofaer og fler dører."
        show johnny at right

        j "Ta å desinfiser hendene dine før vi går videre."
        scene bg antibac
        "Til venstre for døren ser du midler for å desinfisere hender og munnbind hvis du trenger det. Du kan også henge fra deg jakker her."
        scene bg lobby
        show johnny at right
        j "Dette er lobbyen."
        j "Her finner du møterommene Spania, Zambia og Kenya."
        j "Toalettene finner du også her."
        "Alltid godt å vite hvor toalettene er."
    
    else:
        show johnny at left
        "Da er vi tilbake til lobbyen, hvor vil du besøke neste?"
    
    $ lobbyBesokt = True

    show screen lobbyScreen

    menu lobby_menu:
        "Gå til venstre mot kantina":
            hide screen lobbyScreen
            jump kantine
        "Gå til høyre mot datarommene":
            hide screen lobbyScreen
            scene bg gang tilaft with fade 
            pause 2.0
            jump aftGangen
        "Hvor er toalettene?":
            hide screen lobbyScreen
            jump toalettene
        "Ferdig for dagen":
            hide screen lobbyScreen
            j "Ha en fin dag!"
            scene bg svart with fade
            pause 2.0
            return
