import data

# действия игрока #
def player_attack():
    if(data.player_energy >= data.player_attack_energy_cost):
        data.enemy_hp -= data.player_damage
        data.player_energy -= data.player_attack_energy_cost
        print("\nвы атаковали")
    
    else: print("\nнедостаточно энергии")
    
def player_defends():
    if(data.player_energy >= data.player_defends_energy_cost):
        data.player_hp += data.enemy_damage * data.player_absorbed_damage_proc
        data.player_energy -= data.player_defends_energy_cost
        print("вы защитились\n")
        
    else: print("недостаточно энергии")