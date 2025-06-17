import random
choices=["rock","papper","scissor"]
chances=5
User_score=0 
Comp_score=0 
print("Hi, Welcome to Rock Papper Scissor Game:\nNo of chances You got is five.\n")
while(chances!=0):
   user_input=input("Rock Papper Scissor ?").lower()
   comp_choice=random.choice(choices)
   print("\nComp: ",comp_choice, "\nUser: ", user_input,"\n")
   if comp_choice==user_input:
       continue
   elif(comp_choice=="papper" and user_input=="scissor"):
       User_score+=1
   elif(comp_choice=="scissor" and user_input=="papper"):
       Comp_score+=1
   elif(comp_choice=="rock" and user_input=="scissor"):
       Comp_score+=1
   elif(comp_choice=="scissor" and user_input=="rock"):
       User_score+=1
   elif(comp_choice=="rock" and user_input=="papper"):
       User_score+=1
   elif(comp_choice=="papper" and user_input=="rock"):
       Comp_score+=1
   else:
       print("Enter Correct choices!! \n")
   print("Comp score : ",Comp_score, " User score: ",User_score,"\n")
   chances-=1    
if(User_score>Comp_score):
    print("\n User wins")
elif(User_score==Comp_score):
    print("\n Draw")
else:
    print("\n Computer Wins")
