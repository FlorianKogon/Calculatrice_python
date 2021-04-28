from app import controller

def ask_user(sentence):
    choice = input(sentence + "\n>")
    return choice

def display_interface(calculatrice):
    choice = ask_user("""
    Tu veux :
    1. Additionner Tape 1
    2. Soustraire Tape 2
    3. Multiplier Tape 3
    4. Diviser Tape 4""")
    while choice.isdigit():
        choice = int(choice) #conversion en entier
        if choice == 1:
            choice = ask_user("Saisir un chiffre à ADDITIONNER ou clicker sur '=' ")
            result = controller.calculate(choice, calculatrice, "additionner")
        elif choice == 2:
            choice = ask_user("Saisir un chiffre à SOUSTRAIRE ou clicker sur '=' ")
            result = controller.calculate(choice, calculatrice, "soustraire")
        elif choice == 3:
            choice = ask_user("Saisir un chiffre à MULTIPLIER ou clicker sur '=' ")
            result = controller.calculate(choice, calculatrice, "multiplier")
        elif choice == 4:
            choice = ask_user("Saisir un chiffre à DIVISER ou clicker sur '=' ")
            result = controller.calculate(choice, calculatrice, "diviser")
        return print(f"Le resultat est ==> {result}")
