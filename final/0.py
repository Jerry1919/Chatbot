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
import lists

from csv import DictWriter,DictReader


# wid.configure(bg = newColour) button,etc
robo = "champ"
# user = "You"
task = 0

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
                if(user == "Admin"):
                    adminSection()
                else:
                    chatbot(name)

####################################################################################
####################################################################################
####################################################################################

def adminSection():
    # print("In admin section ")
    name = "Admin"
    password = "Admin"
    ttk.Style().configure('Font.TLabelframe',background = "#b3f5e9",foreground = "red")
    AdminBox1 = ttk.LabelFrame(mainApplication,text="  Admin Section ",style ='Font.TLabelframe')
    AdminBox1.grid(row = 0,column = 0,padx = 325,pady = 125)


    def Update():
        AdminBox1.destroy()
        ttk.Style().configure('Font.TLabelframe',background = "#b3f5e9",foreground = "red")
        updateBox = ttk.LabelFrame(mainApplication,text=" Only below Data files can be updated",style ='Font.TLabelframe')
        updateBox.grid(row = 0,column = 0,padx = 325,pady = 125)

        submitButton = tk.Button(updateBox,text="library data",command =updatelibrarydata)
        submitButton.grid(row = 0,column = 0,padx = 80,pady =10)
        submitButton.configure(foreground = "#ffffff",background = "#000000")

        submitButton = tk.Button(updateBox,text="not available")
        submitButton.grid(row = 1,column = 0,padx = 80,pady =10)
        submitButton.configure(foreground = "#ffffff",background = "#000000")

        submitButton = tk.Button(updateBox,text=" not avalaible ")
        submitButton.grid(row = 2,column = 0,padx = 80,pady =10)
        submitButton.configure(foreground = "#ffffff",background = "#000000")

        
        
    def Add():
        AdminBox1.destroy()
        ttk.Style().configure('Font.TLabelframe',background = "#b3f5e9",foreground = "red")
        updateBox = ttk.LabelFrame(mainApplication,text=" Only below Data files can be extended",style ='Font.TLabelframe')
        updateBox.grid(row = 0,column = 0,padx = 325,pady = 125)

        submitButton = tk.Button(updateBox,text="library data",command =addlibrarydata)
        submitButton.grid(row = 0,column = 0,padx = 80,pady =10)
        submitButton.configure(foreground = "#ffffff",background = "#000000")

        submitButton = tk.Button(updateBox,text="not available")
        submitButton.grid(row = 1,column = 0,padx = 80,pady =10)
        submitButton.configure(foreground = "#ffffff",background = "#000000")

        submitButton = tk.Button(updateBox,text=" not avalaible ")
        submitButton.grid(row = 2,column = 0,padx = 80,pady =10)
        submitButton.configure(foreground = "#ffffff",background = "#000000")


    def Feedback():
        AdminBox1.destroy()
        WorkOnFeedback()

    submitButton = tk.Button(AdminBox1,text="work on Feedback",command = Feedback)
    submitButton.grid(row = 0,column = 0,padx = 80,pady =10)
    submitButton.configure(foreground = "#ffffff",background = "#000000")

    submitButton = tk.Button(AdminBox1,text="Update data",command = Update)
    submitButton.grid(row = 1,column = 0,padx = 80,pady =10)
    submitButton.configure(foreground = "#ffffff",background = "#000000")

    submitButton = tk.Button(AdminBox1,text="Add data",command = Add)
    submitButton.grid(row = 2,column = 0,padx = 80,pady =10)
    submitButton.configure(foreground = "#ffffff",background = "#000000")

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
def updatelibrarydata():
    ttk.Style().configure('Font.TLabelframe',background = "#b3f5e9",foreground = "red")
    addDataInLabrary = ttk.LabelFrame(mainApplication,text="  Add library data ",style='Font.TLabelframe')
    addDataInLabrary.grid(row = 0,column = 0,padx = 100,pady = 30)

    labelFrame = ttk.LabelFrame(addDataInLabrary,text="   please Enter All details correctly !   ",style='Font.TLabelframe')
    labelFrame.grid(row = 0,column = 0,padx = 40,pady = 30)


    labels = ["Book Name : ",  "Auhor : ",  "Number of copies : ",  "Price : ",  "Issued by : ",  "Description : ",  "Reviews (0.0-5.0) : "]

    for i in range(len(labels)):
        currentLabel = ttk.Label(labelFrame,text=labels[i]) 
        currentLabel.grid(row=i,column=0,sticky=tk.W) 

    userDict1 = {
        "Book Name":tk.StringVar(),
        "Auhor":tk.StringVar(),
        "Number of copies":tk.StringVar(),
        "Price":tk.StringVar(),
        "Issued by":tk.StringVar(),
        "Description":tk.StringVar(),
        "Reviews (0.0-5.0)":tk.StringVar()
    }

    index = 0

    for i in userDict1:
        currentEntryBox = ttk.Entry(labelFrame,width = 40,textvariable = userDict1[i])
        currentEntryBox.grid(row = index,column = 2)
        currentEntryBox.focus()
        index+=1

   
    for child in labelFrame.winfo_children():
        child.grid_configure(padx=35,pady=5)


    def submitAction():
        pass
        ok = 1
        num = [] 
        for i in userDict1:
            if userDict1[i].get() == "":
                mBox.showerror('Warning',"fields Can't be Empty" )
                ok = -1
                break
            num.append(userDict1[i].get())

        if ok==1:
            pass
            with open('libbooks.csv','a',newline='') as wf:
                CSVwriter = DictWriter(wf,fieldnames=['Book Name' , 'Auhor' , 'Number of copies' , 'Price' , 'Issued by' , 'Description' , 'Reviews'],delimiter='|')
                CSVwriter.writerow({
                                        "Book Name":num[0],
                                        "Auhor":num[1],
                                        "Number of copies":num[2],
                                        "Price":num[3],
                                        "Issued by":num[4],
                                        "Description":num[5],
                                        "Reviews":num[6]
                                    })
            mBox.showinfo ('successful',"Book has been added successfully" )
    submitButton = tk.Button(addDataInLabrary,text="  Add  ",command = submitAction)
    submitButton.grid(row = 1,column = 0,padx = 80,pady =10)
    submitButton.configure(foreground = "#ffffff",background = "#000000")

def addlibrarydata():
    ttk.Style().configure('Font.TLabelframe',background = "#b3f5e9",foreground = "red")
    addDataInLabrary = ttk.LabelFrame(mainApplication,text="  Add library data ",style='Font.TLabelframe')
    addDataInLabrary.grid(row = 0,column = 0,padx = 100,pady = 30)

    labelFrame = ttk.LabelFrame(addDataInLabrary,text="   please Enter All details correctly !   ",style='Font.TLabelframe')
    labelFrame.grid(row = 0,column = 0,padx = 40,pady = 30)


    labels = ["Book Name : ",  "Auhor : ",  "Number of copies : ",  "Price : ",  "Issued by : ",  "Description : ",  "Reviews (0.0-5.0) : "]

    for i in range(len(labels)):
        currentLabel = ttk.Label(labelFrame,text=labels[i]) 
        currentLabel.grid(row=i,column=0,sticky=tk.W) 

    userDict1 = {
        "Book Name":tk.StringVar(),
        "Auhor":tk.StringVar(),
        "Number of copies":tk.StringVar(),
        "Price":tk.StringVar(),
        "Issued by":tk.StringVar(),
        "Description":tk.StringVar(),
        "Reviews (0.0-5.0)":tk.StringVar()
    }

    index = 0

    for i in userDict1:
        currentEntryBox = ttk.Entry(labelFrame,width = 40,textvariable = userDict1[i])
        currentEntryBox.grid(row = index,column = 2)
        currentEntryBox.focus()
        index+=1

   
    for child in labelFrame.winfo_children():
        child.grid_configure(padx=35,pady=5)


    def submitAction():
        pass
        ok = 1
        num = [] 
        for i in userDict1:
            if userDict1[i].get() == "":
                mBox.showerror('Warning',"fields Can't be Empty" )
                ok = -1
                break
            num.append(userDict1[i].get())

        if ok==1:
            pass
            with open('libbooks.csv','a',newline='') as wf:
                CSVwriter = DictWriter(wf,fieldnames=['Book Name' , 'Auhor' , 'Number of copies' , 'Price' , 'Issued by' , 'Description' , 'Reviews'],delimiter='|')
                CSVwriter.writerow({
                                        "Book Name":num[0],
                                        "Auhor":num[1],
                                        "Number of copies":num[2],
                                        "Price":num[3],
                                        "Issued by":num[4],
                                        "Description":num[5],
                                        "Reviews":num[6]
                                    })
            mBox.showinfo ('successful',"Book has been added successfully" )

    submitButton = tk.Button(addDataInLabrary,text="  Add  ",command = submitAction)
    submitButton.grid(row = 1,column = 0,padx = 80,pady =10)
    submitButton.configure(foreground = "#ffffff",background = "#000000")

#########################################################################################################
##########################################################################################################


def WorkOnFeedback():

        ttk.Style().configure('Font.TLabelframe',background = "#b3f5e9",foreground = "red")
        FeedbackBox = ttk.LabelFrame(mainApplication,text="  Improvement Box ",style ='Font.TLabelframe')
        FeedbackBox.grid(row = 0,column = 0,padx = 170,pady = 110)


        f = open(f'ADMINfeedback.txt','r')
        f.seek(0)
        Readlines = f.readlines()
        os.remove("ADMINfeedback.txt")
        removedQ = []
        laterQ = []
        ModifiedQ = []
        answerOfModifiedQ = []


        numofQ = len(Readlines)
        # temp = True
        num = 0
        # # for line in Readlines:
        # while temp and num <numofQ:
        #     line = Readlines[num]
        #     num+=1
        # #     temp = False
        # def feedbackDone():
        #     pass

        def eachFeedback(num,numofQ):
            
            if(num == numofQ):
                removeQ0 = len(removedQ)
                laterQ0 = len(laterQ)
                addedQ0 = len(ModifiedQ)
                FeedbackDone = ttk.Label(FeedbackBox,text=f"Great .!!\nyou have worked on all Feedbacks\n\nremoved irrelevant feedbacks : {removeQ0}\nadded for later : {laterQ0}\nfeedbacks accepted : {addedQ0}",font = (12)) 
                FeedbackDone.grid(row=0,column=0,sticky=tk.W,padx=200,pady=30)
                finalWorkOnFeedback(removedQ,laterQ,ModifiedQ,answerOfModifiedQ)
                
                def over():
                    exit()
                doneButton = tk.Button(FeedbackBox,text=" Done ",command = over)
                doneButton.grid(row = 1,column = 0,padx = 220,pady =10 ,sticky=tk.W)
                doneButton.configure(foreground = "#ffffff",background = "#000000")
                return

            line = Readlines[num].strip()
            
            num+=1

            def add():

                ModifiedQ.append(improvedquestion.get())
                answerOfModifiedQ.append(answerForQuestion.get())

                Label01.grid_remove()
                submitButton1.grid_remove()
                submitButton2.grid_remove()
                Label02.grid_remove()
                improvedquestionInput.grid_remove()
                Label03.grid_remove()
                answerForQuestionInput.grid_remove()
                submitButton3.grid_remove()


                eachFeedback(num,numofQ)
            def remove():
                removedQ.append(line)

                Label01.grid_remove()
                submitButton1.grid_remove()
                submitButton2.grid_remove()
                Label02.grid_remove()
                improvedquestionInput.grid_remove()
                Label03.grid_remove()
                answerForQuestionInput.grid_remove()
                submitButton3.grid_remove()
                eachFeedback(num,numofQ)

            def later():
                laterQ.append(line)

                Label01.grid_remove()
                submitButton1.grid_remove()
                submitButton2.grid_remove()
                Label02.grid_remove()
                improvedquestionInput.grid_remove()
                Label03.grid_remove()
                answerForQuestionInput.grid_remove()
                submitButton3.grid_remove()
                eachFeedback(num,numofQ)


            Label01 = ttk.Label(FeedbackBox,text=f"Q : {line}",font = (12)) 
            Label01.grid(row=0,column=0,sticky=tk.W,padx=40,pady=30)

            submitButton1 = tk.Button(FeedbackBox,text="remove",command = remove)
            submitButton1.grid(row = 0,column = 1,padx = 50,pady =10,sticky = tk.W)
            submitButton1.configure(foreground = "#ffffff",background = "#000000")

            submitButton2 = tk.Button(FeedbackBox,text="Later",command =later)
            submitButton2.grid(row = 0,column = 1,padx = 50,pady =10,sticky = tk.E)
            submitButton2.configure(foreground = "#ffffff",background = "#000000")


            Label02 = ttk.Label(FeedbackBox,text=f"Improved question : ",font = (12)) 
            Label02.grid(row=1,column=0,sticky=tk.W,padx=40,pady=10)

            improvedquestion = tk.StringVar()
            improvedquestionInput = ttk.Entry(FeedbackBox,width = 40,textvariable = improvedquestion)
            improvedquestionInput.grid(row = 1,column = 1,padx=20,pady=10)
            improvedquestionInput.focus()

            Label03 = ttk.Label(FeedbackBox,text=f"Answer for question : ",font = (12)) 
            Label03.grid(row=2,column=0,sticky=tk.W,padx=40,pady=10)

            answerForQuestion = tk.StringVar()
            answerForQuestionInput = ttk.Entry(FeedbackBox,width = 40,textvariable = answerForQuestion)
            answerForQuestionInput.grid(row = 2,column = 1,padx=20,pady=10)
            answerForQuestionInput.focus()

            submitButton3 = tk.Button(FeedbackBox,text="   Add   ",command = add)
            submitButton3.grid(row = 3,column = 1,padx = 120,pady =10 ,sticky=tk.W)
            submitButton3.configure(foreground = "#ffffff",background = "#000000")

        eachFeedback(0,numofQ)

        def finalWorkOnFeedback(removedQ,laterQ,ModifiedQ,answerOfModifiedQ):
            # print(removedQ)
            # print(laterQ)
            # print(ModifiedQ)
            # print(answerOfModifiedQ)


            removedQ = []
            f = open(f'ADMINfeedback.txt','a')
            for line in laterQ:
                f.write(f"{line}\n")
            f.close()

            addedQ1 = len(ModifiedQ)
            f = open(f'info.txt','a')
            for i in range(addedQ1):
                f.write(f"{ModifiedQ[i]} : {answerOfModifiedQ[i]} : \n")
            f.close()

        # for line in lines:
        #     Key,Value,a1 = line.split(" : ")
        #     if(Key.lower() == "password"):
        #         passwordValue = Value


####################################################################################
####################################################################################
####################################################################################
####################################################################################
######

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




def SignUpForm(userName,password):
    name = userName
    ttk.Style().configure('Font.TLabelframe',background = "#b3f5e9",foreground = "red")
    Signupnext = ttk.LabelFrame(mainApplication,text="  Sign up Form ",style='Font.TLabelframe')
    Signupnext.grid(row = 0,column = 0,padx = 275,pady = 30)
    labelFrame = ttk.LabelFrame(Signupnext,text="   please Enter your details here !   ",style='Font.TLabelframe')
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
                if(rawQ in lists.empty):
                    answer = f"{robo} : Sorry you haven't entered anything, Please try again !"
                    Actions.chatUpdate(answer,1)
                elif (rawQ in lists.no):
                    answer = f"{robo} : ok alright , let's discover more things!"
                    Actions.chatUpdate(answer,1)   
                elif (rawQ in lists.yes):
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
                if(rawQ in lists.empty):
                    answer = f"{robo} : Sorry you haven't entered anything, Please try again !"
                    Actions.chatUpdate(answer,1)
                elif (rawQ in lists.no):
                    answer = f"{robo} : ok alright , let's discover more things!"
                    Actions.chatUpdate(answer,1)   
                elif (rawQ in lists.yes):
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
                if(rawQ in lists.empty):
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
                if(rawQ in lists.empty):
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
                if(rawQ in lists.empty):
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
    ageInputBox.focus()
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
    for word in lists.userCall:
        if(word in userquestion.lower()):
            own = 1
    for word in lists.welcomeGreetings1:
            if(word in userquestion.lower()):
                return (f"{robo} : {word.title()} buddy  ")
    

    if("photo" in userquestion.lower() or "image" in userquestion.lower()):
        for word in lists.imejas:
            if(word in userquestion.lower()):
                # try:
                    try:
                        img = mpimg.imread(f'images/{word}.png')
                    except FileNotFoundError:
                        img = mpimg.imread(f'images/{word}.jpg')
                    imgplot = plt.imshow(img)
                    plt.show()
                    return(f"{robo} : and here we go!!")

        return(f"{robo} : Sorry !! photos are not available")
            

    for word in lists.welcomeGreetings:
        if(word in userquestion.lower()):
            return(f"{robo} : {random.choice(lists.welcomeGreetingResponces)}")
    for word in lists.exitGreetings:
        if(word in userquestion.lower() or status == 0):
            return(f"{robo} : Ok Byeee.! Have a nice day")
            
    for word in lists.information:
        if((word in userquestion.lower())):
            f = open(f'info.txt','r+')
            found = 0 
            f.seek(0)
            lines = f.readlines()
            f.close()
            num = 0
            for line in lines:
                # print(line)
                Key,Value,a1 = line.split(" : ")
                if(Key.lower() == word.lower()):
                    found =1
                    return(f"{robo} : {Value}")  
    for word in lists.updateData:
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
    for word in lists.saveData:
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


    for word in lists.askData:
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
                    if("my " in Key):
                        a1,Key =  Key.split("my ")
                    return(f"{robo} : {Key} - {Value}")
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


    for word in lists.options:
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
        if ("twitter" in userquestion.lower()):
            t1 = ("site","https://twitter.com/iitdhrwd",f"{robo} : Opening twitter..")
            return t1
        if ("intranet" in userquestion.lower()):
            t1 = ("site","http://intranet.iitdh.ac.in:81/",f"{robo} : Opening Intranet..")
            return t1
        if ("more about college" in userquestion.lower()):
            t1 = ("site","https://www.collegepravesh.com/engineering-colleges/iit-dharwad/",f"{robo} : Opening collagepravesh.com")
            return t1
        if ("portal" in userquestion.lower()):
            t1 = ("site","http://portal.iitdh.ac.in/asc/index.jsp",f"{robo} : Opening IIT Dharwad Portal")
            return t1
        if ("moddle" in userquestion.lower()):
            t1 = ("site","https://moodle2.iitdh.ac.in/my/", f"{robo} : Opening moodle")
            return t1
        if ("news" in userquestion.lower()):
            t1 = ("site","https://timesofindia.indiatimes.com/topic/IIT-Dharwad",f"{robo} : Opening news")
            return t1
        if ("quora"  in userquestion.lower() or "query" in userquestion.lower()):
            t1 = ("site",f"https://www.quora.com/search?q={userquestion}",f"{robo} : Opening quora..")
            return t1
        if ("train" in userquestion.lower() or "flight" in userquestion.lower()):
            t1 = ("site","https://railways.makemytrip.com/listing?date=20191120&srcStn=SBC&srcCity=Benguluru&destStn=DWR&destCity=Dharwar&classCode=",f"{robo} : Opening make my trip..")
            return t1
        if ("hotel" in userquestion.lower()):
            t1 = ("site","https://www.makemytrip.com/hotels/hotel-listing/?checkin=11202019&checkout=11222019&roomStayQualifier=2e0e&city=XZQ&country=IN&type=CTY&searchText=Dharwad&visitorId=628f4b8d-399c-4531-84c3-fc1c79c4b953",f"{robo} :Opening make my trip..")
            return t1
############################################################e########################################## 

# Unable to interpret 

    # print(f"{robo} : Sorry I am not able to answer this !")

    f1 = open("ADMINfeedback.txt","a")
    var,a1 = userquestion.split(" : ")
    f1.write(f"\n{a1}")
    f1.close()


    t1 = ("exit",f"{robo} : Sorry I am not able to answer this !",f"{robo} :  your question has been added in feedback for Admin, Still you can get more info here :")
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

# def adminSection():
#     print("In admin section ")