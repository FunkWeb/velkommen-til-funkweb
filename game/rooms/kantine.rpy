
label kantine:
    scene bg lobby kantine with fade
    pause 3.0
    scene bg gang thailand with fade
    "Her finner du møterom Thailand og (møterom navn her). Kantinen er til høyre."    
    scene bg kantine with fade
    show screen kantineScreen

    "Kantina ser ut som en ganske vanlig kontorkantine ved første blikk."
    "Når du ser deg litt rundt så ser du en del kjøleskap og kanskje noen pakker."
    show anders at left
    a "I kjølekapet lengst til venstre fra døren kan du legge mat du har med deg."
    a "Vanlig lunsjtid for kontoret er 11:30 til 12:00, men ikke føl et press for å spise her."

    menu kantine_meny:
        "Gå rundt å se litt":
            scene bg kantine kjøkken with fade
            pause 3
            scene bg kantine bak with fade
            pause 3
            scene bg kantine kjøleskap with fade
            pause 3
            #"Kjøleskapet helt til høyre er for AFT deltakere. Til høyre for det igjen kan du kaste pant."
            scene bg kantine with fade
            jump kantine_meny
        "Gå tilbake til lobby":
            hide screen kantineScreen
            jump lobby 

