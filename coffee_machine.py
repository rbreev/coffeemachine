class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def remaining(self):
        print(f'The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')

    def take(self):
        print(f'I gave you ${self.money}')
        self.money -= self.money

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:'))
        self.milk += int(input('Write how many ml of milk do you want to add:'))
        self.beans += int(input('Write how many grams of coffee beans do you want to add:'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:'))

    def buy(self):
        t = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if t == "back":
            return
        # espresso = 250 ml of water and 16 g of coffee beans. It costs $4.
        elif t == "1" and self.water >= 250 and self.beans >= 16 and self.cups >= 1:
            print('I have enough resources, making you a coffee!')
            self.water -= 250
            self.beans -= 16
            self.money += 4
            self.cups -= 1
        # latte = 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7
        elif t == "2" and self.water >= 350 and self.beans >= 20 and self.milk >= 75 and self.cups >= 1:
            print('I have enough resources, making you a coffee!')
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.money += 7
            self.cups -= 1
        # cappuccino = 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6
        elif t == "3" and self.water >= 200 and self.beans >= 12 and self.milk >= 100 and self.cups >= 1:
            print('I have enough resources, making you a coffee!')
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.money += 6
            self.cups -= 1
        else:
            print('Sorry, not enough water!')

    def work(self):
        action = input('Write action (buy, fill, take, remaining, exit):')
        while action != "exit":
            if action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'buy':
                self.buy()
            elif action == 'remaining':
                self.remaining()
            self.work()
        exit()


machine = CoffeeMachine(400, 540, 120, 9, 550)
machine.work()
