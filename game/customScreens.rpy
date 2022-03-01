#Lobby knapper

#datarom knapper------------------------------------------------------------------
screen dataromScreen():
    imagebutton:
        xalign 0.60
        yalign 0.0
        idle "skrivemaskin"
        #hover_color "#7d7d7d"
        action [ui.callsinnewcontext("skrivemaskinIkon")]
    imagebutton:
        xalign 0.40
        yalign 0.1
        idle "vanlig_datamaskin"
        #hover_color "#7d7d7d"
        action [ui.callsinnewcontext("datamaskinIkon")]

label skrivemaskinIkon:
    hide screen iconScreen
    a "Du kan bruke printeren når du trenger det."
    a "Den har navnet AFT-skriver i systemet."
    return

label datamaskinIkon:
    hide screen iconScreen
    a "Disse datamaskinene kjører hovedsakelig Windows."
    a "De to PC-ene nærmest døren er kraftigere gaming-maskiner."
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
    s "Datamaskinene her er Chromebooks som bruker Chrome OS."
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
    am "Her kan du legge lunsjen din så den holder seg kald."
    am "Kjøleskapet som står nærmest vinduet kan brukes av deltakere."
    return

label pantIkon:
    hide screen kantineScreen
    am "Pantbare tomflasker plasseres her i panteposen."
    am "Det er viktig å resirkulere."
    return

label kaffeIkon:
    hide screen kantineScreen
    am "Forsyn deg gjerne med nytraktet kaffe herfra."
    am "Lag helst mer om du tar den siste koppen."
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
    scene bg antibac
    j "Ved inngangen står det antibac og diverse smittevernsutstyr."
    j "Vi prøver å begrense smittespredning. Det er fint om du spriter deg når du kommer og før du går."
    return


# Brannslukker---------------------

label brannslukkerIkon:
    #hide screen kantineScreen
    "her kan en veileder si noe om objectet. Brannslukker i dette tilfellet"
    return