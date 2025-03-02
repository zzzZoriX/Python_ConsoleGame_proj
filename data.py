# статы врага #
enemy_hp: float = 50
enemy_damage: float = 10
enemy_atack_chance: float = 0.5
enemy_defends_chance: float = 0.5
enemy_absorbed_damage_proc: float = 0.55
drops_money: int = 10

# статы игрока #
player_hp: float = 100
player_damage: float = 5.0
player_absorbed_damage_proc: float = 0.5
player_energy: int = 10

player_balance: int = 0
player_exp: int = 1

player_attack_energy_cost: int = 2
player_defends_energy_cost: int = 1
energy_per_round: int = 1

player_actions = [
    "attack",
    "check stats",
    "inventory",
    "skip",
    "exit"
]

player_stats = [
    player_hp,
    player_damage,
    player_energy,
    player_absorbed_damage_proc,
    player_attack_energy_cost,
    player_defends_energy_cost,
    player_balance,
    player_exp
]