
label klasserom:

    scene bg klasserom with fade
    show simen2 at right 

    "Foran deg er et stort rom med datamaskiner på rekke og rad."
    s "Velkommen til klasserommet. Jeg heter Simen."
    s "Jeg har jobbet her i seks år, så om du lurer på noe kan jeg helt sikkert hjelpe."
    s "Dette er ett av to rom du kan booke for å sitte å arbeide i."
    s "Du kan reservere plass på booking.funkweb.no."
    s "Dette rommet er utstyrt med enkle Chromeboxes."
    s "Her kan du skrive CV, jobbsøknader eller kanskje ta noen onlinekurs."

    show screen klasseromScreen

    menu:
        "Tilbake til gangen":
            hide screen klasseromScreen
            jump velgDatarom
        "Tilbake til lobbyen":
            $ forbiDataromGang = False
            hide screen klasseromScreen
            jump lobby