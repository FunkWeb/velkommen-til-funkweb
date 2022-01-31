# Confessions of a stressed developer to whom it may concern.
#Først og fremst, beklager for dette rotet...
#Jeg fant ut litt sent at man kan splitte opp spillet i flere .rpy scripts så alt ble crammed inn i ett dokument.
#Tips, renpy liker ikke ØÆÅ så bytt de ut når du lager variables.

#Logikken og dialogen for hvert rom er flyttet til rooms mappen.

define j = Character("Johnny")
define a = Character("Anders")
define i = Character("Ingeborg")
define r = Character("Reidar")
define q = Character("???")
#define am = Character("Amelie")

default lobbyBesokt = False

label start:

    scene bg inngang    

    "Du har endelig kommet deg opp til femte etasje."

    "På døren ser du Funkweb-logoen"

    "Det er første dagen din på arbeidsforberedene trening, eller AFT for kort."

    "På venstre siden av døren finner du en ringeklokke. Du trykker på den."

    show johnny at right with fade
    q "Heisann! Alltid fint å få nye folk inn i AFT!"
    j "Mitt navn er Johnny, hyggelig å møte deg."
    j "La meg vise deg rundt kjapt."

    jump lobby








 

