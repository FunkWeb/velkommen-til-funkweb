
label datarom:
    scene bg datarom with fade
    show anders at left

    if dataromIntroFerdig:
        jump datarom_menu

    a "Hei, jeg heter Anders. Jeg er IT-ansvarlig her i huset."
    $ dataromIntroFerdig = True

    label dataromBeskrivelse:
        a "Dette er prosjektrommet."
        a "Du kan reservere arbeidsplass på booking.funkweb.no om du vil sitte her."
        a "Her kan du sitte å arbeide med Windows-maskiner og god utsikt over Oslo."
    
    show screen dataromScreen

    menu datarom_menu:
        "\"Kan du fortelle meg om dette rommet igjen?\"":
            jump dataromBeskrivelse
        "Tilbake til gangen":
            hide screen dataromScreen
            jump velgDatarom
        "Tilbake til lobbyen":
            $ forbiDataromGang = False
            hide screen dataromScreen
            jump lobby