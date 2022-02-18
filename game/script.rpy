#
#Tips, renpy liker ikke ØÆÅ så bytt de ut når du lager variables.

#Logikken og dialogen for hvert rom er flyttet til rooms mappen.

define j = Character("Johnny")
define a = Character("Anders")
define q = Character("???")
define l = Character("Laila")
define am = Character("Amelie")
define s = Character("Simen")

default lobbyBesokt = False
default forbiDataromGang = False

default dataromIntroFerdig = False
default bibliotekIntroFerdig = False
default kantineIntroFerdig = False
default klasseromIntroFerdig = False

label start:

    scene bg inngang    

    "Du har endelig kommet deg opp til femte etasje."

    "På døren ser du Funkweb-logoen"

    "Det er første dagen din på arbeidsforberedene trening, eller AFT for kort."

    "På venstre siden av døren finner du en ringeklokke. Du trykker på den."

    show johnny at right with fade
    q "Heisann!"
    j "Mitt navn er Johnny, hyggelig å møte deg."
    j "Jeg er veileder her på FunkWeb og jobber i AFT: arbeidsforberedene tiltak."
    j "Jeg elsker å prate om film, så hvis du øsnker å nerde litt om det er jeg alltid positiv til det."
    j "Jeg snakker også flytende spansk."
    j "La meg vise deg rundt kjapt."

    jump lobby








 

