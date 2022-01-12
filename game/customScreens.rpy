#Lobby knapper

#datarom knapper------------------------------------------------------------------
screen dataromScreen():
    imagebutton:
        xalign 0.90
        yalign 0.0
        idle "skrivemaskin"
        #hover_color "#7d7d7d"
        action [ui.callsinnewcontext("skrivemaskinIkon")]
    imagebutton:
        xalign 0.70
        yalign 0.1
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
    "her kan en veileder si noe om objectet. Datamaskinen i dette tilfellet"
    hide anders
    return

#Klasserom knapper---------------------------------------------------------------
screen klasseromScreen():
    imagebutton:
        xalign 0.50
        yalign 0.05
        idle "chromebook"
        #hover_color "#7d7d7d"
        action [ui.callsinnewcontext("chromebookIkon")]

label chromebookIkon:
    hide screen iconScreen
    show anders
    "her kan en veileder si noe om objectet. Chromebook i dette tilfellet"
    hide anders
    return

#Kantine knapper----------------------------------------------------------------
screen kantineScreen():
    imagebutton:
        xalign 0.30
        yalign 0.0
        idle "kjoleskap"
        #hover_color "#7d7d7d"
        action [ui.callsinnewcontext("kjoleskapIkon")]
    imagebutton:
        xalign 0.50
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
    "her kan en veileder si noe om objectet. Kjøleskapet i dette tilfellet"
    hide anders
    return

label pantIkon:
    hide screen kantineScreen
    show anders
    "her kan en veileder si noe om objectet. Panteposen i dette tilfellet"
    hide anders
    return

label kaffeIkon:
    hide screen kantineScreen
    show anders
    "her kan en veileder si noe om objectet. Kaffemaskinen i dette tilfellet"
    hide anders
    return


# Lobby knapper---------------------------------------------------------------

screen lobbyScreen():
    imagebutton:
        xalign 0.5
        yalign 0.0
        idle "smittevern"
        #hover_color "#7d7d7d"
        action [ui.callsinnewcontext("smittevernIkon")]

label smittevernIkon:
    hide screen lobbyScreen
    show anders
    "her kan en veileder si noe om objectet. Smittevern i dette tilfellet"
    hide anders
    return


# Brannslukker---------------------

label brannslukkerIkon:
    #hide screen kantineScreen
    show anders
    "her kan en veileder si noe om objectet. Brannslukker i dette tilfellet"
    hide anders
    return