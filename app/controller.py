from app import view
from app import model


def start(message):
    calculatrice = model.Calculatrice(message)
    view.display_interface(calculatrice)

def calculate(choice, calculatrice, operation):
    result = calculatrice.make_current_operation(operation[0].lower(),choice)
    return result

def ask_user(message):
    response = view.ask_user(message)
    return response
