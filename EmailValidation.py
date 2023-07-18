# eg:::> g@g.in
# condition 1: atleast 6 characters
# condition 2: first letter should only be alphabet
# condition 3: only 1 @ should be present
# condition 4: "." should be present at the fourthlast, thirdlast or secondlast position
# condition 5: a) should not condain white space
#              b) should not have uppercase character
#              c) only symbols like "#" "." and "_" should be present
# if these above conditions are satisfied, then the email entered is valid else it's not

email = input("Enter your email: ") 
k,j,d = 0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]==".") ^ (email[-2]=="."):
                for i in email:
                    if i.isspace() == True:
                        k = 1
                    
                    elif i.isalpha():
                        if i==i.upper(): 
                            j = 1
                    
                    elif i.isdigit():
                        continue

                    elif (i=="_") or (i==".") or (i=="@"):
                        continue
                    
                    else:
                        d = 1
                       

                if k==1 or j==1 or d==1:
                    print("Wrong email (by condition 5)")
                else:
                    print("Right email")

            else:
                print("Wrong email (by condition 4)")

        else:
            print("Wrong email (by condition 3)")

    else:
        print("wrong Email (by contition 2)")

else:
    print("Wrong email (By condition 1)")