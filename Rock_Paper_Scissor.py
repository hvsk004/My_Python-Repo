import random
list=["Rock","Paper","Scissor"]
User_input=input("Enter Rock,Paper or Scissor :")
computer_choice=random.choice(list)
print(computer_choice)
if(User_input==list[0]):
    if(computer_choice==list[2]):
     print("The computer Choice is :",computer_choice)
     print("Congratulations You Win")
    elif(computer_choice==list[1]):
         print("The computer Choice is :",computer_choice)
         print("You lost try again")
    elif(computer_choice==User_input):
        print("The computer Choice is :",computer_choice)
        print("Its a draw Try again")
    else:
        print("Enter a valid Choice")
if(User_input==list[1]):
    if(computer_choice==list[0]):
         print("The computer Choice is :",computer_choice)
         print("Congratulations You Win")
    elif(computer_choice==list[2]):
         print("The computer Choice is :",computer_choice)
         print("You lost try again")
    elif(computer_choice==User_input):
        print("The computer Choice is :",computer_choice)
        print("Its a draw Try again")
    else:
        print("Enter a valid Choice")
if(User_input==list[2]):
    if(computer_choice==list[1]):
         print("The computer Choice is :",computer_choice)
         print("Congratulations You Win")
    elif(computer_choice==list[0]):
         print("The computer Choice is :",computer_choice)
         print("You lost try again")
    elif(computer_choice==User_input):
        print("The computer Choice is :",computer_choice)
        print("Its a draw Try again")
    else:
        print("Enter a valid Choice")