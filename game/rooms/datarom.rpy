
label datarom:
    scene bg datarom with fade
    show reidar at left

    r "Her har du datarommet."
    r "Dette er rommet hvor AFT-deltakerene sitter og jobber med prosjekter."

    show screen dataromScreen

    menu:
        "Jeg vil se klasserommet":
            hide screen dataromScreen
            jump klasserom
        "Jeg vil se biblioteket":
            hide screen dataromScreen
            jump bibliotek
        "Tilbake til lobbyen":
            hide screen dataromScreen
            jump lobby