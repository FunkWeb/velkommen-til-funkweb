
label datarom:
    scene bg datarom with fade
    show anders at left

    a "Hei, jeg heter Anders. Dette er prosjektrommet."
    a "Jeg er IT-ansvarlig her i huset."
    a "Du kan reservere arbeidsplass på booking.funkweb.no om du vil sitte her."
    a "Her kan du sitte å arbeide med Windows-maskiner og god utsikt over Oslo."
    a "Dette er rommet hvor AFT-deltakerene sitter og jobber med prosjekter."

    show screen dataromScreen

    menu:
        "Tilbake til gangen":
            hide screen dataromScreen
            jump velgDatarom
        "Tilbake til lobbyen":
            $ forbiDataromGang = False
            hide screen dataromScreen
            jump lobby