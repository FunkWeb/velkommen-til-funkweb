
label kantine:
    scene bg lobby kantine with fade
    pause 2.0
    scene bg gang thailand with fade
    "Her finner du møterommene Kina, Thailand og Tibet. Kantina er til høyre."    
    scene bg kantine with fade

    "Kantina ser ut som en ganske vanlig kontorkantine ved første blikk."
    "Når du ser deg litt rundt så ser du et kjøkken med noen kjøleskap og noen spisebord."
    show anders at left
    a "I kjølekapet lengst til venstre fra døren kan du legge mat du har med deg."
    a "Vanlig lunsjtid for kontoret er 11:30 til 12:00, men ikke føl deg presset til å spise her da."
    a "Innerst til høyre ligger også møterommet Brazil."

    show screen kantineScreen

    menu kantine_meny:
        "Se deg litt rundt i kantina":
            hide screen kantineScreen
            scene bg kantine kjøkken with fade
            pause 2
            scene bg kantine bak with fade
            pause 2
            scene bg kantine kjøleskap with fade
            pause 2
            #"Kjøleskapet helt til høyre er for AFT deltakere. Til høyre for det igjen kan du kaste pant."
            scene bg kantine with fade
            show screen kantineScreen
            jump kantine_meny
        "Gå tilbake til lobbyen":
            hide screen kantineScreen
            jump lobby 

