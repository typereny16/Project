#Tyleri
import time

print (" --- Connecting to the System ---\n")
time.sleep(1)
print (".....\n")
time.sleep(1)
print (".....\n")
time.sleep(1)
print ("Connection established.\n")

print ("\n------------------")
print ("WELCOME TO TYLERi")
print ("------------------\n")

name = " "
while name.lower() != "jeremy" and name.lower() != "tyler" and name.lower() != "gregg":
	name = input("What is your name? ")
if name.lower() == "tyler":
	t_age = "16"
	t_name = "Tyler Pereny"
elif name.lower() == "jeremy":
	j_age = "17"
	j_name = "Jeremy Hepker"
elif name.lower() == "gregg":
	g_age = "27"
	g_name = "Gregg Neville"
	
def store(*values):
    store.values = values or store.values
    return store.values
store.values = ()

store (16, 17, 27)
t, j, g = store()

def question_choice():
	question = " "
	return question
question = " "
while question.lower() != "how old am i?" and question.lower() != "what is my name?":
	print ("\nGo ahead and ask me a question about yourself", name,)
	question = input("Question:> ")

def check_question(chosen_question):
	print ("\nSearching through the database...\n")
	time.sleep(1)
	print (".....\n")
	time.sleep(1)
	print (".....\n")
	time.sleep(1)
	print ("File found.\n")
	if name.lower() == "tyler" and question.lower() == "how old am i?":
		print ("You are", t_age, "years old.")
	elif name.lower() == "jeremy" and question.lower() == "how old am i?":
		print ("You are", j_age, "years old.")
	elif name.lower() == "gregg" and question.lower() == "how old am i?":
		print ("You are", g_age, "years old.")
	elif name.lower() == "tyler" and question.lower() == "what is my name?":
		print ("Your name is", t_name)
	next_question = input("Press Enter to ask a new question.")

question_again = "yes"
while question_again.lower() == "yes":
	question_number = question_choice()
	check_question(question_choice)

	
