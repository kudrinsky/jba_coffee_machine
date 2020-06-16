class CoffeeMachine:
    supply_names = ['water', 'milk', 'coffee beans', 'disposable cups']
    recipe = [[], [250, 0, 16, 1, 4], [350, 75, 20, 1, 7], [200, 100, 12, 1, 6]]
    not_enough = ''
    messages = ['Write action (buy, fill, take, remaining, exit):',
                'The coffee machine has:',
                'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:',
                'Write how many ml of water do you want to add:',
                'Write how many ml of milk do you want to add:',
                'Write how many grams of coffee beans do you want to add:',
                'Write how many disposable cups of coffee do you want to add:',
                'I have enough resources, making you a coffee!']

    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.supply = [water, milk, coffee_beans, disposable_cups, money]
        self.status = None
        self.action(self.messages[0])

    def action(self, string):
        print(string)
        action = input()
        if action == 'exit':
            pass
        else:
            self.logic(action)

    def remaining(self):
        print()
        print(self.messages[1])
        print(f'{self.supply[0]} of water')
        print(f'{self.supply[1]} of milk')
        print(f'{self.supply[2]} of coffee beans')
        print(f'{self.supply[3]} of disposable cups')
        print(f'${self.supply[4]} of money')
        print()
        self.action(self.messages[0])

    def take(self):
        print()
        print(f'I gave you ${self.supply[4]}')
        print()
        self.supply[4] = 0
        self.action(self.messages[0])

    def fill(self, amount=0):

        if self.status > -1:
            self.supply[self.status] += abs(int(amount))
        self.status += 1
        if self.status < 4:
            self.action(self.messages[self.status + 3])
        else:
            self.status = None
            print()
            self.action(self.messages[0])

    def buy(self, coffee):
        for i in range(4):
            if self.supply[i] < self.recipe[abs(int(coffee))][i]:
                if len(self.not_enough) > 0:
                    self.not_enough += ', ' + self.supply_names[i]
                else:
                    self.not_enough += self.supply_names[i]
        if self.not_enough == '':
            print(self.messages[7])
            for i in range(4):
                self.supply[i] -= self.recipe[abs(int(coffee))][i]
            self.supply[4] += self.recipe[abs(int(coffee))][4]
        else:
            print(f'Sorry, not enough {self.not_enough}!')
        print()
        self.not_enough = ''
        self.status = None
        self.action(self.messages[0])

    def logic(self, action):
        if action == 'buy':
            self.status = 6
            print()
            self.action(self.messages[2])
        elif action == 'fill':
            print()
            self.status = -1
            self.fill()
        elif action == 'take':
            self.take()
        elif action == 'remaining':
            self.remaining()
        elif action == 'back':
            self.action(self.messages[0])
        elif self.status == 6:
            self.buy(action)
        elif self.status in range(4):
            self.fill(action)


tefal = CoffeeMachine(400, 540, 120, 9, 550)
