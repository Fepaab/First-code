warrior_money = 450.0
master_sword = 150.0
mana_potion = 100.0
healers_potion = 75.0

resposta = input("Good night warrior, would like to buy something? Y/N: ")
if resposta == "Y":
    print("Here it is the name and the prices os the products")
    
    print("1 - Master Sword: $", master_sword)
    print("2 - Mana Potion: $", mana_potion)
    print("3 - Healer's Potion: $", healers_potion)
    print("Money available: $", warrior_money)

elif resposta == "N":
    print("Ok though, Good bye and Good Night :D")

troco = 0.0

warrior_choise = int(input("Choose your item: "))

if (warrior_choise == 1):
    print("You choose the Master Sword")
    warrior_money -= master_sword
    print(f"You have ${warrior_money} left")

elif (warrior_choise == 2):
    print("You choose the Mana Potion")
    warrior_money -= mana_potion
    print(f"You have ${warrior_money} left")

elif (warrior_choise == 3):
    print("You choose the Healer's Potion")
    warrior_money -= healers_potion
    print(f"You have ${warrior_money} left")