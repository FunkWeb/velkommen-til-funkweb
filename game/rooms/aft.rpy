label aft:
    #pause 2
    scene bg aft with fade

    j "Her er kontoret til alle AFT-veilederne."
    j "Om du skal ha tak i noen her, så kan du sende en chat."

    #scene bg gang til aft with fade
    menu :
        
        "Snu deg mot kjøkkenet":
            jump gangKjokken
        "Gå videre mot datarommene":
            jump velgDatarom
        "Gå tilbake til resepsjonen":
            jump lobby
       