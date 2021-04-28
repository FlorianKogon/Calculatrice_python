from app import controller

class Calculatrice:

    def __init__(self,message='Bienvenue chez Alfred'):
        self.welcome = message
        print(self.welcome)

    def make_current_operation(self,operator,choice):

        numbers_list = Calculatrice.build_list_numbers(choice,operation=operator)
        result = Calculatrice.calculation(numbers_list,operator=operator)
        return result

    @classmethod
    def build_list_numbers(cls,choice,operation):
        list_numbers = []
        while choice.isdigit():
            if choice.isdigit():
                list_numbers.append(int(choice))
            choice = controller.ask_user(message=f"Saisir un chiffre à {operation} ou clicker sur '=' ")
        return list_numbers

    @classmethod
    def calculation(cls,numbers_list,operator):
        for index, number in enumerate(numbers_list):
            if index == 0:
                result = number
            else:
                if operator == 'm':
                    result = result * number
                elif operator == 'd':
                    result = result / number
                elif operator == 's':
                    result = result - number
                elif operator == 'a':
                    result = result + number
                else:
                    return None
        return result
