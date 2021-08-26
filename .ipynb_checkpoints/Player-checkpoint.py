from numpy.random import randint

class Player():
    def __init__(self, money=31, position = 1):
        self.position = position
        self.money = money
            
    def __repr__(self):
        return f"money:{self.money}||position:{self.position}"
    
    def __len__(self):
        return self.position
    
    def update_money(self, int):
        self.money = self.money+int
        
    def update_position(self, int):
        self.position = int
        
    def roll_dice(self, die = 6):
        self.position = (self.position+randint(die)+1)%33
        
        