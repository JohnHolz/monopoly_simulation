from numpy.random import randint

class Player():
    def __init__(self, name, money=31, position = 1):
        self.position = position
        self.money = money
        self.play_next_round = True
        self.name = name
    
    def __repr__(self):
        ret =  f"""
        name:{self.name}
        money:{self.money}
        position:{self.position}
        next round:{self.play_next_round}"""
        return ret

    def __len__(self):
        return self.position

    def update_money(self, int):
        self.money = self.money+int
        
    def update_position(self, int):
        self.position = int
        
    def roll_dice(self, die = 6):
        self.position = (self.position+randint(die)+1)%33
        
    def not_play_next_round(self):
        self.play_next_round = False

    def to_dict(self):
        ret = dict()
        ret['position'] = self.position
        ret['money'] = self.money
        ret['play_next_round'] = self.play_next_round
        ret['name'] = self.name
        return ret
    