import random

choices = ['Rock', 'Paper', 'Scissors']

while True:
    CPU_player = random.choice(choices)
    player_choice = None

    while player_choice not in choices:
        player_choice = input("rock, paper or scissors: ").title()


    if CPU_player == player_choice:
        print("computer: ",CPU_player)
        print("player: ", player_choice)
        print("Tie!")

    elif player_choice == 'Rock': 
        if CPU_player == 'Scissors':
            print("computer: ",CPU_player)
            print("player: ", player_choice)
            print("You won!")
        if CPU_player == 'Paper':
            print("computer: ",CPU_player)
            print("player: ", player_choice)
            print("You lose!")

    elif player_choice == 'Paper': 
        if CPU_player == 'Rock':
            print("computer: ",CPU_player)
            print("player: ", player_choice)
            print("You won!")
        if CPU_player == 'Scissors':
            print("computer: ",CPU_player)
            print("player: ", player_choice)
            print("You lose!")

    elif player_choice == 'Scissors': 
        if CPU_player == 'Paper':
            print("computer: ",CPU_player)
            print("player: ", player_choice)
            print("You won!")
        if CPU_player == 'Rock':
            print("computer: ",CPU_player)
            print("player: ", player_choice)
            print("You lose!")

    play_again = input("Play again? (yes/no): ")

    if play_again!= 'yes':
        break

print('Bye!')
# for item in alist:
