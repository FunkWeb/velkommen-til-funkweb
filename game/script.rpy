# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Johnny")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg inngang    

    "Du har endelig kommet deg opp til femte etasje."

    "På døren ser du Funkweb logoen"

    "Det er første dagen din på arbeidsforberedene trening, eller AFT for kort."

    "På venstre siden av døren finner du en ringeklokke. Du trykker på den."

    "Her kommer Johnny inn og sier noe som Johnny ville si."
    show Johnny
    j "Heisan! Alltid hyggelig å få nye folk inn i AFT!"
    j "La meg vise deg rundt kjapt."

    scene bg lobby

    "Du går inn døren til et rom med sofaer og mange dører."
    j "Ta å desinfiser hendene dine før vi går videre."
    "Du tar tiden til å desinfiserre deg. Best å være sikker."

    j "Dette er lobbyen"
    j "Her finner du møterom (møterom navn her) og toaletter"
    "Alltid godt å vite hvor toalettene er"

    # This ends the game.

    return
