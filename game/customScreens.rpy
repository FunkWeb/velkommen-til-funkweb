#datarom knapper------------------------------------------------------------------
screen dataromScreen():
    imagebutton:
        xalign 0.90
        yalign 0.0
        idle "skrivemaskin"
        #hover_color "#7d7d7d"
        action [ui.callsinnewcontext("skrivemaskinIkon")]
    imagebutton:
        xalign 0.80
        yalign 0.0
        idle "vanlig_datamaskin"
        #hover_color "#7d7d7d"
        action [ui.callsinnewcontext("datamaskinIkon")]

label skrivemaskinIkon:
    hide screen iconScreen
    show anders
    "her kan en veileder si noe om objectet. Skriveren i dette tilfellet"
    hide anders
    return

label datamaskinIkon:
    hide screen iconScreen
    show anders
    "her kan en veileder si noe om objectet. Skriveren i dette tilfellet"
    hide anders
    return

#Klasserom knapper---------------------------------------------------------------
screen klasseromScreen():
    imagebutton:
        xalign 0.90
        yalign 0.0
        idle "chromebook"
        #hover_color "#7d7d7d"
        action [ui.callsinnewcontext("skrivemaskinIkon")]

label chromebookIkon:
    hide screen iconScreen
    show anders
    "her kan en veileder si noe om objectet. Skriveren i dette tilfellet"
    hide anders
    return

#Kantine knapper----------------------------------------------------------------
screen kantineScreen():
    imagebutton:
        xalign 0.90
        yalign 0.0
        idle "kjoleskap"
        #hover_color "#7d7d7d"
        action [ui.callsinnewcontext("kjoleskapIkon")]
    imagebutton:
        xalign 0.80
        yalign 0.0
        idle "panteflasker"
        #hover_color "#7d7d7d"
        action [ui.callsinnewcontext("pantIkon")]
    imagebutton:
        xalign 0.70
        yalign 0.0
        idle "kaffemaskin"
        #hover_color "#7d7d7d"
        action [ui.callsinnewcontext("kaffeIkon")]

label kjoleskapIkon:
    hide screen kantineScreen
    show anders
    "her kan en veileder si noe om objectet. Skriveren i dette tilfellet"
    hide anders
    return

label pantIkon:
    hide screen kantineScreen
    show anders
    "her kan en veileder si noe om objectet. Skriveren i dette tilfellet"
    hide anders
    return

label kaffeIkon:
    hide screen kantineScreen
    show anders
    "her kan en veileder si noe om objectet. Skriveren i dette tilfellet"
    hide anders
    return