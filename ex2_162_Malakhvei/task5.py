d_main = {'cake': ["flour, eggs, fat, butter, sugar, salt, milk, cherries, E259", 100, 4500],
          'cupcake': ['flour, milk, egg, sugar, salt, butter, vanilla extract, E340, E210', 230, 5600],
          'muffin': ['flour, milk, egg, sugar, salt, shortening, baking powder, chocolate', 60, 3400]}


# Заключаем в отдельную функцию алгоритм действий для каждого возможного выбора
def get_description():
    for x in d_main:
        print(f'{x} ingredients are: {d_main[x][0]}')


def get_price():
    for x in d_main:
        print(f'{x} price per 100 g is: {d_main[x][1]} EUR')


def get_quantity():
    for x in d_main:
        print(f'Available quantity of {x} is: {d_main[x][2]} g')


def get_all_info():
    for x in d_main:
        print(f'Item: {x}, price per 100g: {d_main[x][1]} EUR,'
              f' available quantity: {d_main[x][2]}g, ingredients: {d_main[x][0]}')


def make_purchase():
    print('Purchase mode. Enter "n" to exit')
    while True:
        inp = input('Enter item and quantity (in g) separated with " ": ')
        if inp == "n":
            print('Exit from purchase mode')
            break
        else:
            try:
                L = inp.split()
                if d_main[L[0]][2] - int(L[1]) > 0:
                    d_main[L[0]][2] -= int(L[1])
                    print(f'{(int(L[1]) / 100) * d_main[L[0]][1]} EUR spent. {d_main[L[0]][2]}g of {L[0]} available')
                else:
                    print(f'not enough {L[0]} available ')
            except KeyError:
                print('Invalid Item entered')
            except ValueError:
                print('Invalid quantity entered')


# Значению каждого возможного выбора будет соовтетсвовать объект соответсвующей функции
d_actions = {'1': get_description, '2': get_price, '3': get_quantity, '4': get_all_info, '5': make_purchase}

print('Welcome to Baker`s shop! Enter 1 to get descriptions, 2 - to get prices, 3 - to get available quantity,'
      '4 - to get all information, 5 - to make purchases, 6 - to leave')
while True:
    print('-' * 20)
    choice = input('Enter Your choice: ')
    if choice == '6':
        print('Bye! Bye! See You soon!')
        break
    else:
        try:
            d_actions[choice]()
        except KeyError:
            print('Invalid choice')
