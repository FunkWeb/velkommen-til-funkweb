#image johnny = im.Scale("johnny.png",480,900)
#image anders = im.Scale("anders.png",480,900)
#image ingeborg = im.Scale("ingeborg.png",480,900)
#image reidar = im.Scale("reidar.png",480,900)

define j = Character("Johnny")
define a = Character("Anders")
define i = Character("Ingeborg")
define r = Character("Reidar")
define q = Character("???")

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

label lobby:

    scene bg lobby with ease
    show skrivemaskin at left

    if not lobbyBesokt:
        "Du går inn døren til et område med sofaer og fler dører."
        show johnny at right

        j "Ta å desinfiser hendene dine før vi går videre."
        scene bg antibac
        "Til venstre for døren ser du midler for å desinfisere hender og munnbind hvis du trenger det. Du kan også henge fra deg jakker her."
        scene bg lobby

        show johnny at right
        j "Dette er lobbyen."
        j "Her finner du møterom (møterom navn her) og toaletter."
        "Alltid godt å vite hvor toalettene er."
    
    else:
        show johnny at left
        "Da er vi tilbake til lobbyen, hvor vil du besøke neste?"
    
    $ lobbyBesokt = True

    menu lobby_menu:
        "Gå til kantinen":
            jump kantine
        "Gå til datarom og klasserom":
            scene bg gang tilaft with fade 
            pause 3.0
            jump velgDatarom
        "Hvor er toalettene?":
            jump toalettene
        "Ferdig for dagen":
            return

label kantine:
    scene bg lobby kantine with fade
    pause 3.0
    scene bg gang thailand with fade
    "Her finner du møterom Thailand og (møterom navn her)."    
    scene bg kantine with fade

    "Kantina ser ut som en ganske vanlig kontorkantine ved første blikk."
    "Når du ser deg litt rundt så ser du en del kjøleskap og kanskje noen pakker."
    show anders at left
    a "I kjølekapet lengst til venstre fra døren kan du legge mat du har med deg."
    a "Vanlig lunsjtid for kontoret er 11:30 til 12:00, men ikke føl et press for å spise her."

    menu kantine_meny:
        "Gå rundt å se litt":
            scene bg kantine kjøkken with fade
            pause 3
            scene bg kantine kjøleskap with fade
            "Kjøleskapet helt til høyre er for AFT deltakere. Til høyre for det igjen kan du kaste pant."
            scene bg kantine with fade
            jump kantine_meny
        "Gå tilbake til lobby":
            jump lobby 


label velgDatarom:
    menu aft_meny:
        "Det er to steder du kan besøke på vei til datarommene."
        "AFT kontor dør":
            jump aft
        "Kjøkken":
            jump gangKjokken
        "Gå videre":
            scene bg gang tildatarom with fade
            pause 3        
            scene bg gang dataromdør with fade
            jump velg

    menu velg:
        "Hva vil du se først?"
        "Datarom":
            jump datarom
        "Klasserom":
            jump klasserom
        "Tilbake til lobby":
            jump lobby
        

label datarom:
    scene bg datarom with fade
    show reidar at left
    show screen iconScreen 

    r "Her har du datarommet."
    r "Dette er rommet hvor AFT-deltakerene sitter og jobber med prosjekter."
    menu:
        "Jeg vil se klasserommet":
            hide screen iconScreen
            jump klasserom
        "Tilbake til lobby":
            hide screen iconScreen
            jump lobby

label klasserom:

    scene bg klasserom with fade
    show ingeborg at right 

    "Foran deg er et stort rom med datamaskiner på rekke og rad."
    i "Dette rommet er utstyrt med enkle Chromebooks."
    i "Hvis du primært skal skrive CV, jobbsøknader eller kanskje ta noen onlinekurs kommer du til å sitte her."

    menu:
        "jeg vil se datarommet":
            jump datarom
        "Tilbake til lobby":
            jump lobby

label toalettene:
    scene bg toaletter with fade

    "Godt å vite hvor toalettene er."

    menu :
        
        "Hva er inngangen til høyre for toalettene?":
            jump gangVedToaletter
        "Tilbake til lobby":
            jump lobby

label gangVedToaletter:

    scene bg gang spania with fade

    "Her finner du grupperom Spania og (Blank)"

    menu :
        "Tilbake til lobby":
            jump lobby

label aft:
    scene bg gangtilaft with fade
    pause 3
    scene bg aft with fade

    "Her er kontoret til alle AFT veilederne, hvis du har spørsmål kan du komme her."

    menu :
        
        "Er det et kjøkken bak meg?":
            jump lobby
        "Gå videre til datarommene":
            jump velgDatarom
        "Gå tilbake til lobby":
            jump lobby
        
label gangKjokken:
    
    scene bg gang kjøkken with fade

    "Kopper og glass finner du i skapene øverst. Ta kaffe og vann som du ønsker."

    menu :
        
        "Hva er døren bak meg?":
            jump aft
        "Gå videre til datarommene":
            jump velgDatarom
        "Gå tilbake til lobby":
            jump lobby
