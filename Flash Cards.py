##******************
## Flash Cards
## Developed by: Ian Johnson
## Version 0.1
##
## Purpose:
## To import a formatted text file, generate a list from that file, then quiz the user on the data in the file
##******************

import random	## Allows the program to randomly choose questions

## Define variables
score = 0		## Score
q = 0			## Question number
numOfQ = 0		## Number of questions per round
run = True		## Boolean to control runtime of the quiz
x = 0			
att = 0			## Number of attempts
quiztab = []	## List of quiz data from the provided file
scores = []		## List of all scores

## Display welcome message
print("Welcome to Flash Cards!")
print("This is a tool designed to help you study information that requires matching.")
print("When prompeted, enter the name of the text file ending with \".txt\" The program will then generate a list with the quiz information and will begin the quiz.")
print("When you are done, type \"done\" for your answer and your score will be displayed.")

filename = input("Please enter the name of the quiz file: ")		## Save name of file from the user
numOfQ = int(input("Enter the number of questions per round: "))	## Save numOfQ as an int
print("\n")

## Create the list to draw questions from
with open(filename, 'r') as infile:
	for line in infile:
		line = line.strip()		## Removes newline character from file line
		prt1, prt2 = line.split(" ")	## Split on whitespace
		quiztab.append(prt1)	## Add first part to the list
		quiztab.append(prt2)	## Add second part to the lsit

## This block of code is the main code block for the quiz
while (run == True):
	## This is the block of code that ends the quiz
	if q == numOfQ:		## Checks the question number
		att += 1	## Increase the number of attempts by 1
		fatt = 'Attempt #' + str(att) + ':'			## Creates a variable for output of attempt number		
		fscore = str(score) + ' out of ' + str(q)	## Creates variable for output of final score
		scores.append(fatt)		## Adds the new attempt count to the list
		scores.append(fscore)	## Adds the final score to the list
		for s in scores:
			print(s)	## Prints the scores of all attempts
		print("\n")
		
		## Reset question and score variables
		q = 0
		score = 0
	
	q += 1		## Increment question number
	x = random.randrange(len(quiztab))	## Choose a random number of an index in range 0 to length of list
	
	print('Question', q)	## Display question number
	
	ans = input(str(quiztab[x]) + ' ')	## Display the information at the randomly chosen index
	
	
	## Determine the approriate answer
	if x % 2 == 0:	## If the value the computer chose is even ...
	
		correctelem = quiztab[x + 1]	## ... correctelem equals the next element in the list
	
	elif x % 2 != 0:	## If the value the computer chose is odd ...
	
		correctelem = quiztab[x - 1]	## ... correctelem equals the previous element in the list
	
	
	## Determine what to do based on user's response
	if ans == "done":		## If user enters 'done' for answer
		print(score, 'out of', q - 1)	## display score
		run = False		## Sets run to False, which kills the while loop
	
	elif ans == correctelem:	## Compare the correct entry with the user's input
		print("Correct\n")		## Print 'Correct'
		score += 1		## Increase score by 1
	
	else:		## Run this if the user's answer is wrong
		print('Wrong')		## Tells the user they were wrong
		print('You said:', ans)		## Displays the user's answer
		print('Correct answer:',correctelem, '\n')		## Tells the user the correct answer so that they learn for the next time