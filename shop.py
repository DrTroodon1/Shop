class shop:
    
    funds = 0
    inventory = {}

    def getfunds():
        return funds
    def losefunds(self):
        funds -= self
    def gainfunds(self):
        funds += self
    def showInventory(self):
        print("\n")
        for key,value in self.inventory.items():
            print (key,value)
            print("\n")
    def bought(self, brokness, product, amount):
        if brokness >= 0:
            if product in self.inventory:
                if brokness >= self.inventory[product]['Price']*amount:
                    if self.inventory[product]['Amount'] >= amount:
                        self.inventory[product]['Amount'] -= amount
                        self.funds += self.inventory[product]['Price']*amount
                    else:
                        print("We don't have any of those left.")
                else:
                    print("You are to broke to buy that!!!")
            else:
                print("We don't carry those!")
        else:
            print("I am not giving you money!!!!!!")
    def __init__ (self, Funds, Inventory):
        self.funds = Funds
        self.inventory = Inventory








INVENTORY = {'SmallTv':{'Price':350, "Amount":20}, 'Nuclearwaste':{'Price':50, "Amount":5000000000000000000}}

jeffsshop = shop(20000000000000000000000000, INVENTORY)





jeffsshop.showInventory()

print(jeffsshop.funds)

jeffsshop.bought(3000, 'SmallTv', 10)


print(jeffsshop.funds)


jeffsshop.showInventory()

