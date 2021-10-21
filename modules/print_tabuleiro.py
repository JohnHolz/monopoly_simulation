import pandas as pd, numpy as np
tab = pd.read_csv('tabuleiro.csv')

def players_column(players, tab):
    ls = tab.shape[0]*['']
    for i in players:
        space=''
        if ls[i.position-1]!='':
            space = ', '
        ls[i.position-1] = f'{ls[i.position-1]}{space}{i.name}'
    return pd.Series(ls)

def players_position(players,tab):
    tab['players'] = players_column(players,tab)
    return tab

def print_game(players,tab):
    players_info_table = pd.DataFrame(list(map(lambda x: x.to_dict(),players)))
    print(players_info_table[['name','money','position','play_next_round']])
    return players_position(players,tab)