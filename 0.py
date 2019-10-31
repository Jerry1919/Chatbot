import os
import random

robo = "champ"
empty = [" ","\t","\n",""]

print(f"{robo} : Hi.!! I am {robo}, here for you.")
print(f"{robo} : What's your user name? ")
user = input(f"user : ").strip()

if not os.path.exists(f'{user}.txt'):
    print(f"{robo} : I'm glad that you are here 😊  I assure, you will have great experiance.")
    print(f"{robo} : {user} Please, Enter password for your new account :")
    enteredPassword = input(f"{user} : ").strip()
    if not(enteredPassword in  empty):
        f = open(f'{user}.txt','a')
        f.write(f"Password : {enteredPassword} : \n")
        for i in range(1,4):
            print(f"{robo} : What do you want to call me :")
            robo = input(f"{user} : ").strip()
            if not(robo in empty):
                print(f"{robo} : I really like this name")
                break
        if(robo in empty):
            robo = "champ"
        f.write(f"Robo : {robo} : \n")
        print(f"{robo} : your account has been created successfully.")
        print(f"{robo} : To proceed further please signin again.")
        f.close()
    else:
        print(f"{robo} : Sorry you haven't entered Password, please signup again.")
    exit()

else:
    print(f"{robo} : I'm glad that you are back here again 😊")
    print(f"{robo} : {user} Please, Enter your password ")
    enteredPassword = input(f"{user}: ").strip()
    f = open(f'{user}.txt','r+')
    f.seek(0)
    lines = f.readlines()
    for line in lines:
        Key,Value,a1 = line.split(" : ")
        if(Key.lower() == "password"):
            passwordValue = Value
            break
    if not(passwordValue == enteredPassword):
        print(f"{robo} : 'WRONG PASSWORD', please try again")
        exit()
    for line in lines:
        Key,Value,a1 = line.split(" : ")
        if(Key.lower() == "robo"):
            robo = Value
            break
    f.close()
    print(f"{robo} : what do you want to discover?")


welcomeGreetings = ["hello", "hi","hii","hiii", "greetings", "sup"]
welcomeGreetings1 = ["good morning","good evening","good afternoon"]
welcomeGreetingResponces = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
exitGreetings = ["exit","bye","byee","byeee","quit","good night","thanks","thank you"]
saveData = ["save","add","remember","store"]
typesOfData = ["name","roll number","gmail","address","branch","college","birthdate","year","hostel","friends","place","TODO","mobile"]
userCall = ["me","I","mine","my"]
askData = ["show","tell"]
updateData = ["change","update","replace"]
askdiff = ["what","what's"]
yes = ["y","s","yes","ya","yeah","okey","hmmm","hmm"]
no = ["no","leave","na","n"]

def userInputs(robo,user,status,userquestion):
    own = 0
    if(userquestion == ""):
        userquestion = input(f"{user} : ").strip()
    extractOfQuestion = [ keyword   for keyword in userquestion.split() ]
    for keyword in extractOfQuestion:
        for word in userCall:
            if(keyword == word):
                own = 1
    for word in welcomeGreetings1:
            if(word in userquestion.lower()):
                print(f"{robo} : {word.title()} buddy 😊 ")
                userInputs(robo,user,1,"")
    for word in welcomeGreetings:
            if(word in userquestion.lower()):
                print(f"{robo} : {random.choice(welcomeGreetingResponces)}")
                userInputs(robo,user,1,"")
    for word in exitGreetings:
            if(word in userquestion.lower()):
                print(f"{robo} : Ok Byeee.! Have a nice day 😊 ")
                exit()
    for word in updateData:
            if(word in userquestion.lower()):
                a1,dataKey = userquestion.split(f"{word} ")
                f = open(f'{user}.txt','r')
                lines = f.readlines()
                os.remove(f"{user}.txt")
                f = open(f'{user}.txt','a')
                data = 0
                for line in lines:
                    Key,Value,a1 = line.split(" : ")
                    if(Key == dataKey):
                        data = 1
                        print(f"{robo} : what you want to set instead of '{Value}' ?")
                        MValue = input(f"{user} : ").strip()
                        if(MValue in empty):
                            print(f"{robo} : Sorry you haven't entered anything, Please try again !")
                            f.write(f"{Key} : {Value} : {a1}")
                        else:
                            f.write(f"{Key} : {MValue} : {a1}")
                            print(f"{robo} : updated successfully !")
                    else:
                        f.write(f"{Key} : {Value} : {a1}")
                f.close()
                if(data == 0):
                    print(f"{robo} : can't be updated as it doesn't exist. Still do you want to save it?")
                    answer = input(f"{user} : ").strip()
                    if(answer in empty):
                        print(f"{robo} : Sorry you haven't entered anything, Please try again !")
                    elif (answer in yes):
                        userInputs(robo,user,status,f"Hey {robo} please save {dataKey}")
                    elif (answer in no):
                        print(f"{robo} : ok alright , let's discover more things!")
                    else:
                        print(f"{robo} : Sorry can't able understand, Please try again !")
                userInputs(robo,user,status,"")
    for word in saveData:
            if(word in userquestion.lower()):
                a1,dataKey = userquestion.split(f"{word} ")
                f = open(f'{user}.txt','r')
                lines = f.readlines()
                for line in lines:
                    Key,Value,a1 = line.split(" : ")
                    if(Key == dataKey):
                        print(f"{robo} : sorry it's already saved")
                        print(f"{robo} : Do you want to 'update it or save as new '?")
                        answer = input(f"{user} : ").strip()
                        if(answer in empty):
                            print(f"{robo} : Sorry you haven't entered anything, Please try again !")
                            userInputs(robo,user,status,"")
                        elif (answer in yes):
                            print(f"{robo} : what do you want 'update' or 'save as new' ?")
                            response = input(f"{user} : ").strip()
                            if((response in saveData) or (response == "new")):
                                userInputs(robo,user,status,f"Hey {robo} please save {dataKey} (new)")
                            elif(response in updateData):
                                userInputs(robo,user,status,f"Hey {robo} please update {dataKey}")
                            else:
                                print(f"{robo} : Sorry can't able understand, Please try again !")
                                userInputs(robo,user,status,"")
                        elif (answer in no):
                            print(f"{robo} : ok alright , let's discover more things!")
                            userInputs(robo,user,status,"")                            
                        else:
                            print(f"{robo} : Sorry can't able understand, Please try again !")
                            userInputs(robo,user,status,"")
                print(f"{robo} : Ok, please give details about it ")
                dataValue = input(f"{user} : ").strip()
                f = open(f'{user}.txt','a')
                f.write(f"{dataKey} : {dataValue} : \n")
                f.close()
                print(f"{robo} : Done !")
                userInputs(robo,user,status,"")
    for word in askData:
        if((word in userquestion.lower()) or (("what") in userquestion.lower() and own==1)):# ME => mech
            a1,dataKey = userquestion.split(f"{word} ")
            f = open(f'{user}.txt','r')
            found = 0 
            f.seek(0)
            lines = f.readlines()
            f.close()
            num = 0
            for line in lines:
                Key,Value,a1 = line.split(" : ")
                if(dataKey.lower() in Key.lower()):   
                    found = 1 
                    num+=1
                    a1,key =  Key.split("my ")
                    print(f"{robo} : {num}. {key} - {Value}")
            if(found ==1):
                userInputs(robo,user,status,"")     

            print(f"{robo} : Sorry but this data is not available, Do you want to add this ?")
            answer = input(f"{user} : ").strip()
            if(answer in empty):
                print(f"{robo} : Sorry you haven't entered anything, Please try again !")
            elif (answer in no):
                print(f"{robo} : ok alright , let's discover more things!")    
            elif (answer in yes):
                userInputs(robo,user,status,f"Hey {robo} please save {dataKey}")                     
            else:
                print(f"{robo} : Sorry can't able understand, Please try again !")
            userInputs(robo,user,status,"")


    print(f"{robo} : Sorry I am not supposed to answer this !")
    f = open("ADMINfeedback.txt","a")
    f.write(f"{userquestion}\n")
    f.close()
    print(f"{robo} : your question has been added in feedback for Admin") 
    userInputs(robo,user,status,"")


userInputs(robo,user,1,"")