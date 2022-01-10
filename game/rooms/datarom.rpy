
label datarom:
    scene bg datarom with fade
    show reidar at left
    show screen dataromScreen 

    r "Her har du datarommet."
    r "Dette er rommet hvor AFT-deltakerene sitter og jobber med prosjekter."
    menu:
        "Jeg vil se klasserommet":
            hide screen dataromScreen
            jump klasserom
        "Tilbake til lobby":
            hide screen dataromScreen
            jump lobby