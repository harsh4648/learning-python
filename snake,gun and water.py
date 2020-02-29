import random
lst=['s','w','g']
print(" \t \t \t \t Snake,Water,Gun Game\n \n")
print("s for snake \nw for water \ng for gun \n")
no_of_chances=0
chances=10
computer_wins=0
player_wins=0
while no_of_chances < chances:
     _input=input('snake,water,gun:')
     _random= random.choice(lst)
     if _random== _input:
        print("tie")
     elif _input=='s' and _random=='g':
        print(f"computer guesss {_random} and player guest { _input}")
        computer_wins=computer_wins + 1
        print("computer wins\n")
        print(f"computer_point is {computer_wins} and player_point is {player_wins}")     
     elif _input=='s' and _random=='w':
        print(f"computer guesss {_random} and player guest { _input}\n")
        human_wins=human_wins + 1
        print("human wins\n")
        print(f"computer_point is {computer_wins} and player_point is {player_wins}")     
     elif _input=='w' and _random=='s':
        print(f"computer guesss {_random} and player guest{ _input}\n")
        computer_wins=computer_wins + 1
        print("computer wins\n")
        print(f"computer_point is {computer_wins} and player_point is {player_wins}")
     elif _input=='w' and _random=='g':
        print(f"computer guesss {_random} and player guest { _input}\n")
        human_wins=human_wins + 1
        print("human wins\n")
        print(f"computer_point is {computer_wins} and player_point is {player_wins}")   
     elif _input=='g' and _random=='s':
        print(f"computer guesss {_random} and player guest{ _input}\n")
        human_wins=human_wins + 1
        print("human wins\n")
        print(f"computer_point is {computer_wins} and player_point is {player_wins}")       
    
     elif _input=='g' and _random=='w':
        print(f"computer guesss {_random} and player guest{ _input}\n")
        computer_wins=computer_wins + 1
        print("computer wins\n")
        print(f"computer_point is {computer_wins} and player_point is {player_wins}") 
     else:
        print("u enter wronf _input\n")
     no_of_chances = no_of_chances + 1
     print(f"{chances - no_of_chances} is left out {chances}")

print("game over\n")
if computer_wins==player_wins:
    print("tie")
    
    
         
