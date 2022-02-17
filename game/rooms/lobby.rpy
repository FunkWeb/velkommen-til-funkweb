
label lobby:

    scene bg lobby with fade

    if not lobbyBesokt:
        "Du går inn i et resepsjonsområde med flere sofaer."
        show johnny at right

        scene bg lobby
        show johnny at right
        j "Dette er resepsjonen. Her kan folk vente på møter, eller bare sitte å slappe av."
        j "Her finner du møterommene Spania, Zambia og Kenya."
        j "Toalettene finner du også her innerst til venstre."

    
    else:
        show johnny at left
        "Da er vi tilbake i resepsjonen. Hvor vil du gå nå?"
    
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
        "Fortell meg om møterommene":
            hide screen lobbyScreen
            j "Vi har åtte møterom som kan reserveres gjennom Google Kalender."
            j "De fleste av disse har vi gitt navn av forskjellige nasjoner."
            j "Hvilket møterom er du interessert i å høre mer om?"
            
        "Ferdig for dagen":
            hide screen lobbyScreen
            j "Ha en fin dag!"
            scene bg svart with fade
            pause 2.0
            return

    menu møterom_menu:
        "Spania":
            j "Spania er lengst til venstre i resepsjonen, ved siden av toalettene. Der er det fire sitteplasser."
            jump møterom_menu
        "Zimbabwe":
            j "Zimbabwe er det midterste møterommet i resepsjonen, mellom Spania og Kenya. Det er det fire sitteplasser."
            jump møterom_menu
        "Kenya":
            j "Kenya er lengst til høyre i resepsjonen, og er nærmest TV-skjermen. Der er det fire sitteplasser."
            jump møterom_menu
        "Brazil":
            j "Ingangen til Brazil finner du innerst i kantinen, ved siden av vinduene. Det har plass til tre stykker."
            jump møterom_menu
        "Thailand":
            j "Thailand er møterommet rett utenfor kantinen. Der er det fire sitteplasser."
            jump møterom_menu
        "Tibet":
            j "Tibet er det andre møterommet i gangen utenfor kantinen. Der er det fire sitteplasser."
            jump møterom_menu
        "Kina":
            j "Kina er det tredje møterommet i gangen utenfor kantinen. Der er det fire sitteplasser."
            jump møterom_menu
        "Biblioteket":
            j "Biblioteket er det største møterommet vi har, med 7 sitteplasser."
            j "Det finner du om du følger gangen helt inn til høyre, og går til høyre ved datarommene."
            jump møterom_menu
        "Det var alt":
            show screen lobbyScreen
            jump lobby_menu