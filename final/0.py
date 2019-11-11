import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
from tkinter import messagebox as mBox
from tkinter import *
import random
import webbrowser
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# wid.configure(bg = newColour) button,etc
robo = "champ"
# user = "You"
task = 0
empty = [" ","\t","\n",""]

welcomeGreetings = ["hello", "hi","hii","hiii", "greetings", "sup"]
callingrobo = [f"Hi {robo}",f"hello {robo}"]
welcomeGreetings1 = ["good morning","good evening","good afternoon"]
welcomeGreetingResponces = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
exitGreetings = ["exit","bye","byee","byeee","quit","good night","thanks","thank you"]
saveData = ["save","remember","store"]
askData = ["show","tell","show me","tell me"]
updateData = ["change","update","replace"]
askdiff = ["what","what's"]
yes = ["y","s","yes","ya","yeah","okey","hmmm","hmm"]
no = ["no","leave","na","n"]
userCall = ["me","I","mine","my"]
questioncall = ["what ","when ","where ","why ","?"]
questioncall1 = ["how "]
moodcall = [" happy","Angry","depress","unhappy","boring",""]
options=["sports","campus","faculty","library","administration","students","workshops","icc","dharwad","testimonials","others","gallery","contact","ambulance"]
information = ["dean"," address ","campus area temporary ","Director ","Founded ","Chairman ","website ","fullform ",
"motto ","Mentor ","Acronym ","Nearest Airport ","enrollment "," 550 (2019) ",
"Ownership ","Total Faculty ","Courses Offered ","Railway Station ","admission ","PLACEMENTS ","about ",
"location ","Contact ","email ","Ambulance ","Astronomy Club ","Photography Club ","Robotics Club ",
"library ","club"]
imejas = ["cutoff","photo","dharwad","director","fees","future ","holiday","hostel","location","logo","permanent","seats"]


mainApplication = tk.Tk()
mainApplication.geometry("1000x450")

mainApplication.title(" 米＾_＾米     Chat Bot     米＾_＾米 ")
########################### COLORDESIGN #############
mainApplication.configure(background = "#79ecf2")
ttk.Style().configure('Font.TLabelframe',background = "#b3f5e9",foreground = "red")
Sign = ttk.LabelFrame(mainApplication,text="  Signing   ",style='Font.TLabelframe')
Sign.grid(row = 0,column = 0,padx = 325,pady = 100)

# ttk.Style().configure('Font.TLabelframe',background = "#4fb357",foreground = "red")
labelFrame = ttk.LabelFrame(Sign,text="   please Enter your details here !   ",style='Font.TLabelframe')
labelFrame.grid(row = 0,column = 0,padx = 40,pady = 30)

Label1 = ttk.Label(labelFrame,text="User Name : ",font = ('Helvetica',12,'bold')) 
Label1.grid(row=0,column=0,sticky=tk.W,padx=10,pady=5)


namestored = tk.StringVar()
nameInput = ttk.Entry(labelFrame,width = 16,textvariable = namestored)
nameInput.grid(row = 0,column = 1,padx=10,pady=5)
nameInput.focus()

Label2 = ttk.Label(labelFrame,text="Password : ",font = ('Helvetica',12,'bold')) 
Label2.grid(row=1,column=0,sticky=tk.E,padx=10,pady=5) 

Mobilestored= tk.StringVar()
MobileInput = ttk.Entry(labelFrame,width = 16,textvariable = Mobilestored)
MobileInput.grid(row = 1,column = 1,padx=10,pady=5)
MobileInput.focus()



################################################

def signIn():
    name = namestored.get().strip()
    user = name
    password = Mobilestored.get().strip()
    if name == "" or password == "":
        mBox.showerror('Warning',"fields Can't be Empty" )
        nameInput.delete(0,tk.END)
        MobileInput.delete(0,tk.END)
    else:
        if not os.path.exists(f'{name}.txt'):
            mBox.showerror('Non-Exiting',"Your account doesn't exist please Sign Up")
            nameInput.delete(0,tk.END)
            MobileInput.delete(0,tk.END)
        else :
            f = open(f'{name}.txt','r')
            f.seek(0)
            lines = f.readlines()
            for line in lines:
                Key,Value,a1 = line.split(" : ")
                if(Key.lower() == "password"):
                    passwordValue = Value
                    break
            if not(passwordValue == password):
                mBox.showerror('Wrong Password','Please enter correct password')
                nameInput.delete(0,tk.END)
                MobileInput.delete(0,tk.END)
            else:
                Sign.destroy()
                chatbot(name)


def signUp():
    name = namestored.get().strip()
    user = name
    password = Mobilestored.get().strip()
    if name == "" or password == "":
        mBox.showerror('Warning',"fields Can't be Empty" )
        nameInput.delete(0,tk.END)
        MobileInput.delete(0,tk.END)
    else:
        if not os.path.exists(f'{name}.txt'):
            mBox.showinfo('Processing','Please continue process')
            Sign.destroy()
            SignUpForm(name,password)
        else :
            mBox.showerror('Already Exiting','Your account already exist please Sign In')
            # nameInput.delete(0,tk.END)
            # MobileInput.delete(0,tk.END)


submitButton1 = tk.Button(Sign,text="SignIn ",command = signIn)
submitButton1.grid(row = 1,column = 0)
submitButton1.configure(foreground = "#ffffff",background = "#000000")

submitButton2 = tk.Button(Sign,text="SignUP",command = signUp)
submitButton2.grid(row = 2,column = 0)
submitButton2.configure(foreground = "#ffffff",background = "#000000")


#########################################################################################################
##########################################################################################################


def SignUpForm(userName,password):
    name = userName
    Signupnext = ttk.LabelFrame(mainApplication,text="  Sign up Form ")
    Signupnext.grid(row = 0,column = 0,padx = 275,pady = 30)
    labelFrame = ttk.LabelFrame(Signupnext,text="   please Enter your details here !   ")
    labelFrame.grid(row = 0,column = 0,padx = 40,pady = 30)


    labels = [f"firstname : ","lastname : ","city : " ,"country : ","phone number : ","mail ID : ","JEE rank : "]

    for i in range(len(labels)):
        currentLabel = ttk.Label(labelFrame,text=labels[i]) 
        currentLabel.grid(row=i,column=0,sticky=tk.W) 

    userDict = {
        "firstname":tk.StringVar(),
        "lastname":tk.StringVar(),
        "city":tk.StringVar(),
        'country':tk.StringVar(),
        'phone number':tk.StringVar(),
        'mail ID':tk.StringVar(),
        'JEE rank':tk.StringVar()
    }

    index = 0

    for i in userDict:
        currentEntryBox = ttk.Entry(labelFrame,width = 16,textvariable = userDict[i])
        currentEntryBox.grid(row = index,column = 1)
        currentEntryBox.focus()
        index+=1

   
    for child in labelFrame.winfo_children():
        child.grid_configure(padx=35,pady=5)


    def submitAction():
        # _tkinter.TclError: error
        ok = 1
        for i in userDict:
            if userDict[i].get() == "":
                mBox.showerror('Warning',"fields Can't be Empty" )
                ok = -1
                break
            elif i == "JEE rank" or i == "phone number":
                try:
                    num = int(userDict[i].get())
                except ValueError:
                    mBox.showerror('Error',f"{i} must contain digits only" )
                    ok = -1
                    break
            elif not "@" in userDict["mail ID"].get() and not userDict["mail ID"].get() == "":
                ok = -1
                mBox.showerror('Error'," please enter valid mail Id" )
                break

        if ok==1:
            f = open(f'{userName}.txt','a')
            f.write(f"Password : {password} : \n")
            for i in userDict:
                f.write(f"{i} : {userDict[i].get()} : \n")
            mBox.showinfo('Confirmed','Submitted Successfully ')
            Signupnext.destroy()
            chatbot(name)

    submitButton = tk.Button(Signupnext,text="Submit",command = submitAction)
    submitButton.grid(row = 1,column = 0,padx = 80,pady =10)
    submitButton.configure(foreground = "#ffffff",background = "#000000")

################################################

###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################


def chatbot(name):
    
    class Actions:
        def chatUpdate(chat,i):
            # if i ==0 :
            # print(Actions.chatLast)
            chatlist.insert(Actions.chatLast,chat)
            Actions.chatLast=Actions.chatLast+1
            # chatlist.grid(sticky="e")
            chatlist.pack( side=RIGHT, fill=BOTH)
            chatBox.config(command=chatlist.yview,bg="#b9eded")

    def callUpdater():
        # key1=""
        # mvalue = ""
        user = name
        rawQ = chatStore.get().strip()
        question=f"{name} : {chatStore.get().strip()}"
        Actions.chatUpdate(question,0)
        f = open(f'00.txt','r+')
        f.seek(0)
        line = f.readline()
        f.close()
        if (line == "00"):
            answer = userInputs(robo,user,1,question)
            if not type(answer) == tuple:
                Actions.chatUpdate(answer,1)
        elif line == "11" or line == "22" or line =="23" or line == "33" or line == "34":
            answer = ""
        if answer == f"{robo} : Ok Byeee.! Have a nice day":
            Actions.chatUpdate(answer,1)
            exit()
                # print(f"{robo} : Ok, please give details about it ")
                # t1 = ("save",0,datakey,f"{robo} : Ok, please give details about it ",f"{robo} : Done !")
                # return t1
                # dataValue = input(f"{user} : ").strip()
                # f = open(f'{user}.txt','a')
                # f.write(f"{dataKey} : {dataValue} : \n")
                # f.close()
                # print(f"{robo} : Done !")
                # userInputs(robo,user,status,"")
        elif type(answer) == tuple:
            if answer[0] == "exit" :
                Actions.chatUpdate(answer[1],1)
                Actions.chatUpdate(answer[2],1)
            if answer[0] == "site" :
                Actions.chatUpdate(answer[2],1)
                webbrowser.open(answer[1])
            if answer[0] == "ask" :
                f = open(f'00.txt','w')
                f.seek(0)
                f.write("11") 
                f.close()
                f = open(f'01.txt','w')
                f.seek(0)
                f.write(f"{answer[5]}") 
                f.close()
                Actions.chatUpdate(answer[2],1)
            if answer[0] == "update" :
                if answer[1] ==0:
                    f = open(f'00.txt','w')
                    f.seek(0)
                    f.write("22") 
                    f.close()
                    f = open(f'01.txt','w')
                    f.seek(0)
                    f.write(f"{answer[4]}") 
                    f.close()
                    Actions.chatUpdate(answer[2],1)
                if answer[1] ==1:
                    f = open(f'00.txt','w')
                    f.seek(0)
                    f.write("23") 
                    f.close()
                    f = open(f'01.txt','w')
                    f.seek(0)
                    f.write(f"{answer[2]} : {answer[3]} : \n") 
                    f.close()
                    Actions.chatUpdate(answer[4],1)
                        # t1 = ("save",1,Key,Value,f"{robo} : sorry it's already saved, Do you want to 'update it' or 'save as new'",f"{robo} : Sorry can't able understand, Please try again !")
                        # return t1
            if answer[0] == "save" :
                if answer[1] == 0 :
                    f = open(f'00.txt','w')
                    f.seek(0)
                    f.write("33") 
                    f.close()
                    f = open(f'01.txt','w')
                    f.seek(0)
                    f.write(f"{answer[2]}") 
                    f.close()
                    Actions.chatUpdate(answer[3],1)
                if answer[1]==1:
                    f = open(f'00.txt','w')
                    f.seek(0)
                    f.write("34") 
                    f.close()
                    f = open(f'01.txt','w')
                    f.seek(0)
                    f.write(f"{answer[2]} : {answer[3]} : \n") 
                    f.close()
                    Actions.chatUpdate(answer[4],1)
        elif answer == "":
            if (line == "11"):
                f = open(f'00.txt','w')
                f.seek(0)
                f.write("00") 
                f.close()
                if(rawQ in empty):
                    answer = f"{robo} : Sorry you haven't entered anything, Please try again !"
                    Actions.chatUpdate(answer,1)
                elif (rawQ in no):
                    answer = f"{robo} : ok alright , let's discover more things!"
                    Actions.chatUpdate(answer,1)   
                elif (rawQ in yes):
                    f = open(f'01.txt','r+')
                    f.seek(0)
                    line = f.readline()
                    f.close()
                    # print(line)
                    answer = userInputs(robo,user,1,line)
                    f = open(f'00.txt','w')
                    f.seek(0)
                    f.write("33") 
                    f.close()
                    f = open(f'01.txt','w')
                    f.seek(0)
                    f.write(f"{answer[2]}") 
                    f.close()
                    Actions.chatUpdate(answer[3],1)
                    ##############################################
                    ###########################################
                    #######################################
                    # Actions.chatUpdate(answer,1)              
                else:
                    answer = f"{robo} : Sorry can't able understand, Please try again !"
                    Actions.chatUpdate(answer,1) 
            elif (line == "22"):
                f = open(f'00.txt','w')
                f.seek(0)
                f.write("00") 
                f.close()
                if(rawQ in empty):
                    answer = f"{robo} : Sorry you haven't entered anything, Please try again !"
                    Actions.chatUpdate(answer,1)
                elif (rawQ in no):
                    answer = f"{robo} : ok alright , let's discover more things!"
                    Actions.chatUpdate(answer,1)   
                elif (rawQ in yes):
                    f = open(f'01.txt','r+')
                    f.seek(0)
                    line = f.readline()
                    f.close()
                    ##############################################
                    ###########################################
                    #######################################
                    answer = userInputs(robo,user,1,line)
                    f = open(f'00.txt','w')
                    f.seek(0)
                    f.write("33") 
                    f.close()
                    f = open(f'01.txt','w')
                    f.seek(0)
                    f.write(f"{answer[2]}") 
                    f.close()
                    Actions.chatUpdate(answer[3],1)
                    # Actions.chatUpdate(answer,1)              
                else:
                    answer = f"{robo} : Sorry can't able understand, Please try again !"
                    Actions.chatUpdate(answer,1) 
            elif (line == "23"):
                f = open(f'00.txt','w')
                f.seek(0)
                f.write("00") 
                f.close()
                if(rawQ in empty):
                    answer = f"{robo} : Sorry you haven't entered anything, Please try again !"
                    Actions.chatUpdate(answer,1)                
                else:
                    Mvalue = rawQ
                    f = open(f'01.txt','r+')
                    f.seek(0)
                    line = f.readline()
                    f.close()
                    key , value,a1 = line.split(" : ")
                    f = open(f'{user}.txt','a')
                    # f.seek(0)
                    f.write(f"{key} : {Mvalue} : {a1}")
                    f.close()
                    answer = f"{robo} : updated successfully !"
                    Actions.chatUpdate(answer,1) 
            elif (line == "33"):
                f = open(f'00.txt','w')
                f.seek(0)
                f.write("00") 
                f.close()
                if(rawQ in empty):
                    answer = f"{robo} : Sorry you haven't entered anything, Please try again !"
                    Actions.chatUpdate(answer,1)                
                else:
                    Mvalue = rawQ
                    f = open(f'01.txt','r+')
                    f.seek(0)
                    line = f.readline()
                    f.close()
                    key = line
                    f = open(f'{user}.txt','a')
                    # f.seek(0)
                    f.write(f"{key} : {Mvalue} : \n")
                    f.close()
                    answer = f"{robo} : saved successfully !"
                    Actions.chatUpdate(answer,1)
            elif (line == "34"):
                f = open(f'00.txt','w')
                f.seek(0)
                f.write("00") 
                f.close()
                if(rawQ in empty):
                    answer = f"{robo} : Sorry you haven't entered anything, Please try again !"
                    Actions.chatUpdate(answer,1)                
                elif "save" in rawQ or "new" in rawQ:
                    f = open(f'01.txt','r+')
                    f.seek(0)
                    key,value,a1 = f.readline().split(" : ")
                    f.close()
                    line = (f"save {key} new")
                    ##############################################
                    ###########################################
                    ####################################### save new new
                    answer = userInputs(robo,user,1,line) 
                    f = open(f'00.txt','w')
                    f.seek(0)
                    f.write("33") 
                    f.close()
                    f = open(f'01.txt','w')
                    f.seek(0)
                    f.write(f"{answer[2]}") 
                    f.close()
                    Actions.chatUpdate(answer[3],1) 
                elif "update" in rawQ or "change" in rawQ:
                    f = open(f'01.txt','r+')
                    f.seek(0)
                    key,value,a1 = f.readline().split(" : ")
                    f.close()
                    line = (f"update {key}")
                    ##############################################
                    ###########################################
                    #######################################
                    answer = userInputs(robo,user,1,line) 
                    f = open(f'00.txt','w')
                    f.seek(0)
                    f.write("23") 
                    f.close()
                    f = open(f'01.txt','w')
                    f.seek(0)
                    f.write(f"{answer[2]} : {answer[3]} : \n") 
                    f.close()
                    Actions.chatUpdate(answer[4],1)
                else:
                    answer = f"{robo} : Sorry can't able understand, Please try again !"
                    Actions.chatUpdate(answer,1) 
        # else:
            # Actions.chatUpdate(answer,1)
        # print(answer)
        chatStore.set("")
    # def callUpdater():
    #     text = textBox.get()
    #     textBox.delete(0, 'end')
    #     chat.configure(state='normal')
    #     chat.insert('end', text + '\n')
    #     chat.configure(state='disabled')

    ############################# COLORDIGIN #########
    ttk.Style().configure('Font.TLabelframe',background = "#353838",foreground = "red")
    ChatStarted = ttk.LabelFrame(mainApplication,text="  Chat Box ",style="Font.TLabelframe")
    ChatStarted.grid(row = 0,column = 0,padx = 40,pady = 60)
    ChatHistroy = ttk.LabelFrame(ChatStarted,text="  ChatHistroy ")
    ChatHistroy.grid(row = 0,column = 0,padx = 40,pady = 10)

    # chat box
    chatBox = Scrollbar(ChatHistroy)
    chatBox.pack(side=RIGHT, fill=Y)
    chatlist = Listbox(ChatHistroy, yscrollcommand = chatBox.set,width=100)
    Actions.chatLast=0
    Actions.chatUpdate("                        ",0)

    # text box
    # textView = Label(frame2, text="Input: ")
    # textView.pack(side=LEFT)
    # text_text = StringVar()
    # textBox = Entry(frame2, textvariable=text_text, bd=0, width=40, bg="pink")
    # textBox.pack(side=RIGHT)
    chatStore = tk.StringVar()                    
    ageInputBox = ttk.Entry(ChatStarted,width = 80,textvariable = chatStore)
    ageInputBox.grid(row = 1,column = 0)
    # ageInputBox.configure(background = "#f2b78d")
    
    submitButton = tk.Button(ChatStarted,text="Ask",command = callUpdater)
    submitButton.grid(row = 1,column = 0,sticky="E",padx = 40,pady = 20)
    ############ COLORDIGIN
    submitButton.configure(foreground = "#ffffff",background = "#000000")
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################

###########################################################################################################
##########################################################################################################
#####################----------------Main Chatbot workings -------------------#####################











def userInputs(robo,user,status,userquestion):
        
    own = 0
    for word in userCall:
        if(word in userquestion.lower()):
            own = 1
    for word in welcomeGreetings1:
            if(word in userquestion.lower()):
                return (f"{robo} : {word.title()} buddy  ")
    for word in options:
        if (word in userquestion.lower()):
            t1 = ("site",f"http://www.iitdh.ac.in/{word}.php",f"{robo} : Now you will be directed to {word} page ")
            # webbrowser.open(f"http://www.iitdh.ac.in/{word}.php")
            return t1

        if ("facebook" in userquestion.lower()):
            t1 = ("site","https://www.facebook.com/iitdharwadofficial/",f"{robo} : Opening Facebook page")
                # webbrowser.open("https://www.facebook.com/iitdharwadofficial/")
            return t1
        if ("youtube" in userquestion.lower()):
            t1 = ("site","https://www.youtube.com/channel/UCG_M5tP34-uO-Jkr9Q7VDsA",f"{robo} : Opening youtube channel")
                # webbrowser.open("https://www.youtube.com/channel/UCG_M5tP34-uO-Jkr9Q7VDsA")
            return t1
    for word in imejas:
        if(word in userquestion.lower()):
            try:
                img = mpimg.imread(f'{word}.png')
            except FileNotFoundError:
                img = mpimg.imread(f'{word}.jpg')
            # else:

            imgplot = plt.imshow(img)
            plt.show()
            return(f"{robo} : and here we go!!")
        

    for word in welcomeGreetings:
        if(word in userquestion.lower()):
            return(f"{robo} : {random.choice(welcomeGreetingResponces)}")
    for word in exitGreetings:
        if(word in userquestion.lower() or status == 0):
            return(f"{robo} : Ok Byeee.! Have a nice day")
            
    for word in information:
        if((word in userquestion.lower())):
            f = open(f'info.txt','r+')
            found = 0 
            f.seek(0)
            lines = f.readlines()
            f.close()
            num = 0
            for line in lines:
                Key,Value,a1 = line.split(" : ")
                if(Key.lower() == word.lower()):
                    found =1
                    return(f"{robo} : {Value}")  
    for word in updateData:
            if(word in userquestion.lower()):
                try:
                    a1,dataKey = userquestion.split(f"{word} ")
                except ValueError:
                    return(f"{robo} : sorry but can you be more clear")
                    # userInputs(robo,user,1,"")                    
                f = open(f'{user}.txt','r')
                lines = f.readlines()
                os.remove(f"{user}.txt")
                f = open(f'{user}.txt','a')
                data = 0
                string1 = ""
                string2 = ""
                for line in lines:
                    Key,Value,a1 = line.split(" : ")
                    if(Key == dataKey):
                        data = 1
                        string1 = Key
                        string2 = Value
                        # print(f"{robo} : what you want to set instead of '{Value}' ?")
                        # MValue = input(f"{user} : ").strip()
                        # if(MValue in empty):
                        #     print(f"{robo} : Sorry you haven't entered anything, Please try again !")
                        #     f.write(f"{Key} : {Value} : {a1}")
                        # else:
                        #     f.write(f"{Key} : {MValue} : {a1}")
                        #     print(f"{robo} : updated successfully !")
                    else:
                        f.write(f"{Key} : {Value} : {a1}")
                if data == 1 :
                    t1 = ("update",1,string1,string2,f"{robo} : what you want to set instead of '{string2}' ?",f"{robo} : Sorry you haven't entered anything, Please try again !",f"{robo} : updated successfully !")
                    return t1
                f.close()
                if(data == 0):
                    t1 = ("update",0,f"{robo} : can't be updated as it doesn't exist. Still do you want to save it?",f"{robo} : Sorry you haven't entered anything, Please try again !",f"Hey {robo} please save {dataKey}",f"{robo} : ok alright , let's discover more things!",f"{robo} : Sorry can't able understand, Please try again !")
                    return t1
                    # answer = input(f"{user} : ").strip()
                    # if(answer in empty):
                    #     print(f"{robo} : Sorry you haven't entered anything, Please try again !")
                    # elif (answer in yes):
                    #     userInputs(robo,user,status,f"Hey {robo} please save {dataKey}")
                    # elif (answer in no):
                    #     print(f"{robo} : ok alright , let's discover more things!")
                    # else:
                    #     print(f"{robo} : Sorry can't able understand, Please try again !")
                # userInputs(robo,user,status,"")
    for word in saveData:
            if(word in userquestion.lower()):
                try:
                    a1,dataKey = userquestion.split(f"{word} ")
                except ValueError:
                    return(f"{robo} : sorry but can you be more clear")

                    # userInputs(robo,user,1,"")
                f = open(f'{user}.txt','r')
                lines = f.readlines()
                for line in lines:
                    Key,Value,a1 = line.split(" : ")
                    if(Key == dataKey):
                        t1 = ("save",1,Key,Value,f"{robo} : sorry it's already saved, Do you want to 'update it' or 'save as new'",f"{robo} : Sorry can't able understand, Please try again !")
                        return t1
                        # print(f"{robo} : Do you want to 'update it or save as new' ?")
                        # answer = input(f"{user} : ").strip()
                        # if(answer in empty):
                        #     print(f"{robo} : Sorry you haven't entered anything, Please try again !")
                        #     userInputs(robo,user,status,"")
                        # elif (answer in yes):
                        #     print(f"{robo} : what do you want 'update' or 'save as new' ?")
                        #     response = input(f"{user} : ").strip()
                        #     if(response in saveData or response == "new"):
                        #         userInputs(robo,user,status,f"Hey {robo} please save {dataKey} (new)")
                        #     elif(response in updateData):
                        #         userInputs(robo,user,status,f"Hey {robo} please update {dataKey}")
                        #     else:
                        #         print(f"{robo} : Sorry can't able understand, Please try again !")
                        #         userInputs(robo,user,status,"")
                        # elif (answer in no):
                        #     print(f"{robo} : ok alright , let's discover more things!")
                        #     userInputs(robo,user,status,"")                            
                        # else:
                        #     print(f"{robo} : Sorry can't able understand, Please try again !")
                        #     userInputs(robo,user,status,"")
                # print(f"{robo} : Ok, please give details about it ")
                t1 = ("save",0,f"{dataKey}",f"{robo} : Ok, please give details about it ",f"{robo} : Done !")
                return t1
                # dataValue = input(f"{user} : ").strip()
                # f = open(f'{user}.txt','a')
                # f.write(f"{dataKey} : {dataValue} : \n")
                # f.close()
                # print(f"{robo} : Done !")
                # userInputs(robo,user,status,"")

################################
###### ASK 


    for word in askData:
        if((word in userquestion.lower()) or (("what") in userquestion.lower() and own==1)):# ME => mech
            try:
                a1,dataKey = userquestion.split(f"{word} ")
            except ValueError:
                return(f"{robo} : sorry but can you be more clear")
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
                    return(f"{robo} : {key} - {Value}")
            # if(found ==1):
            #     userInputs(robo,user,status,"")     


            t1 = ("ask",f"{robo} : Sorry but this data is not available.",f"{robo} : Sorry but this data is not available , Do you want to add this ?",f"{robo} : Sorry you haven't entered anything, Please try again !",f"{robo} : ok alright , let's discover more things!",f"Hey {robo} please save {dataKey}",f"{robo} : Sorry can't able understand, Please try again !")
            return t1
            # answer = input(f"{user} : ").strip()
            # if(answer in empty):
            #     print(f"{robo} : Sorry you haven't entered anything, Please try again !")
            # elif (answer in no):
            #     print(f"{robo} : ok alright , let's discover more things!")    
            # elif (answer in yes):
            #     userInputs(robo,user,status,f"Hey {robo} please save {dataKey}")                     
            # else:
            #     print(f"{robo} : Sorry can't able understand, Please try again !")
            # userInputs(robo,user,status,"")

############################################################e########################################## 

# Unable to interpret 

    # print(f"{robo} : Sorry I am not able to answer this !")
    f = open("ADMINfeedback.txt","a")
    f.write(f"{userquestion}\n")
    f.close()
    t1 = ("exit",f"{robo} : Sorry I am not able to answer this !",f"{robo} :  your question has been added in feedback for Admin, Still you can get more info here :")
    var,a1 = userquestion.split(" : ")
    # print(var)
    webbrowser.open(f"http://www.google.com/search?q={a1}")
    return t1
    # userInputs(robo,user,status,"")


###################################################################################################### 







###########################################################################################################
##########################################################################################################

################################################

mainApplication.mainloop()


###########################################################################################################
##########################################################################################################

            # t1 = ("ask",f"{robo} : Sorry but this data is not available",f"{robo} : Sorry but this data is not available , Do you want to add this ?",f"{robo} : Sorry you haven't entered anything, Please try again !",f"{robo} : ok alright , let's discover more things!",f"Hey {robo} please save {dataKey}",f"{robo} : Sorry can't able understand, Please try again !")
            # return t1
            # answer = input(f"{user} : ").strip()
            # if(answer in empty):
            #     print(f"{robo} : Sorry you haven't entered anything, Please try again !")
            # elif (answer in no):
            #     print(f"{robo} : ok alright , let's discover more things!")    
            # elif (answer in yes):
            #     userInputs(robo,user,status,f"Hey {robo} please save {dataKey}")                     
            # else:
            #     print(f"{robo} : Sorry can't able understand, Please try again !")
            # userInputs(robo,user,status,"")
            # if answer[0] == "exit" :
            #     Actions.chatUpdate(answer[1],1)
            #     Actions.chatUpdate(answer[2],1)