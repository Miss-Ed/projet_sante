print('===================================================')
print('                   CALCULATRICE                    ')
print('===================================================')
print('(Tapez "q" a tout moment pour annuler le calcul en cours)')


def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        print('Erreur : division par zero impossible')
        return a  # on garde le resultat inchange en cas d'erreur


def demander_nombre(message):
    while True:
        saisie = input(message)
        if saisie == 'q':
            return None
        try:
            return float(saisie)
        except ValueError:
            print('Saisie invalide. Merci de taper un nombre.')


def demander_operateur(message):
    while True:
        saisie = input(message)
        if saisie == 'q':
            return None
        if saisie in ('+', '-', '*', '/'):
            return saisie
        print('Operation invalide. Merci de taper +, -, * ou /.')


nouveau_calcul = True

while nouveau_calcul:
    resultat = demander_nombre('Entrez le premier nombre : ')
    if resultat is None:
        print('Calcul annule.')
        continue

    continuer = 'o'

    while continuer == 'o':
        operateur = demander_operateur('Operateur (+, -, *, /) : ')
        if operateur is None:
            print('Calcul annule.')
            break

        nombre = demander_nombre('Entrez le nombre suivant : ')
        if nombre is None:
            print('Calcul annule.')
            break

        if operateur == '+':
            resultat = addition(resultat, nombre)
        elif operateur == '-':
            resultat = soustraction(resultat, nombre)
        elif operateur == '*':
            resultat = multiplication(resultat, nombre)
        elif operateur == '/':
            resultat = division(resultat, nombre)

        print('Resultat :', resultat)

        continuer = input('Voulez-vous continuer ? (o/n/q) : ').lower()
        while continuer != 'o' and continuer != 'n' and continuer != 'q':
            print('Reponse invalide. Merci de taper "o" pour continuer, "n" pour arreter, ou "q" pour recommencer.')
            continuer = input('Voulez-vous continuer ? (o/n/q) : ').lower()

        if continuer == 'q':
            print('On recommence un nouveau calcul.')

    if continuer == 'n':
        nouveau_calcul = False
        print('Resultat final :', resultat)

print('Merci d\'avoir utilise la calculatrice !')