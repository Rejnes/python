import random

def gra():
    user = input("jaki jest twój wybór? 'k' dla kamien, 'p' dla papier, 'n' dla nożyce\n")
    computer = random.choice(['k', 'p', 'n'])
 
    if user == computer:
        return 'remis'

    if wygrana(user, computer):
        return 'wygrałeś'

    return 'przegrałeś'

def wygrana(gracz, przeciwnik):
    if (gracz == 'k' and przeciwnik == 'n') or (gracz == 'n' and przeciwnik == 'p') or (gracz == 'p' and przeciwnik == 'k'):
        return True
    
print(gra())