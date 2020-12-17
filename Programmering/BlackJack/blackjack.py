import kortlek

#behöver kunna räkna kortvärden
def räknaPoäng(hand):
    poäng = 0
    for kort in hand:
        if kort == "J" or kort == "Q" or kort == "K":
            poäng += 10
        elif kort == "A" and poäng < 11:
            poäng += 11
        elif kort == "A" and poäng >= 11:
            poäng += 1
        else:
            poäng += kort
    return poäng        


#handen
def skrivUtHanden(hand):
    print("Dina kort är: ", end="")
    for kort in hand:
        print(kort + ", ", end ="")

#checkaVinnare
def checkaVinnare(hand, dealer):
    dealerPoäng = räknaPoäng(dealer)
    spelarePoäng = räknaPoäng(hand)

    print(f"Dealerns kort är {dealer[0]} och dealer {dealer[1]}.")
    print(f"Dealerns totala poäng är {dealerPoäng}.")
    print(f"Din totala poäng är {spelarePoäng}.")
    
    if spelarePoäng == 21:
        print("Blackjack, du vinner!")
    elif spelarePoäng <= dealerPoäng or spelarePoäng > 21:
        print("Dealern tar dina pengar")
    else:
        print(" ")
        print(" ")
        print("Du vinner!")

#spel-loop
while True:
    spela = input("Vill du spela blackjack? (j för ja, annan tangent för nej)")
    
    if spela !="j":
        break   #hoppar ut ur while-satsen.

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

    checkaVinnare(hand, dealer)
    

print("Spelet slutar, ha en bra dag!")

