import data

# действия игрока #
def player_attack():
    if(data.player_stats[4] >= data.player_stats[7]):
        data.enemy_stats[1] -= data.player_stats[0]
        data.player_stats[4] -= data.player_stats[7]
        print("\nвы атаковали")
    
    else: print("\nнедостаточно энергии")
    
def player_defends():
    if(data.player_stats[4] >= data.player_stats[6]):
        data.player_stats[1] += data.enemy_stats[0] * data.player_stats[5]
        data.player_stats[4] -= data.player_stats[6]
        print("вы защитились\n")
        
    else: print("недостаточно энергии")