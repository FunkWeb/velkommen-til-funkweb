label bibliotek:
    scene bg vei til bibliotek 1 with fade
    pause 1
    scene bg vei til bibliotek 2 with fade
    pause 1
    scene bg bibliotek with fade
    show laila at left
    l "Her kan Laila si noe for å introdusere biblioteket."
    l "Vi må huske å erstatte denne placeholderen når vi vet hva vi vil ha her."
    #show screen bibliotekScreen

    menu bibliotek_menu:
        "Jeg vil se datarommet":
            jump datarom
        "Jeg vil se klasserommet":
            jump klasserom
        "Tilbake til lobbyen":
            jump lobby