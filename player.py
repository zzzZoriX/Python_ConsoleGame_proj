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
    
def lvl_up():
    data.player_stats[4] += 1
    data.player_stats[9] -= data.player_stats[8]
    
    print("что улучшить?\n 1 - хп\n 2 - урон\n 3 - энергию")
    choice = int(input("> "))
    if(choice == 1):
        data.player_stats[1] = float(int(data.player_stats[1] * data.hp_multi_per_lvl))
    
    elif(choice == 2):
        data.player_stats[0] = float(int(data.player_stats[0] * data.damage_multi_per_lvl))
        
    elif(choice == 3):
        data.player_stats[4] = float(int(data.player_stats[4] * data.energy_multi_per_lvl))