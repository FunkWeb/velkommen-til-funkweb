
label klasserom:

    scene bg klasserom with fade
    show ingeborg at right 

    "Foran deg er et stort rom med datamaskiner på rekke og rad."
    i "Velkommen til klasserommet. Jeg heter Ingeborg."
    i "Jeg lover at jeg ikke er så skummel som jeg ser ut."
    i "Dette er ett av to rom du kan booke for å sitte å arbeide i."
    i "Du kan reservere plass på booking.funkweb.no."
    i "Dette rommet er utstyrt med enkle Chromeboxes."
    i "Her kan du skrive CV, jobbsøknader eller kanskje ta noen onlinekurs."

    show screen klasseromScreen

    menu:
        "Tilbake til gangen":
            hide screen klasseromScreen
            jump velgDatarom
        "Tilbake til lobbyen":
            $ forbiDataromGang = False
            hide screen klasseromScreen
            jump lobby