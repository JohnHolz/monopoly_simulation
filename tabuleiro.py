from numpy.random import randint
from propriedades import propriedades

def card(player):
    if randint(2)==True:
        player.update_money(2)
    else:
        player.update_money(-2)

def func_1(player):
    player.update_money(2)
        
def stop_propriedade(player_name,number):
    # valores da propriedadde
    owner = propriedades[number]['owner']
    price = propriedades[number]['price']
    pay   = propriedades[number]['pay']
    
    if  owner == None:
        ## 1. checar se já tem dono
        eval(player_name).update_money(-price)
        propriedades[number]['owner'] = player_name
        return
    elif owner == player_name:
        return
    else:
        eval(owner).update_money(+pay)
        eval(player_name).update_money(-pay)
        return        

tabuleiro = dict()
tabuleiro['1'] = func_1
tabuleiro['2'] = card
tabuleiro['3'] = stop_propriedade
tabuleiro['4'] = stop_propriedade
tabuleiro['5'] = card
#tabuleiro['6'] = 
tabuleiro['7'] = stop_propriedade
tabuleiro['8'] = stop_propriedade
#tabuleiro['9'] = 
tabuleiro['10'] = card
#tabuleiro['11'] = 
tabuleiro['12'] = stop_propriedade
tabuleiro['13'] = stop_propriedade
#tabuleiro['14'] = 
tabuleiro['15'] = stop_propriedade
tabuleiro['16'] = stop_propriedade
#tabuleiro['17'] = 
tabuleiro['18'] = card
tabuleiro['19'] = stop_propriedade
tabuleiro['20'] = stop_propriedade
tabuleiro['21'] = card
#tabuleiro['22'] = 
tabuleiro['23'] = stop_propriedade
tabuleiro['24'] = stop_propriedade
#tabuleiro['25'] = 
tabuleiro['26'] = card
#tabuleiro['27'] = 
tabuleiro['28'] = stop_propriedade
tabuleiro['29'] = stop_propriedade
#tabuleiro['30'] = 
tabuleiro['31'] = stop_propriedade
tabuleiro['32'] = stop_propriedade
