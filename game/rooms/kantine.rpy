
label kantine:
    scene bg lobby kantine with fade
    pause 2.0
    scene bg gang thailand with fade
    "Her finner du møterom Thailand og Tibet. Kantina er til høyre."    
    scene bg kantine with fade

    "Kantina ser ut som en ganske vanlig kontorkantine ved første blikk."
    "Når du ser deg litt rundt så ser du en del kjøleskap og kanskje noen pakker."
    show anders at left
    a "I kjølekapet lengst til venstre fra døren kan du legge mat du har med deg."
    a "Vanlig lunsjtid for kontoret er 11:30 til 12:00, men ikke føl deg presset til å spise her."

    show screen kantineScreen

    menu kantine_meny:
        "Se deg litt rundt i kantina":
            scene bg kantine kjøkken with fade
            pause 2
            scene bg kantine bak with fade
            pause 2
            scene bg kantine kjøleskap with fade
            pause 2
            #"Kjøleskapet helt til høyre er for AFT deltakere. Til høyre for det igjen kan du kaste pant."
            scene bg kantine with fade
            jump kantine_meny
        "Gå tilbake til lobbyen":
            hide screen kantineScreen
            jump lobby 

