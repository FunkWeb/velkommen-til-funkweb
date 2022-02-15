
label klasserom:

    scene bg klasserom with fade
    show ingeborg at right 

    "Foran deg er et stort rom med datamaskiner på rekke og rad."
    i "Dette rommet er utstyrt med enkle Chromeboxes."
    i "Hvis du primært skal skrive CV, jobbsøknader eller kanskje ta noen onlinekurs kan du sitte her."

    show screen klasseromScreen

    menu:
        "Tilbake til gangen":
            hide screen klasseromScreen
            jump velgDatarom
        "Tilbake til lobbyen":
            $ forbiDataromGang = False
            hide screen klasseromScreen
            jump lobby