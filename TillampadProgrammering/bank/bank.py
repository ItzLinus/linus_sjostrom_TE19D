import funktioner


read_file()
# PROGRAMLOOP
while True:     
#Program Meny
    meny = (f"\n≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖\n"
            "\n           ▶ B͏a͏n͏k͏ o͏f͏ J͏a͏p͏a͏n͏ ◀"
            "\n\n≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖"
            "\n\n<=> 1. Redovisa Saldo             <=>"
            "\n<=> 2. Insättning                 <=>"
            "\n<=> 3. Uttag                      <=>"
            "\n<=> 0. Avsluta/Stoppa programmet  <=>"
            "\n\n≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖"
            "\n<=> Gör ditt val:                 <=>\n\n"
            "").format(saldo())


    välj = validate_int(meny, "Felaktig Inmatning!")

    if välj == 0:               # Avslutar/Stoppar programmet
        break

    elif välj == 1:             # Redovisar Transaktioner
        print(print_transactions())

    elif välj == 2:             # Sätt in pengar
        print("<=>   Insättning   <=>")
        insättning = int(input("<=>  Ange Belopp:  <=>"))
        if insättning > 0:
            add_transaction(insättning, True)
        else:
            print("⊘ Insättningen måste vara större än 0! ⊘")

    elif välj == 3:             # Gör din Uttag
        print("<=>     Uttag     <=>")
        uttag = int(input("<=>  Ange Belopp:  <=>"))
        if uttag <= saldo() and uttag >= 0:
            add_transaction(-uttag, True)
        elif uttag < 0:
            print("⊘ Uttaget måste vara större än 0! ⊘")
        else:
            print("⊘ Beloppet får inte vara större än saldo! ⊘")


    else:
        print("<=>  Felaktigt val!  <=>")

print("\nTack för ditt besök, välkommen åter!")