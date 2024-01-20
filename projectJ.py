import random
print("Want To Play The Hand Cricket Game....")
No_of_players=int(input("Enter The No. Of Players...="))
if No_of_players==1:
    Player=input("Enter The Name Of Player..=")
    Print1="""Welcome... {}!! Nice to see you here...Ready to test your luck..."""
    Print1= Print1.format(Player)
    print(Print1)
    print("So , Let The Game Be Started....And Computer Will Be Your Default Second Player...First You Have To Choose (Odd Or Even) For The Toss Between The Two Teams...")
    even_odd=input("Enter Your Choice...=")
    even_odd=even_odd.lower()
    if even_odd=="even":
        Toss_User1="even"
        Toss_Comp="odd"
        print("Choose a Number Of Your Choice From The Following Gievn Numbers-")
        Numbers=[1,2,3,4,5,6]
        print(Numbers)
        Toss_numberU=int(input("Enter The Number You Choiced"))
        if Toss_numberU>=1 and Toss_numberU<=6:
            Toss_numberC=random.choice(Numbers)
            sum_of_numbers=Toss_numberU+Toss_numberC
            if sum_of_numbers%2 ==0:
                print("Congratulations You Win The Toss")
                print("Now You Have to Opt Between Batting or Balling")
                User_Bat_ball= input("Enter Your choice..=")
                User_Bat_ball=User_Bat_ball.lower()
                if User_Bat_ball=="batting":
                    print("Now The Rules Very Simple...You Just Have To Choose One Number From 1 To 6...and The Computer Will Do The Same..and Choose One Random Number From These Numbers...and If The Number Chosen By You And The Computer Are Same...You Will Be Declared Out...Otherwise The No. Chosen By You Will Be Added To Your Total_Score...So Lets Begin...!!")
                    def BattingU():
                        Player_score=0
                        User_no=int(input("Enter The No. Of Your Choice...="))
                        Numbers=[1,2,3,4,5,6]
                        Comp_no=random.choice(Numbers)
                        print(User_no,Comp_no)
                        if User_no==Comp_no:
                            out="""Oops..You Are Out...Its The Time For Computer To Bat...And To Win Computer Have To Make {}"""
                            out=out.format(Player_score+1)
                            print(out)
                            def BowlingU():
                                Comp_score=0
                                comp_no=random.choice(Numbers)
                                User_no=int(input("Enter The NO. Of Your Choice...="))
                                if User_no==Comp_no:
                                    print("Congrats...Computer Got Out...You Win The Game....hurrryyy....")
                                else:
                                    Comp_score+=Comp_no    
                                    print("The Score Of Computer is",Comp_score)
                                    BowlingU()
                            BowlingU()        
                        else:
                            Player_score+=User_no
                            print(Player_score)
                            BattingU()
                    BattingU()        
            else:
                print("Oopss...You Lose The Toss...")    
                print("Computer Win The Toss")
                print("Now Computer Will Opt Between Bating or Balling")
                List=[1,2]
                Comp_bat_ball=random.choice(List)
                if Comp_bat_ball==1:
                    print("Computer Has Choosed To Bat First...")
                    print("Now The Rules Are Very Simple... The Computer Will Choose One Random Number From Numbers 1 To 6...and Also You Have To Choose One Number From These Six Numbers...andand If The Number Chosen By You And The Computer Are Same...So, Computer Will Be Declared Out...Otherwise The No. Chosen By Computer Will Be Added To Computer's Total_Score...So Lets Begin...!!")
                    def BattingC():
                        Comp_score=0
                        Comp_no=random.choice(Numbers)
                        User_no=int(input("Enter The No. Of Your Choice...="))
                        if User_no==Comp_no:
                            print("Luckly..Computer IS Out...Its The Time For You To Bat...")
                            def BattingU2():
                                Player_score=0
                                User_no=int(input("Enter The No. Of Your Choice...="))
                                Numbers=[1,2,3,4,5,6]
                                Comp_no=random.choice(Numbers)
                                if User_no==Comp_no:
                                    print("oops..you are out")
                                else:
                                    Player_score+=User_no
                                    print("your score is"+Player_score)
                                    BattingU2()
                            BattingU2()
                                
                        else:
                            Comp_score+=User_no
                            print(Comp_score)
                            BattingC() 
                    BattingC() 
                elif Comp_bat_ball==2:
                    print("Computer Has Choosed To Bowl First...")
                    def BowlingC():
                        Player_score=0
                        User_no=int(input("Enter The No. Of Your Choice...="))
                        Comp_no=random.choice(Numbers)
                        if User_no==Comp_no:
                            print("Oops..You Are Out...Its The Time For You To Bowl...")
                        else:
                            Player_score=User_no
                            print(Player_score)
                            BowlingC() 
                    BowlingC()



    elif even_odd=="odd":
        Toss_User1="odd"
        Toss_Comp="even"
        print("Choose a Number Of Your Choice From The Following Gievn Numbers-")
        Numbers=[1,2,3,4,5,6]
        print(Numbers)
        Toss_numberU=int(input("Enter The Number You Choiced"))
        print(Toss_numberU)
        if Toss_numberU>=1 and Toss_numberU<=6:
            Toss_numberC=random.choice(Numbers)
            sum_of_numbers=Toss_numberU+Toss_numberC
            if sum_of_numbers%2 !=0:
                print("Congratulations You Win The Toss")
                print("Now You Have to Opt Between Batting or Balling")
                User_Bat_ball= input("Enter Your choice..=")
                User_Bat_ball=User_Bat_ball.lower()
                if User_Bat_ball=="batting":
                    print("Now The Rules Very Simple...You Just Have To Choose One Number From 1 To 6...and The Computer Will Do The Same..and Choose One Random Number From These Numbers...and If The Number Chosen By You And The Computer Are Same...You Will Be Declared Out...Otherwise The No. Chosen By You Will Be Added To Your Total_Score...So Lets Begin...!!")
                    def BattingU():
                        Player_score=0
                        User_no=int(input("Enter The No. Of Your Choice...="))
                        Numbers=[1,2,3,4,5,6]
                        Comp_no=random.choice(Numbers)
                        
                        if User_no==Comp_no:
                            out="""Oops..You Are Out...Its The Time For Computer To Bat...And To Win Computer Have To Make {}"""
                            out=out.format(Player_score+1)
                            print(out)
                            def BowlingU():
                                Comp_score=0
                                Comp_no=random.choice(Numbers)
                                User_no=int(input("Enter The NO. Of Your Choice...="))
                                if User_no==Comp_no:
                                    print("Congrats...Computer Got Out...You Win The Game....hurrryyy....")
                                else:
                                    Comp_score+=Comp_no    
                                    print("The Score Of Computer is",Comp_score)
                                    BowlingU()
                                    
                            BowlingU()        
                        else:
                            Player_score+=User_no
                            print(Player_score)
                            BattingU()
                    BattingU()

    else:
        print("Please Enter a Valid Option...")    

elif No_of_players==2:
    Player1=input("Enter The Name Of Player 1..=")
    Player2=input("Enter The Name Of Player 2..=")
    Print1="""Welcome... {}!! & {}!! Nice to see you guys here...Ready to test your luck..."""
    Print1= Print1.format(Player1,Player2)
    print(Print1)
else:
    print("A Maximum Of Just Two Players Can Play This Game....Sorry.. ")    


