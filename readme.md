# Monopoly Simulation
Teaching my friends python redoing the final test of Computational Statistics 2.

---
## The Problem
Simulate N monopoly games with 2 players, save general information about the game and then make an inference about the relation of the information collect and the winner of the game.


# Jogo Monopoly

    condition = True
    i = 0
    while(condition):
    #     <RODADA>
    #     for i in [gabriel, brenda, joao]:
    #         if i.play_next_round:
    #         function(player)
    #             i.roll_dice
    #             tabuleiro[str(i.position)](i)
    #         else:
    #             i.play_next_round = True
    #     <FIM DA RODADA>
        i+=1
        if i>10_000:
            print(i)
            break

#### João Paulo de Paiva Holz
1. 2 Players vão jogar
1. Players possuem:
    1. dinheiro
    2. posição
    3. forma de alterar o dinheiro
    4. forma de alterar posição
    5. alterar posição rolando o dado
1. jogo possui 20 casas:
    Nr|Casa|Efeito
    ---|---|---
    1|go|money +2
    2|chance|card
    3|ballon stand|propriedade 1/1
    4|corron stand|propriedade 1/1
    5|chance|card
    6|yello line railroad|roll dice again
    7|puppet show| propriedade 2/2
    8|magic show| propriedade 2/2
    9|fireworks| money -2
    10|chance|card
    11|rest rooms| 1 round withou play
    12|merry-go round| propriedade 2/2
    13|paddle boats| propriedade 2/2
    14|green line railroad| roll dice again
    15|water slide| propriedade 3/3
    16|mini golf| propriedade 3/3
    17|uncle pennybags| money +3
    18|chance| card
    19|video arcade| propriedade 3/3
    20|haunted house| propriedade 3/3
    21|chance| card
    22|blue line railroad| roll dice again
    23|helicopter ride| propriedade 4/4
    24|pony ride| propriedade 4/4
    25|water show| money -2
    26|chance|card
    27|tremway to rest rooms| go to 11 (rest room)
    28|bumber cars| propriedade 4/4
    29|ferris wheel| propriedade 4/4
    30|red line railroad| roll dice again
    31|loop the loop| propriedade 5/5
    32|roller coaster| propriedade 5/5