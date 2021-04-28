def ask_user(sentence):
    choice = input(sentence + "\n>")
    return choice


def calculate(number, operation):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))  # conversion en entier
        number = ask_user(f"Saisir un chiffre à {operation} ou clicker sur '=' ")
    for list_number, index in zip(list_numbers,list(range(len(list_numbers)))): # refactoriser
        if index == 0:
            result = list_number
        else:
            if operation == "soustraire":
                result -= list_number
            elif operation == "multiplier":
                result *= list_number
            elif operation == "diviser":
                result /= list_number
            elif operation == "additionner":
                result += list_number
    return result


def display_interface():
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
            result = calculate(choice, "additionner")
        elif choice == 2:
            choice = ask_user("Saisir un chiffre à SOUSTRAIRE ou clicker sur '=' ")
            result = calculate(choice, "soustraire")
        elif choice == 3:
            choice = ask_user("Saisir un chiffre à MULTIPLIER ou clicker sur '=' ")
            result = calculate(choice, "multiplier")
        elif choice == 4:
            choice = ask_user("Saisir un chiffre à DIVISER ou clicker sur '=' ")
            result = calculate(choice, "diviser")
        return print(f"Le resultat est ==> {result}")
