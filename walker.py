import time
import sys

def qtype(text):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.05)
	text = input()
	return text
	
def type(text):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.05)

# Main Program
answer = qtype("Are you feeling Alone?\n").lower() 
if answer == "yes":
	type("You are not alone")
	time.sleep(0.75)
	file = open("Wk.txt","r")
	w = file.read()
	print("\n\33[1;96;40m",w)
	time.sleep(0.5)
	type("\nGetting your co-ordinates...")
	time.sleep(0.75)
	type("\nSending portal request...")
	time.sleep(0.75)
	type("\nTeleporting you to Walker dimension in ....3")
	time.sleep(1)
	type("....2")
	time.sleep(1)
	type("....1")
	time.sleep(0.5)
	type("\nYou have been teleported to Walker dimension. ")
	time.sleep(0.75)
	type("\nAnd always remember \33[1;32;40m#YouAreNotAlone")
	time.sleep(0.75)
	type("\n\n\t\t\t\33[1;94;40m   <Alan Walker>")
elif answer =="no":
	type("Good! Never think you are alone")
	quit()
else:
	type("I think you should type either Yes or No")