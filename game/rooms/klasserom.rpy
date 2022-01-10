
label klasserom:

    scene bg klasserom with fade
    show ingeborg at right 
    show screen klasseromScreen

    "Foran deg er et stort rom med datamaskiner på rekke og rad."
    i "Dette rommet er utstyrt med enkle Chromebooks."
    i "Hvis du primært skal skrive CV, jobbsøknader eller kanskje ta noen onlinekurs kommer du til å sitte her."

    menu:
        "jeg vil se datarommet":
            hide screen klasseromScreen
            jump datarom
        "Tilbake til lobby":
            hide screen klasseromScreen
            jump lobby
