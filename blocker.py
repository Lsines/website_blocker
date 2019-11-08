from tkinter import *
import tkinter as tk
import website_blocker

#Adds the website to the list to block the website
def addToList():
    website= entry_var.get()  # gets the name of the website from the Stringvar which is binded to entry_website widget
    if "www."not in website:  #adds www. infron of website if not added
        website = "www."+website
    website_blocker.addWebsite(website)  #refers to the function in the website_blocker module 
    
    website_blocker.block(0)  # 0 parameter means execute the code inside the website_blocker module that blocks the website from the list



# Helps to view the website that are blocked
def view_blocked():
     list_box.delete(0,END)   #Empities the listbox
     # blocked_list contains all the website that were blocked in a databse in a table
     for rows in website_blocker.blocked_list():
         list_box.insert(END,rows) # adds the name of website in the list
  
   

# these blocks of code are to select the website row from list and dsiplay it in the entry widget for further operations
selected_row = None  #At first none of the rows are selected
def get_selected_row(event):  # the parameter is the event that is binded to the listbox
    global selected_row
    try:
        index = list_box.curselection()[0]  #gets the index of the selected item
        selected_row = list_box.get(index)  #assigns the selected row to slected_row variable
        website.delete(0,END)
        website.insert(END,selected_row)    #adds the selected_row to the website entry
    except:
        IndexError          #if endex erroroccurs dont execute


# gets the value from entry widget and runs the code that unblocks it. also delete from databse
def unblock():
    website= entry_var.get()  
    website_blocker.block(1)
    website_blocker.deleteWebsite(selected_row[0])

       
            
window = Tk()

window.geometry("450x400+0+0")

#Create website label and place it
website_label = Label(window,text = "Website: ")
website_label.place(x = 0, y = 0)
        
entry_var = StringVar()  #variable to store the value in Entry widget
website = Entry(window,width = 60,textvariable=entry_var) #website entry widget
website.place(x = 50,y = 0)


#Buttons to do things
block = Button(window,text = "Block",width = 10,command = addToList)
unblock = Button(window,text = "UnBlock",width = 10,command=unblock)
view_block = Button(window,text = "View Blocked",width = 10,command = view_blocked)
close = Button(window,text = "close",width = 10)
        
block.place(x = 0, y = 50)
unblock.place(x = 100 , y = 50)
view_block.place(x = 200, y = 50)
close.place(x = 300, y = 50)

#Listbox
list_box = Listbox(window,height = 50,width = 65)
list_box.place(x = 0, y = 100)

#Scroll bar
scroll_bar = Scrollbar(window,orient="vertical")
scroll_bar.place (x = 400 , y = 100,height = 50)
scroll_bar.config(command = list_box.yview)  # scrollbar is set to list_box
list_box.config(yscrollcommand=scroll_bar.set)

list_box.bind('<<ListboxSelect>>',get_selected_row)  # a virtual event is being bind to the fnction
        
#Create required buttons



window.mainloop()