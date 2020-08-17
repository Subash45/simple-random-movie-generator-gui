from tkinter import *
from random import randint

movie_list=[]
count=6
dict1={}
movie=''
rating=0

root=Tk()
root.title("Random Movie Generator")

Enter_text=Label(root,text="Enter the movie and click save").pack()

enter=Entry(root,width=50)
enter.pack()



def rand_rating(movie):
    movie=randint(0,100)
    return movie

def countdown():
    global count
    count-=1
    label_counter.config(text=str(count))
    if(count==0):
        counter_widget.destroy()
    else:
        label_counter.after(1000,countdown)

def deleteLabel():
    label1.destroy()
    #save_movie_bt['state']= NORMAL
    #delete_label_bt['state']=DISABLED
    
def helpButton():
    root1=Tk()
    root1.title("How To Use")
    help_text='''This is a Python GUI Program to help the users to generate a random movie which they will watch Today.
The user needs to enter the movie and click the Save Movie Button to save.
Then they need to click the Delete Label button to delete the Label and to enable the Save movie Button.
After Entering All the Choice Movies simpy click The Generate button to generate a Random movie
Make sure You saved all the movies'''
    help_label=Label(root1,text=help_text).pack()

def saveMovie():
    global label1
    movie_list.append(enter.get())
    enter.delete(0,END)
    #label1=Label(root,text="Movie Saved")
    #label1.pack()
    #delete_label_bt['state']=NORMAL
    #save_movie_bt['state']= DISABLED
    
def generate():
    root.destroy()
   
    
                      #Buttons in root widget
save_movie_bt=Button(root,text="Save Movie",command=saveMovie)
save_movie_bt.pack()

'''delete_label_bt=Button(root,text="Delete Label to Enable Button",command=deleteLabel)
delete_label_bt.pack()
delete_label_bt['state']=DISABLED'''

generate_button=Button(root,text="Generate",command=generate)
generate_button.pack()

help_button=Button(root,text="How To Use",command=helpButton)
help_button.pack()

root.mainloop()

                         #algorithm to generate movie


for i in movie_list:
    rating=rand_rating(i)
    dict1[i]=rating
dict1=dict(sorted(dict1.items(), key=lambda switch: (switch[1],switch[0])))
dict1=dict(reversed(list(dict1.items())))
dict1=list(dict1.items())

for i in dict1:
    movie="The Movie To Watch Today is "+ str(i[0])
    rating="It Got an Random rating of "+ str(i[1])
    break;

counter_widget=Tk()

counter_widget.geometry("200x200")
counter_widget.title("Generating...")
label_counter=Label(counter_widget,text=str(count),font="RomanShiny 50 bold")
label_counter.pack()
countdown()

counter_widget.mainloop()

generated=Tk()
generated.title("Movie Generated!!")
generated.geometry("1000x200")

movie_label=Label(text=movie,font="Verdana 16 bold").pack()
rating_label=Label(text=rating,font="Helvetica 15 bold").pack()

print(movie,"\n",rating,"\n",dict1,"\n")

generated.mainloop()





