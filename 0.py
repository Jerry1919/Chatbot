import os

robo = "champ"

print(f"{robo}: Hi.!! I am {robo}, here for you.")
you = input(f"{robo}: What's your user name? : ")

if not os.path.exists(f'{you}.txt'):
    print(f"{robo}: I'm glad that you are here 😊  I assure, you will have great experiance.")
    enteredPassword = input(f"{robo}: Please, Enter password for your new account :")
    f = open(f'{you}.txt','a')
    f.write(f"Password : {enteredPassword}")
    print(f"{robo}: your account has been created successfully.")
    print(f"{robo}: To proceed further please login again.")
    exit

else:
    enteredPassword = input(f"{robo}: Please, Enter your password :")
    f = open(f'{you}.txt','r+')
    f.seek(0)
    lines = f.readlines()
    passwordValue = "aaaa"
    for line in lines:
        Key,value = line.split(" : ")
        if(Key == "Password"):
            passwordValue = value
            break
    if(passwordValue == enteredPassword):
        print(f"{robo}: I'm glad that you are back here again 😊")
    else:
        print(f"{robo}: 'WRONG PASSWORD', please try again")
        exit


