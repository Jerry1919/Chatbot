import os
import random

robo = "champ"
empty = [" ","\t","\n",""]

print(f"{robo}: Hi.!! I am {robo}, here for you.")
print(f"{robo}: What's your user name? ")
user = input(f"user : ")

if not os.path.exists(f'{user}.txt'):
    print(f"{robo}: I'm glad that you are here 😊  I assure, you will have great experiance.")
    print(f"{robo}: {user} Please, Enter password for your new account :")
    enteredPassword = input(f"{user} : ")
    if not(enteredPassword in  empty):
        f = open(f'{user}.txt','a')
        f.write(f"Password : {enteredPassword} : \n")
        for i in range(1,4):
            print(f"{robo}: What do you want to call me :")
            robo = input(f"{user} : ")
            if not(robo in empty):
                print(f"{robo}: I really like this name")
                break
        if(robo in empty):
            robo = "champ"
        f.write(f"Robo : {robo} : \n")
        print(f"{robo}: your account has been created successfully.")
        print(f"{robo}: To proceed further please signin again.")
        f.close()
    else:
        print(f"{robo}: Sorry you haven't entered Password, please signup again.")
    exit()

else:
    print(f"{robo}: I'm glad that you are back here again 😊")
    print(f"{robo}: {user} Please, Enter your password ")
    enteredPassword = input(f"{user}: ")
    f = open(f'{user}.txt','r+')
    f.seek(0)
    lines = f.readlines()
    for line in lines:
        Key,Value,a1 = line.split(" : ")
        if(Key.lower() == "password"):
            passwordValue = Value
            break
    if not(passwordValue == enteredPassword):
        print(f"{robo}: 'WRONG PASSWORD', please try again")
        exit()
    for line in lines:
        Key,Value,a1 = line.split(" : ")
        if(Key.lower() == "robo"):
            robo = Value
            break
    f.close()
    print(f"{robo}: what do you want to discover?")


welcomeGreetings = ["hello", "hi","hii","hiii", "greetings", "sup","hey"]
welcomeGreetings1 = ["good morning","good evening","good afternoon"]
welcomeGreetingResponces = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
exitGreetings = ["exit","bye","byee","byeee","quit","good night","thanks","thank you"]
saveData = ["save","add","remember","store"]
typesOfData = ["name","roll number","gmail","address","branch","college","birthdate","year","hostel","friends","place","TODO","mobile"]
userCall = ["me","I","mine","my"]
askData = ["show","tell"]
changeData = ["change"]
askdiff = ["what","what's"]

def userInputs(robo,user,status):
    own = 0
    userquestion = input(f"{user} : ")
    extractOfQuestion = [ keyword   for keyword in userquestion.split() ]
    for keyword in extractOfQuestion:
        for word in userCall:
            if(keyword == word):
                own = 1
    for word in welcomeGreetings1:
            if(word in userquestion.lower()):
                print(f"{robo} : {word.title()} buddy 😊 ")
                userInputs(robo,user,1)
    for word in welcomeGreetings:
            if(word in userquestion.lower()):
                print(f"{robo} : {random.choice(welcomeGreetingResponces)}")
                userInputs(robo,user,1)
    for word in exitGreetings:
            if(word in userquestion.lower()):
                print(f"{robo} : Ok Byeee.! Have a nice day 😊 ")
                exit()
    for keyword in extractOfQuestion:
        for word in saveData:
            if(keyword == word):
                a1,dataKey = userquestion.split(f"{word} ")
                print(f"{robo} : Ok, please give details about it ")
                dataValue = input(f"{user} : ")
                f = open(f'{user}.txt','a')
                f.write(f"{dataKey} : {dataValue} : \n")
                f.close()
                print(f"{robo} : Done !")
                userInputs(robo,user,status)
    for keyword in extractOfQuestion:
        for word in askData:
            if(keyword == word or ((keyword in askdiff) and own==1)):        # ME => me mechanical
                f = open(f'{user}.txt','r')
                f.seek(0)
                lines = f.readlines()
                f.close()
                for line in lines:
                    Key,Value,a1 = line.split(" : ")
                    # print(Key,Value)
                    if(Key.lower() in userquestion.lower()):    
                        print(f"{robo} : {Value}")
                        userInputs(robo,user,status)                
                print(f"{robo} : Sorry but this data is not available.")
                userInputs(robo,user,status)
    print(f"{robo} : Sorry but I am not supposed to answer this !")
                
                      




    
    userInputs(robo,user,status)


userInputs(robo,user,1)