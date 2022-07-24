class CoffeeMachine:
    # states: choosing_action, choosing_coffee, filling_water, filling_milk, filling_beans, filling_cups
    ESPRESSO = [250, 0, 16, 4]
    LATTE = [350, 75, 20, 7]
    CAPPUCCINO = [200, 100, 12, 6]

    def __init__(self, water, milk, coffee_beans, cups, cash):
        self.water_in_ml = water
        self.milk_in_ml = milk
        self.coffee_beans_in_gr = coffee_beans
        self.cups = cups
        self.cash_in_dollars = cash
        self.state = 'choosing_action'

    def print_message(self):
        if self.state == 'choosing_action':
            print('Write action (buy, fill, take, remaining, exit): ')
        elif self.state == 'choosing_coffee':
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
        elif self.state == 'filling_water':
            print('Write how many ml of water you want to add: ')
        elif self.state == 'filling_milk':
            print('Write how many ml of milk you want to add: ')
        elif self.state == 'filling_beans':
            print('Write how many grams of coffee beans you want to add: ')
        elif self.state == 'filling_cups':
            print('Write how many disposable cups you want to add: ')

    def start_machine(self, action):
        if self.state == 'choosing_action':
            if action == 'exit':
                return 0
            elif action == 'buy':
                self.state = 'choosing_coffee'
            elif action == 'fill':
                self.state = 'filling_water'
            elif action == 'take':
                self.take_money()
            elif action == 'remaining':
                self.print_resources()
            else:
                print('Invalid action')
        elif self.state == 'choosing_coffee':
            self.buy_coffee(action)
            self.state = 'choosing_action'
        elif self.state == 'filling_water':
            self.fill_water(action)
            self.state = 'filling_milk'
        elif self.state == 'filling_milk':
            self.fill_milk(action)
            self.state = 'filling_beans'
        elif self.state == 'filling_beans':
            self.fill_beans(action)
            self.state = 'filling_cups'
        elif self.state == 'filling_cups':
            self.fill_cups(action)
            self.state = 'choosing_action'

    def buy_coffee(self, coffee_input):

        if coffee_input == 'back':
            return
        elif coffee_input == '1':
            coffee_type = self.ESPRESSO
        elif coffee_input == '2':
            coffee_type = self.LATTE
        elif coffee_input == '3':
            coffee_type = self.CAPPUCCINO
        else:
            print('Invalid action')
            return

        water_diff = self.water_in_ml - coffee_type[0]
        milk_diff = self.milk_in_ml - coffee_type[1]
        beans_diff = self.coffee_beans_in_gr - coffee_type[2]
        cups_diff = self.cups - 1

        if (water_diff >= 0) and (milk_diff >= 0) and (beans_diff >= 0) and (cups_diff >= 0):
            print('I have enough resources, making you a coffee!')
            self.cash_in_dollars += coffee_type[3]
            self.water_in_ml -= coffee_type[0]
            self.milk_in_ml -= coffee_type[1]
            self.coffee_beans_in_gr -= coffee_type[2]
            self.cups -= 1
        else:
            shortage = []
            if water_diff < 0:
                shortage.append('water')
            if milk_diff < 0:
                shortage.append('milk')
            if beans_diff < 0:
                shortage.append('coffee beans')
            if cups_diff < 0:
                shortage.append('cups')
            print(f'Sorry, not enough {", ".join(shortage)}!')

        return

    def fill_water(self, action):
        self.water_in_ml += int(action)
        return

    def fill_milk(self, action):
        self.milk_in_ml += int(action)
        return

    def fill_beans(self, action):
        self.coffee_beans_in_gr += int(action)
        return
        
    def fill_cups(self, action):
        self.cups += int(action)
        return

    def take_money(self):
        given_money = self.cash_in_dollars
        self.cash_in_dollars = 0
        print(f'I gave you ${given_money}')
        return

    def print_resources(self):
        print('The coffee machine has:')
        print(f'{self.water_in_ml} ml of water')
        print(f'{self.milk_in_ml} ml of milk')
        print(f'{self.coffee_beans_in_gr} g of coffee beans')
        print(f'{self.cups} disposable cups')
        print(f'{self.cash_in_dollars} of money')
        return


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    coffee_machine.print_message()
    run = coffee_machine.start_machine(input())
    if run == 0:
        break
