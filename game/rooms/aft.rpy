label aft:
    #pause 2
    scene bg aft with fade

    "Her er kontoret til alle AFT veilederne, hvis du har spørsmål kan du komme her."

    #scene bg gang tilaft with fade
    menu :
        
        "Er det et kjøkken bak meg?":
            jump gangKjokken
        "Gå videre mot datarommene":
            jump velgDatarom
        "Gå tilbake til lobby":
            jump lobby
       