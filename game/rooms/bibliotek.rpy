label bibliotek:
    scene bg vei til bibliotek 1 with fade
    pause 1
    scene bg vei til bibliotek 2 with fade
    pause 1
    scene bg bibliotek with fade
    "Du går inn i et stort møterom med prosjektor og noen bokhyller."
    show laila at left
    
    if bibliotekIntroFerdig:
        jump bibliotek_menu
    
    l "Hei, jeg heter Laila. Jeg er en alt-mulig person i FunkWeb."
    l "Bruk meg gjerne som et oppslagsverk. Jeg har mye erfaring i denne bransjen."
    $ bibliotekIntroFerdig = True

    label bibliotekBeskrivelse:
        l "Nå er du i biblioteket."
        l "Det kalles det på grunn av bokhyllene, selv om det ikke er så mange bøker her."
        l "Dette er det største møterommet vi har."

    menu bibliotek_menu:
        "\"Kan du fortelle meg om dette rommet igjen?\"":
            jump bibliotekBeskrivelse
        "Gå tilbake til gangen":
            jump velgDatarom
        "Gå tilbake til resepsjonen":
            $ forbiDataromGang = False
            jump lobby