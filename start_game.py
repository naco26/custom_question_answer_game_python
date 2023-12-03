#importing necessary libraries
import random
import json

class Start_game:
    def start__game():
        print("Ques-Ans Game Start...")

        #initalizing variables
        Ques_Ans = [] #Questionnaire for this game
        score=0 # our participant score
        asked_q=[]  #list to maintain asked question
        want_to_play=True #after every question check if user wants to continue or exit

        #reading file content, adding it to our json, and closing file
        with open('Ques_Ans.txt','r') as f:
            [Ques_Ans.append(json.loads(line.strip())) for line in f.readlines()]
        f.close()

        #Generating a random number
        random_no = random.randint(0, len(Ques_Ans)-1)

        #Game start
        print("WELCOME TO QUESTIONARRIE GAME")

        #Ending if all questions are asked or user quits
        while len(asked_q)!=len(Ques_Ans) and want_to_play:

            #generating random num that has not been asked 
            while random_no  in asked_q :
                random_no = random.randint(0, len(Ques_Ans)-1)

            #adding that to asked question list
            asked_q.append(random_no)
            print("Your Question is:",Ques_Ans[random_no][0])

            #Taking user response to the ques
            ans = input("Enter your answer:")
            C_ans = Ques_Ans[random_no][1]

            #adding score if answer matches
            if ans.lower() == C_ans.lower():
                score+=1
            
            #if all questions are asked, end the game
            if len(asked_q)==len(Ques_Ans):
                break

            #taking user consent for continuing the game
            want_to_play = input("Enter 'Exit' to exit or press any key to continue").lower()!="exit"

        #print score
        print("Thanks for playing!! Your score is:",score)




