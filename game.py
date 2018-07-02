
a=[0,0,0,0,0,0,0,0,0]

"""
def display(val):
	

"""
def initialize():
	for i in range(9):
		a[i]=0

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
		for i in [0,2] :
			if a[i]==val:
				if a[i+6]==val:
					win=True
	return win

def update(inn,val):
	a[inn-1]=val
	#display(val)

def won(winner):
	print("Player",str(winner),"won!!")
	play_again()

def play_again():
	ch=input("Want to play again")
	if ch=='yes':
		start()
	else:
		quit()

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

def start():
	initialize()
	while True:
		for i in [1,2]:
			print("Player",i,":")
			in2=int(input("Enetr a value"))
			if validate(in2):
				update(in2,i)
				if check(i):
					won(i)
				if tie():
					print("Looks like no one won :(")
					play_again()
			else:
				print("Space already occupied :(")
				play_again()

start()



		



