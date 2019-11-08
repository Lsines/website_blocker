import sqlite3



host_path= r"C:\Windows\System32\drivers\etc\hosts"  #actual host path
host_temp = r"C:\Users\sital\Desktop\Learning pythom\website blocker\hosts" #to test the functionality of program

redirect = "127.0.0.1" #address to redirect to

#creates the database blocked with block table to store website that are blocked.
def connect():
    conn = sqlite3.connect("blocked.db")
    cur = conn.cursor()
    cur. execute("CREATE TABLE IF NOT EXISTS block(website TEXT PRIMARY KEY unique)") # website is a primary unique key.
    conn.commit()
    conn.close()

website_list = [] #list of website to be blocked

# appends website we get from entery widget to website list
def addWebsite(website):
    website_list.append(website) 
    
    conn = sqlite3.connect("blocked.db")
    cur = conn.cursor()
    cur.execute("INSERT or IGNORE INTO block VALUES(?)",(website,)) #does not insert if alreadt there.. use of ignore//
    conn.commit()
    conn.close()

#deletes the website from the database
def deleteWebsite(website):
    conn = sqlite3.connect("blocked.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM block WHERE website =?",(website,))
    conn.commit()
    conn.close()

    with open(host_path,'r+') as file:
                content=file.readlines()
                
                
                file.seek(0) #starts at the begining of file
                for lines in content:
                    if not any(website in lines for website in website_list):  # if the website to be unblocked is not in the line of the file then write the file
                        file.write(lines) #rewriting the  file without the website
                file.truncate() #the rewritten file is above the originial,,truncates truncates the original..hence blocked website is unvlocked



# returns all the website from databse that have been blocked 
def blocked_list():
    blocked_list = website_list.copy()  # i dont need this
    conn = sqlite3.connect("blocked.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM block")
    rows = cur.fetchall()
    conn.close()
    return rows


#meat and potates of the script.
def block(x): 
        #run this part of the code if x is zero
        if x==0:  
            print("Working hours")
            #opens the host file as r+ as file variable
            with open(host_path,'r+') as file: #r+ cursor at the end of file
                content = file.read() #reads the line of file
                
                for sites in website_list: #extarct each website from website list
                    if sites in content: # if the website is already in the host file do nth
                        pass
                    else:
                        file.write(redirect+" "+sites+"\n") #write in file with redirect address and website name

        # if x == 1 which means unblock
        else:
            print("use that site")
            #same open read
            with open(host_path,'r+') as file:
                content=file.readlines()
                
                
                file.seek(0) #starts at the begining of file
                for lines in content:
                    if not any(website in lines for website in website_list):  # if the website to be unblocked is not in the line of the file then write the file
                        file.write(lines) #rewriting the  file without the website
                file.truncate() #the rewritten file is above the originial,,truncates truncates the original..hence blocked website is unvlocked


connect() 



