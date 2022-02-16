label bibliotek:
    scene bg vei til bibliotek 1 with fade
    pause 1
    scene bg vei til bibliotek 2 with fade
    pause 1
    scene bg bibliotek with fade
    "Du går inn i et stort møterom med prosjektor og noen bokhyller."
    show laila at left
    l "Hei, jeg heter Laila. Jeg er en alt-mulig person i FunkWeb."
    l "Bruk meg gjerne som et oppslagsverk. Jeg her mye erfaring i denne bransjen."
    l "Nå er du i biblioteket, det kalles det selv om det ikke er så mye bøker her."
    l "Dette er det største møterommet vi har."
    #show screen bibliotekScreen

    menu bibliotek_menu:
        "Tilbake til gangen":
            jump velgDatarom
        "Tilbake til lobbyen":
            $ forbiDataromGang = False
            jump lobby