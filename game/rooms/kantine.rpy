
label kantine:
    scene bg lobby kantine with fade
    pause 2.0
    scene bg gang thailand with fade
    "Her finner du møterommene Kina, Thailand og Tibet. Kantina er til høyre."    
    scene bg kantine with fade

    "Kantina ser ut som en ganske vanlig kontorkantine ved første blikk."
    "Når du ser deg litt rundt så ser du et kjøkken med noen kjøleskap og noen spisebord."
    show amelie at left
    am "Hei, er du sulten? Da har du kommet til rett sted."
    am "Jeg heter Amelie, og dette er kantina."
    am "Jeg er veileder her, og er åpen for spørsmål når som helst."
    am "I kjølekapet til venstre fra døren kan du legge mat du har med deg."
    am "Vanlig lunsjtid for kontoret er 11:30 til 12:00, men du kan bruke kantina når som helst når du trenger en pause."
    am "Innerst til høyre ligger også møterommet Brazil."

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

