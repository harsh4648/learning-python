n=100
number_of_guesses=1
print("number of guesses limited to 9 times:")
while (number_of_guesses<=9):
    guess_number = int(input("guess the number:\n"))
    if guess_number<100:
        print("u enter lesser number")
    elif guess_number>100:
        print("u enter greater number")
    else:
        print("you have won\n")
        print(number_of_guesses,"no. of guesses taken to finish" )
        break
    print(9-number_of_guesses,"no of guesses left")
    number_of_guesses = number_of_guesses+1
if(number_of_guesses>9):
    print("game over")    

    


