from tkinter import *
import random

root=Tk()
root.title("Lucky friend wheel")
root.geometry("500x500")

text_input=Entry(root)
text_input.pack()

text_input1=Entry(root)
text_input1.pack()

list1=[]
list2=[]
countryList_lbl=Label(root)
capitalList_lbl=Label(root)
random_number_lbl=Label(root)
countrylbl=Label(root)
capitallbl=Label(root)



random_lucky_friend=""

def add():
    country_name=text_input.get()
    list1.append(country_name)
    countryList_lbl["text"]="Country list: " +str(list1)
    capital_name=text_input.get()
    list2.append(capital_name)
    capitalList_lbl["text"]="Capital list: " +str(list2)
    
def lucky():
    length=len(list1)
    random_number=random.randint(0,length-1)
    random_lucky_friend=list1[random_number]
    random_number_lbl["text"]=str(random_number)
    countrylbl["text"]="country is:" + str(random_lucky_friend)
    random_lucky_friend1=list2[random_number]
    capitallbl["text"]="capital is:" + str(random_lucky_friend1)

btn2=Button(root,text="Add country and capital name", command=add)
btn2.pack()

countryList_lbl.pack()
capitalList_lbl.pack()

btn=Button(root,text="display random country and its capital", command=lucky)
btn.pack()

random_number_lbl.pack()
countrylbl.pack()
capitallbl.pack()




root.mainloop()