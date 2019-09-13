import os 
from os import system

print("welcome to python tictactoe game")
table={}
x=[["","",""],["","",""],["","",""]]
#code to enter values into coordinates of table
def enter(count,num):
	print("enter coordinates-min(1,1)&(max 3,3)\n")
	x,y=input("enter position:"),input()
	if x in range(1,4) and y in range(1,4):
		i,j=x-1,y-1
		if(table.has_key((i,j))):
			print("field already filled,ERROR")
			print("wrong input,one more chance")
			count+=1
			if(count<=1):
				enter(count,num)
			else:
				print("sorry chance over")
				if(num==1):
					player(2)
				else:
					player(1)
		else:		
			if(num==1):
				table[(i,j)]="X"
			else:
				table[(i,j)]="O"
		add(i,j)
	else:
		print("wrong input,one more chance")
		count+=1
		if(count<=1):
			enter(count,num)
		else:
			print("sorry chance over")
			if(num==1):
				player(2)
			else:
				player(1)
#switch between players
def player(num):
	print("chance for player",num)
	enter(0,num)

#add the table
def add(i,j):
	for i in range(3):
		for j in range(3):
			if table.has_key((i,j)):
				x[i][j]=table[(i,j)]
			else:
				x[i][j]=" "
	display()
#display the game progress
def display():
	system('clear')
	for i in range(3):
		print("\n")
		for j in range(3):
			print(x[i][j]),
def result(flag):
	if(flag==0):
		print("\n")
		print("MATCH DRAWN")
	elif(flag==1):
		print("\n")
		print("PLAYER 1 WON")
	elif(flag==2):
		print("\n")
		print("PLAYER 2 WON") 
	exit()
#game code
def game():
	flag=0
	system('clear')
	for i in range(1,10):
		if(i%2==1):
			player(1)
		else:
			player(2)
		if(x[0][0]==x[1][1]==x[2][2]=="X")or(x[0][2]==x[1][1]==x[2][0]=="X"):
			flag=1
			result(flag)
			break
		if(x[0][0]==x[1][1]==x[2][2]=="O")or(x[0][2]==x[1][1]==x[2][0]=="O"):
			flag=2
			result(flag)
			break
		for i in range(3):
			if(x[i][0]==x[i][1]==x[i][2]=="X") or (x[0][i]==x[1][i]==x[2][i]=="X"):
				flag=1
				result(flag)
				break		
		for i in range(3):
			if(x[i][0]==x[i][1]==x[i][2]=="O") or (x[0][i]==x[1][i]==x[2][i]=="O"):
				flag=2
				result(flag)
				break
		
	result(0)	
#calling function
game()
	
	
