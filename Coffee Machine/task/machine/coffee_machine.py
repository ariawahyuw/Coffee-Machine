class Coffee:
    ingredient = ['water', 'milk', 'coffee beans', 'cups', '']
    espresso = [250, 0, 16, 1, -4]
    latte = [350, 75, 20, 1, -7]
    cappuccino = [200, 100, 12, 1, -6]

    def __init__(self, waters, milks, coffee_bean, cup, moneys):
        self.water = waters
        self.milk = milks
        self.coffee_beans = coffee_bean
        self.cups = cup
        self.money = moneys

    def remaining(self):
        water_status = f'{self.water} of water\n'
        milk_status = f'{self.milk} of milk\n'
        beans_status = f'{self.coffee_beans} of coffee beans\n'
        cups_status = f'{self.cups} of disposable cups\n'
        money_status = f'{self.money} of money'
        return print(f'The coffee machine has:\n{water_status}{milk_status}{beans_status}{cups_status}{money_status}')

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:'))
        self.milk += int(input('Write how many ml of milk do you want to add:'))
        self.coffee_beans += int(input('Write how many grams of coffee beans do you want to add:'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:'))

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0
        return None

    def buy(self, menus):
        total = [self.water, self.milk, self.coffee_beans, self.cups, self.money]
        if menus == '1':
            for i in range(0, 5):
                if total[i] - Coffee.espresso[i] >= 0:
                    total[i] -= Coffee.espresso[i]
                    if i == 4:
                        print('I have enough resources, making you a coffee!')
                        self.water = total[0]
                        self.milk = total[1]
                        self.coffee_beans = total[2]
                        self.cups = total[3]
                        self.money = total[4]

                elif total[i] - Coffee.espresso[i] < 0:
                    print('Sorry not enough ' + Coffee.ingredient[i] + '!')
                    break

        elif menus == '2':
            for i in range(0, 5):
                if total[i] - Coffee.latte[i] >= 0:
                    total[i] -= Coffee.latte[i]
                    if i == 4:
                        print('I have enough resources, making you a coffee!')
                        self.water = total[0]
                        self.milk = total[1]
                        self.coffee_beans = total[2]
                        self.cups = total[3]
                        self.money = total[4]
                elif total[i] - Coffee.latte[i] < 0:
                    print('Sorry not enough ' + Coffee.ingredient[i] + '!')
                    break
        elif menus == '3':
            for i in range(0, 5):
                if total[i] - Coffee.cappuccino[i] >= 0:
                    total[i] -= Coffee.cappuccino[i]
                    if i == 4:
                        print('I have enough resources, making you a coffee!')
                        self.water = total[0]
                        self.milk = total[1]
                        self.coffee_beans = total[2]
                        self.cups = total[3]
                        self.money = total[4]
                elif total[i] - Coffee.cappuccino[i] < 0:
                    print('Sorry not enough ' + Coffee.ingredient[i] + '!')
                    break


# Loop for application
water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550
start = Coffee(water, milk, coffee_beans, cups, money)

while True:
    act = input('Write action (buy, fill, take, remaining, exit):')
    if act == 'exit':
        break
    else:
        if act == 'buy':
            menu = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            if menu == 'back':
                continue
            else:
                start.buy(menu)
        elif act == 'fill':
            start.fill()
        elif act == 'take':
            start.take()
        elif act == 'remaining':
            start.remaining()
