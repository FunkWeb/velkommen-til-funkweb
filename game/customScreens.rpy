screen iconScreen():
    imagebutton:
        xalign 0.90
        yalign 0.0
        idle "skrivemaskin"
        action Jump("skriveren")

label skriveren:
    hide screen iconScreen
    show anders
    "her kan en veileder si noe om objectet. Skriveren i dette tilfellet"
    hide anders
    jump datarom