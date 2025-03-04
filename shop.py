import data, inventory as inv

shop_items = [
    0.5,    # хп бустер
    0.5,    # дамаг бустер
    1       # мана бустер
]

shop_items_cost = [
    10,     # хп
    20,     # урон
    15      # мана
]

def print_shop():
    print(f"\n  хп бустер - {shop_items_cost[0]} монет\n  дамаг бустер - {shop_items_cost[1]} монет\n  мана бустер - {shop_items_cost[2]} монет\n")


def buy_item():
    print("выберите предмет для покупки:\n 1 - хп бустер\n 2 - дамаг бустер\n 3 - мана бустер\n -1 - выход")
    choice = int(input('> '))
    
    if(choice == -1): return
    
    print("кол-во покупаемого товара")
    count = int(input('> '))
    
    cost = 0
    
    if(choice == 1):
        cost = shop_items_cost[choice - 1] * count
        
        while(count > 0 and inv.size > len(inv.inventory)):
            inv.inventory.append("хп бустер")
            count -= 1
        
    elif(choice == 2):
        cost = shop_items_cost[choice - 1] * count
        
        while(count > 0 and inv.size > len(inv.inventory)):
            inv.inventory.append("дамаг бустер")
            count -= 1
        
    elif(choice == 3):
        cost = shop_items_cost[choice - 1] * count
        
        while(count > 0 and inv.size > len(inv.inventory)):
            inv.inventory.append("мана бустер")
            count -= 1
        
    else:
        print("неизвесный товар")
        return
    
    
    if(data.player_stats[2] < cost):
            print("недостаточно монет")
            return
        
    data.player_stats[2] -= cost