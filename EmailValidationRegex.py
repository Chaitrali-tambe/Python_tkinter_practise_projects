""" eg::::> chaitralitambe30@gmail.com
    Conditions for email validation
    Condition 1: a-z lower case alphabets
    Condition 2: 0-9 digits may present
    Condition 3: "." and "_" can be used only once
    Condition 4: "@" can be used only once
    Condition 5: "." position should be at second or third position from right

    Symbols used for the email regex::::>
        ^  =>
        []=> Passing range 
        a-z => range of lower case aphabets a-z
        0-9 => range of numbers 0-9
        +   => joining the two conditions
        \   => Searching character in string
        \._ => In this case searching character "." or "_" in string
        ?   => In this case it validates to check whether "." or "_" are appearing only once
               works on 0-1 
        \w  => searches character
        {2,3}  => giving condition to find dot position at 2nd or 3rd psoition from right
        $ => used to search string from last position

"""
import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter your email: ")

if re.search(email_condition, user_email):
    print ("Right Email")

else:
    print("Wrong Email")

