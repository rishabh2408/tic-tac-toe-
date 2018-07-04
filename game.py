from os import system,name
a=[0,0,0,0,0,0,0,0,0]

def clear():
	if name=='nt':
		_=system('cls')
	else:
		_=system('clear')
def display():
	countt=0
	for j in [6,3,0]:
		countt+=1
		count=0
		for i in [j,j+1,j+2]:
			count+=1
			if a[i]==0:
				print("   ",end="")
			elif a[i]==1:
				print(" X ",end="")
			else:
				print(" O ",end="")
			if count<=2:
				print("|",end="")
		if countt<=2:
			print("\n-----------")
	print("")		

def layout():
	clear()
	print("*****BASIC LAYOUT FOR GAME*****\n\n")
	countt=0
	for j in [6,3,0]:
		countt+=1
		count=0
		for i in [j,j+1,j+2]:
			count+=1
			print(" ",i+1," ",end="")			
			if count<=2:
				print("|",end="")
		if countt<=2:
			print("\n----------------")
	print("\n\n")		
	print("Player 1 entry will be shown as 'X'\nPlayer 2 entry will be shown as 'O'\n\n")

def initialize():
	for i in range(9):
		a[i]=0
	layout()

def check(val):
	win=False
	for i in [0,3,6] :
		if a[i]==val:
			if a[i+1]==val:
				if a[i+2]==val:
					win=True
	for i in [0,1,2] :
		if a[i]==val:
			if a[i+3]==val:
				if a[i+6]==val:
					win=True
	if a[4]==val:
		for i in [0,2]:
			if a[i]==val:
				if a[8-i]==val:
					win=True
	return win

def update(inn,val):
	a[inn-1]=val
	display()

def won(winner):
	print("Player",str(winner),"won!!")
	play_again()

def play_again():
	ch=input("Want to play again: ")
	if ch.lower() =='yes' or ch.lower() =='y' or ch=='True' or ch=='1':
		start()
	else:
		exit()

def tie():
	count=0
	for i in range(9):
		if a[i]!=0:
			count+=1
	if count==0:
		return True

def validate(inn):
	if a[inn-1]==0:
		return True
	else:
		return False	

def play(i):
	print("Player",i,":")
	try:
		in2=int(input("Enetr a value"))
		if in2>=1 and in2<=9:
			if validate(in2):
				update(in2,i)
				if check(i):
					won(i)
				if tie():
					print("Looks like no one won :(")
					play_again()						
			else:
				print("Space already occupied :(")
				play(i)
		else:
			print("Invalis input try again")
			play(i)
	except SystemExit:
		quit()
	except ValueError:
		print("You entered an invalid input")
		play(i)
	

def start():
	initialize()
	while True:
		for i in [1,2]:
			play(i)
	
if __name__ == "__main__":             #will automatically start the game if you use this file seprately if you want to start this game from your own file just call the start() function and rest will be taken care of		
	start()



		



