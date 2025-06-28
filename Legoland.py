print("This is my legoland game")
character = input ("Legoland is a game where you can collect points by building legos and coins. What is your name?")
print("You are in a beautiful land of Legos.")
print("You can win by collecting points.")
print("You can collect points by building legos and coins.")
print("legos = 5 points and coins = 10 points")
print("how many legos do you have?")
legos = int(input("Enter the number of legos you have: "))
print("how many coins do you have?")
coins = int(input("Enter the number of coins  you have: "))
total_points = (legos * 5) + (coins * 10)
print("You have a total of " + str(total_points) + " points.")
if total_points >= 500:
        print("Congratulations " + character + "! You have won the game with " + str(total_points) + " points!")
        print("You have achieved the minimun points required to win the game, you have won the game!")
        if continue_playing.lower() == "yes": 
            print("Great! Keep building and collecting points!")
else: 
    if total_points <= 500 and total_points >= 1000:
        print("Congratulations " + character + "! You have won the game with " + str(total_points) + " points!")
        print("You have achieved the minimun points required to win the game, would you like to continue playing to increase your score? (yes/no)")
        continue_playing = input("Enter your choice: ")
        if continue_playing.lower() == "yes":
            print("Great! Keep building and collecting points!")
        else:  
            print("Thank you for playing Legoland, " + character + "!")
            print("Goodbye!")
print("Sorry " + character + ", you need at least 500 points to win. You have " + str(total_points) + " points.")
print("Thank you for playing Legoland, " + character + "!")
print("Goodbye!")
