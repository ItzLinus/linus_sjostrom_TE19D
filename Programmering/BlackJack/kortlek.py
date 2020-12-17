import random as rd
# lista för att hålla våra kort
def skapaKortlek():
    kortNummer = [i for i in range(2,11)]
    
    # klädda kort
    klädkort = ["J","Q","K","A"]
    kortNummer += klädkort
    lek = 4*kortNummer
    blandaKort(lek)

    return lek

# behöver kunna blanda korten

def blandaKort(lek):
    return rd.shuffle(lek)

kortlek = skapaKortlek()
