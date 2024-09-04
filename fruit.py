import random

# list of fruits 
fruits = ["papyaa","mango","guava","blueberry"]
random_fruit = random.choice(fruits)
list_of_alphabet = []

# total 6 chances to play
lives = 6

for alpha in random_fruit:
    list_of_alphabet.append("_")
print(list_of_alphabet)  

while True:

    # Informing the player about chances left
    print(f"you have {lives} chances play it safe")

    # Asking the user to enter an alphabet     
    ask = input("choose an alphabet :").lower()


    for i in range(len(random_fruit)):
        if ask == random_fruit[i]:       
            list_of_alphabet[i] = ask
    
    print(list_of_alphabet) 


# Ensuring every time user enters alphabet chances reduced by 1    
    lives -= 1
    if lives == 0 and "_" in list_of_alphabet:
        print("you lose")
        False
        break

# Ensuring if all the alphabats are correctly founded to end the game
    if "_" not in list_of_alphabet :
        print("you win")
        False
        break
        


    
