from numpy.random import randint
from propriedades import propriedades

def card(player):
    if randint(2)==True:
        player.update_money(2)
    else:
        player.update_money(-2)

def update_money(value):
    def output_function(player):
        player.update_money(value)
    return output_function

def stop_propriedade(player):
    number = player.position
    # valores da propriedadde
    owner = propriedades[number]['owner']
    price = propriedades[number]['price']
    pay   = propriedades[number]['pay']
    
    if  owner == None:
        ## 1. checar se já tem dono
        player.update_money(-price)
        propriedades[number]['owner'] = player.player_name
        return
    elif owner == player.player_name:
        return
    else:
        eval(owner).update_money(+pay)
        player.update_money(-pay)
        return

def next_round_without_play(player):
    player.play_next_round = False

def play_round(player):
    player.roll_dice
    tabuleiro[str(player.position)](player)

tabuleiro = dict()
tabuleiro['1'] = update_money(+2)
tabuleiro['2'] = card
tabuleiro['3'] = stop_propriedade
tabuleiro['4'] = stop_propriedade
tabuleiro['5'] = card
tabuleiro['6'] = play_round
tabuleiro['7'] = stop_propriedade
tabuleiro['8'] = stop_propriedade
tabuleiro['9'] = update_money(-2)
tabuleiro['10'] = card
tabuleiro['11'] = next_round_without_play
tabuleiro['12'] = stop_propriedade
tabuleiro['13'] = stop_propriedade
tabuleiro['14'] = play_round
tabuleiro['15'] = stop_propriedade
tabuleiro['16'] = stop_propriedade
tabuleiro['17'] = update_money(+3)
tabuleiro['18'] = card
tabuleiro['19'] = stop_propriedade
tabuleiro['20'] = stop_propriedade
tabuleiro['21'] = card
tabuleiro['22'] = play_round
tabuleiro['23'] = stop_propriedade
tabuleiro['24'] = stop_propriedade
tabuleiro['25'] = update_money(-2)
tabuleiro['26'] = card
tabuleiro['27'] = next_round_without_play
tabuleiro['28'] = stop_propriedade
tabuleiro['29'] = stop_propriedade
tabuleiro['30'] = play_round
tabuleiro['31'] = stop_propriedade
tabuleiro['32'] = stop_propriedade
