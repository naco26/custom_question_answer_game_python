from start_game import  Start_game

print("Welcome to the project..")

'''
Taking user input if they want to play game and continuing n times until they hit anything
other than 'yes' or 'y' or '1'
'''
play_game=input("Do you want to play Ques-Ans Game? Type 'yes' or 'y' or '1' : ")
while play_game.lower()=="yes" or play_game.lower()=="y" or play_game.lower()=="1":
    Start_game.start__game()
    play_game=input("Do you want to play Ques-Ans Game Again? Type 'yes' or 'y' or '1' : ")

print("Thank for visiting the project.")

