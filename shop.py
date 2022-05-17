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
        for key,value in self.inventory.items():
            print (key,value)
    def bought(self, brokness, product):
        if product in self.inventory:
            if brokness >= self.inventory[product][0]:
                if self.inventory[product][1] >= 1:
                    self.inventory[product][1] -= 1
                    self.funds += self.inventory[product][0]
        else:
            print("We don't carry those.")
    def __init__ (self, Funds, Inventory):
        self.funds = Funds
        self.inventory = Inventory




INVENTORY = {'SmallTv':[350,20], 'Nuclearwaste':[50,50000000000000000000000000000000000]}

jeffsshop = shop(20000000000000000000000000, INVENTORY)



print( "\n" )

jeffsshop.showInventory()

jeffsshop.bought(3000, 'SmallTv')



print( "\n")

jeffsshop.showInventory()

