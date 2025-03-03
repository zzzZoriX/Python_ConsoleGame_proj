import data, shop, game_main as gm

inventory = []
size = 10

def show_inventory():
    if(len(inventory)):
        print()
        for item in range(0, len(inventory)):
            print(f" {item + 1}: {inventory[item]}")
        print(f" {len(inventory)} / {size}\n")
    else:
        print("инвентарь пуст\n")
        
def use_item():
    print("хотите что-то использовать?")
    answ = input("(Y / N): ").upper()
    
    if(answ == 'Y' and gm.item_was_used == 0.0):
        print("введите номер предмета")
        index = int(input('> ')) - 1
        
        item = inventory[index]
        inventory.pop(index)
        
        if(item == 'хп бустер'): hp_buster()
        elif(item == 'дамаг бустер'): damage_buster()
        elif(item == 'мана бустер'): energy_buster()
    
    elif(answ == 'Y' and gm.item_was_used == 1.0):
        print("вы уже использовали предмет в этом бою")

def hp_buster():
    data.player_stats[1] += float(int(data.player_stats[1] * shop.shop_items[0]))
    
def damage_buster():
    data.player_stats[0] += float(int(data.player_stats[1] * shop.shop_items[1]))
    
def energy_buster():
    data.player_stats[4] += float(int(data.player_stats[4] * shop.shop_items[2]))