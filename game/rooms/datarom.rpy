
label datarom:
    scene bg datarom with fade
    show reidar at left

    r "Her har du datarommet."
    r "Dette er rommet hvor AFT-deltakerene sitter og jobber med prosjekter."

    show screen dataromScreen

    menu:
        "Tilbake til gangen":
            hide screen dataromScreen
            jump velgDatarom
        "Tilbake til lobbyen":
            $ forbiDataromGang = False
            hide screen dataromScreen
            jump lobby