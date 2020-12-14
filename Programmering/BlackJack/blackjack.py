import kortlek

#behöver kunna räkna kortvärden

#handen
def skrivUtHanden(hand):
    print("Dina kort är: ", end="")
    for kort in hand:
        print(kort + ", ", end ="")

#checkaVinnare


#spel-loop
while True:
    spela = input("Vill du spela blackjack? (j för ja, annan tangent för nej)")
    
    if spela !="j":
        break   

    lek = kortlek.skapaKortlek()

    print(lek)
    #dealern tar 2 kort
    dealer = [lek.pop(0), lek.pop(0)]
    print(f"Dealerns förska kort är {dealer[0]}")
    
    hand = [lek.pop(0), lek.pop(0)]
    print(f"Dina första två kort är: {hand[0]} och {hand[1]}")

    fortsätt = True

    #göra val (ta ett till kort eller stanna)
    while fortsätt:
        #fråga användaren om hen vill ta ett kort
        taKort = input(
            "Ta nytt kort? (j för ja, annan tangent för stanna)")
        if taKort =="j":
            #dela ut ett kort
            hand.append(lek.pop(0))
            #skriva ut hand
            skrivUtHanden(hand)
        else:
            fortsätt = False
        )


#göra val(ta mer kort eller stanna)

