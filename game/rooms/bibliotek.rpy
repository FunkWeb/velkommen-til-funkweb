label bibliotek:
    scene bg vei til bibliotek 1 with fade
    pause 1
    scene bg vei til bibliotek 2 with fade
    pause 1
    scene bg bibliotek with fade
    #show screen bibliotekScreen

    "Placeholder text for biblioteket"
    menu bibliotek_menu:
        "jeg vil se datarommet":
            jump datarom
        "jeg vil se klasserommet":
            jump klasserom
        "Tilbake til lobby":
            jump lobby