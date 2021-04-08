import mysql.connector
from getpass import getpass
from getpass import getuser
from colorama import Fore
db=mysql.connector.connect(host="localhost", user="root", passwd="", database="pocdb") #mysql connection
cursor=db.cursor() #for executing sql queries

username=input("Enter Username: ") #user input
password=input("Enter Password: ")

try:    
    cursor.execute("select * from `users` where `username`=%s and `password`=%s", (username, password)) #fetching results
    res=cursor.fetchone()
except Exception as e:
    print(e)
except KeyboardInterrupt:
    print("^C")
#check 

if res == None:
    print(Fore.RED+"Auth failed")
else:
    print(f"Logged in user: {Fore.GREEN+res[0]+Fore.RESET} with uid: {Fore.GREEN+str(res[2])+Fore.RESET}")
    
    
