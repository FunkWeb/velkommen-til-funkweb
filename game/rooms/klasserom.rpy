
label klasserom:

    scene bg klasserom with fade
    show simen2 at right 

    "Foran deg er et stort rom med datamaskiner på rekke og rad."
    
    if klasseromIntroFerdig:
        jump klasserom_menu

    s "Velkommen til klasserommet. Jeg heter Simen."
    s "Jeg har jobbet her i seks år, så om du lurer på noe kan jeg helt sikkert hjelpe."
    $ klasseromIntroFerdig = True

    label klasseromBeskrivelse:
        s "Klasserommet er ett av to rom du kan booke for å sitte å arbeide i."
        s "Du kan reservere plass på booking.funkweb.no."
        s "Dette rommet er utstyrt med enkle Chromeboxes."
        s "Her kan du skrive CV, jobbsøknader eller kanskje ta noen onlinekurs."

    show screen klasseromScreen

    menu klasserom_menu:
        "\"Kan du fortelle meg om dette rommet igjen?\"":
            jump klasseromBeskrivelse
        "Gå tilbake til gangen":
            hide screen klasseromScreen
            jump velgDatarom
        "Gå tilbake til resepsjonen":
            $ forbiDataromGang = False
            hide screen klasseromScreen
            jump lobby