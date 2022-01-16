
label klasserom:

    scene bg klasserom with fade
    show ingeborg at right 
    show screen klasseromScreen

    "Foran deg er et stort rom med datamaskiner på rekke og rad."
    i "Dette rommet er utstyrt med enkle Chromeboxes."
    i "Hvis du primært skal skrive CV, jobbsøknader eller kanskje ta noen onlinekurs kommer du til å sitte her."

    menu:
        "Jeg vil se datarommet":
            hide screen klasseromScreen
            jump datarom
        "Jeg vil se biblioteket":
            hide screen klasseromScreen
            jump bibliotek
        "Tilbake til lobbyen":
            hide screen klasseromScreen
            jump lobby
