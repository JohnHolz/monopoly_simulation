import sys
sys.path.append('../')
from modules.tabuleiro import tabuleiro

def rodada(player):
    """
    ! 1. Verificar se o player pode jogar
    ! 2. o player vai rodar os dados
    ! 3. o player vai executar a ação da casa que ele parou
    !    Se parou numa casa sem dono -> comprar a casa
    !    Se parou numa casa com dodo -> pagar o valor para o dono
    !    Se a casa não é propriedade outros ...
    """
    if player.play_next_round == False:
        return
    
    player.roll_dice()

    ## TODO tabuleiro(player)
    ## TODO verificar a casa que parou e executar a ação