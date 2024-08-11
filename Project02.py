import random

# Write a program that generates a random number and asks the user to guess it.
# If the players guess is higher than the actual number,the program displays "lower number please".
# Similarly if the users guess is too low , the program prints "higher number please"
# when the user guesses the correct number , the program displays the number of guesses the player used 
# to arrive at the number. 

n = random.randint(1, 100) 
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the number: ")) 
    if(a >n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number Please")
        guesses +=1

print(f"You have guessed the number {n} correctly in {guesses} attempts")

