import requests
from time import sleep as sleep
import sys,os

isFirst = True

banner = """
\x1b[1;32;40m]=<*>=<*>=\x1b[1;32;41m[ P H C - M A K I B O T ]\x1b[1;32;40m=<*>=<*>=[\x1b[0m
\x1b[0;30;42m             Bitland Pro Script              \x1b[0m
\x1b[1;32;40m]===========================================[\x1b[0m
"""

#Start of the program
os.system("clear")#Refresh The Command Prompt

#Display the banner with animation
for char in banner:
	sys.stdout.write(char)
	sys.stdout.flush()
	sleep(0.01)

user_email = input("Bitland Email : ")#Ask for Email Address
user_password = input("Bitland Pass  : ")#Ask for Password

#Function to get the current timer
def count_down(claim):
	status = ""
	claim = claim.replace("{"," ")#Removing Brackets
	claim = claim.replace("}"," ")#Removing Brackets
	claim = claim.replace(":"," ")#Removing Colon
	claim = claim.replace(","," ")#Removing Coma
	claim = claim.replace("\\"," ")#Removing Coma
	claim = claim.replace("\/"," ")#Removing Coma
	claim = claim.split("\"")#Split words between " Brakets

	for l, word1 in enumerate(claim):#Looping on the arraly list
		if word1 == "desc":#Searching for word in array list
			status = claim[l+2]#Getting the response
			break
		l += 1

	print(status)#Displaying the response

	for x, word in enumerate(claim):#Looping on the arraly list
		if word == "seconds_to_bonus":#Searching for word in array list
			seconds = claim[x+1]#Getting the current count down
			break
		x += 1
	
	for i in range(int(seconds)):#Looping the count down
		sleep(1)#Freeze the code for 1 seconds
		print(" - > Next claim after " + str(seconds) + " seconds             ",end="\r")#Dispalying the countdown Text in the same line
		seconds = int(seconds) - 1 #Decreasing the seconds

#Function to get USERS IP and COUNTRY
def get_info(info):
	ip = "a"
	country = "a"
	info = info.replace("{"," ")#Remove Brakets
	info = info.replace("}"," ")#Remove Brakets
	info = info.replace(":"," ")#Remove Colon
	info = info.replace(","," ")#Remove Coma
	info = info.split("\"")#Split words between " Brakets

	for c, word in enumerate(info):#Looping on the array list
		if word == "cfIP":#Searching word on the array list
			ip = "YOUR IP : " + info[c+2]#Getting the value
			break
		c += 1
	
	for z, word in enumerate(info):#Looping on the array list
		if word == "cfCountry":#Searching word on the array list
			country = "\nCOUNTRY : " + info[z+2]#Getting the value
			break
		z += 1

	for char in ip:#Looping each char in string
		sys.stdout.write(char)#Printing each Char
		sys.stdout.flush()#Refreshing the terminal
		sleep(0.1)#Freezing the program for 1 seconds

	for char in country:#Looping each char in string
		sys.stdout.write(char)#Printing each Char
		sys.stdout.flush()#Refreshing the terminal
		sleep(0.1)#Freezing the program for 1 seconds

	barrier = "\n\x1b[1;32;40m]=====================[\n"
	for char in barrier:#Looping each char in string
		sys.stdout.write(char)#Printing each Char
		sys.stdout.flush()#Refreshing the terminal
		sleep(0.07)#Freezing the program for 1 seconds
	sleep(5)

def login(user_email,user_password):
	global isFirst
	s = requests.session()#Getting a new session
	data = {"username": user_email,"password": user_password}#Building the data form
	headers = {"Connection":"close"}#Disabling Keep-Alive Connection
	logout = s.get("https://bitland.pro/users/logout",headers=headers)#Logging out the account from web
	sleep(1)
	main = s.get("https://bitland.pro/cryptoplace.cloud",headers=headers)#Opening the main page
	sleep(1)
	login = s.post("https://bitland.pro/users/login", headers=headers, data=data)#Sending a login data
	sleep(1)
	claim = s.get("https://bitland.pro/bonus/get_bonus")#Claiming the bonus
	sleep(1)
	if login.text.find("Successful authorization"):#Searching Words from the response on login
		print("\x1b[1;32;40mSuccessfully Logged in . . . . . . !\x1b[0m")
	else:
		print("Incorrect Email or Password")

	if isFirst:
		get_info(login.text)#Print the info on the first run
		isFirst = False

	count_down(claim.text)#Getting the CountDown

os.system("clear")#Clear the Terminal

#Display the banner
for char in banner:
	sys.stdout.write(char)
	sys.stdout.flush()
	sleep(0.01)

#execute the login function!
while True:
	login(user_email,user_password)#Passing parameters to login function
