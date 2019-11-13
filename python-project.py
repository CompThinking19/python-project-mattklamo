#This program is going to be a interactive questionaire to determine whether a person is going to make the right choice when it comes to drinking and driving
#A function is going to be created in order to get this interactive game going, and a dictionary is also going to be made for this case
#Based off the answers they give to the questions they answer, it will determine if they are going to make the right choice or not. Using the data from this sheet to determine if they know the  rules  to driving while intoxicated
#Using a boolean, if more than half the results are true then they are making a good decision, but if half are false, then they are making a bad descion
#Mostly the question would consist of True or false questions with some multiple choice so the end can be determined.
#After they do the quiz, there is going to be a visual at the end to show the amount of accidents happen and the deaths the resulted
#def drunk_accidents(Quiz):
    score = 0
    print "Welcome to the drunk driving test!"
    print " "
    print " A.) .08 BAC"
    print " B.) .05 BAC"
    print " C.) The limit is zero"
    Question_1  = raw_input("Question 1: What is the legal limit for BAC")
    #Defining the question and using the users Raw input so that we can see if they got the right answer or not.
    #The code below is seeing if they type in the right answer, and using both cases of A incase they do think the quiz is case sensative
    if Question_1 == "A" or "a":
        score = score + 1
    #At the end of the quiz, the score is going to determine if they got a majority of the questions right, to see if they passed.
    else:
        score = score + 0
    print " "
    print " A.) December "
    print " B.) July"
    print " C.) March"
    Question_2  = raw_input("Question 2: What month do drunk driving accidents occur the most ")
    if Question_2 == "B" or "b":
        score = score + 1
    else:
        score = score + 0
    print " "
    print " A.) Motorcycle "
    print " B.) Car"
    print " C.) Trucks"
    Question_3  = raw_input("Question 3: What type of motorvehicle get into more drunk driving accidents ")
    if Question_3 == "A" or "a":
        score = score + 1
        print "In 2016, drunk driving accidents by vehicle type were 25 percent for motorcycles, 21 percent for passenger cars, and 20 percent for the “light trucks” category (22% for pickup trucks, 19% for SUVs, and 12% for vans)."
    else:
        score = score + 0
        print "In 2016, drunk driving accidents by vehicle type were 25 percent for motorcycles, 21 percent for passenger cars, and 20 percent for the “light trucks” category (22% for pickup trucks, 19% for SUVs, and 12% for vans)."
    print " "
    print " A.) 16-20 "
    print " B.) 35-44"
    print " C.) 21-24"
    Question_4  = raw_input("Question 4: Which driving age range causes the most drunk driving accidents ")
    if Question_4 == "C" or "c":
        score = score + 1
    else:
        score = score + 0
    print " "
    print " A.) Texas "
    print " B.) Florida "
    print " C.) California"
    Question_5  = raw_input("Question 5: Which state has the most fatalties due to drunk driving  ")
    if Question_5 == "A" or "a":
        score = score + 1
    else:
        score = score + 0
    if score >= 4:
    #At the end due to there being 5 questions, we need to make sure that the user gets 4 out of 5 to pass so we know they got a jist of what the quiz is
        print "You passed! It  is very important to know what drunk driving could do, and how lethal it is."
    else:
        print "You did not pass! Learning the information about drunk driving is urgent, because one day it will help prevent you from ending the life of someone else"
#The end of the code is going to print the statistics of drivers that get into drunk driving accidents
class Questions:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
#question_prompts is going to take in all the questions for the quiz and display the questions along wiht the answers for this multiple choice quiz
question_prompts = [
     "Question 1:What is the legal limit for BAC?\n(a).08 BAC\n(b).05 BAC\n(c)The limit is zero",
     "Question 2:What month do drunk driving accidents occur the most?\n(a) March\n(b)July\n(c)Decemeber",
     "Question 3:What type of motorvehicle get into more drunk driving accidents?\n(a) Motorcyle\n(b)Car\n(c)Trucks",
     "Question 4:Which driving age rangbe causes the most drunk driving accidents?\n(a)16-20\n(b)35-44\n(c)21-34",
     "Question 5:Which state has the most fatalities due to drunk driving?\n(a)Texas\n(b)Flordia\n(c)California",
]
#questions_done is going to go through each prompt of the questions and make sure it has an answer that correlates correctly with the question
questions_done = [
     Questions(question_prompts[0],"a"),
     Questions(question_prompts[1],"b"),
     Questions(question_prompts[2],"a"),
     Questions(question_prompts[3],"c"),
     Questions(question_prompts[4],"a"),
]

def quiz(questions_done):
     score = 0
     for questions in questions_done:
          answer = raw_input(questions.prompt)
          if answer == questions.answer:
               score = score + 1
     if score >= 4:
        print("You passed! You got", score, "out of", len(questions_done), "It is very important to know what drunk driving could do, and how lethal it is.")
     else:
        print("Oh no!! You failed. You got", score, "out of", len(questions_done), "Learning the information about drunk driving is urgent, because one day it will help prevent you from ending the life of someone else")

quiz(questions_done)

print "For every skull, 1,000 people died in a drunk driving accident:"
text = ""
#The range prints the skull 10 times due to the amnoutof drunk driving accidents that happen per 1000
for fatalties in range(10):
    print "💀",
print ""
print "For every car, an accident has occured:",
#The range prints the car 10 times due to the amnoutof drunk driving accidents that happen per 1000
for accidents in range(40):
    text = text + str(fatalties)
    print "",
    print "🚘",
print ""
print "1 out of 4 accidents are caused due to drunk driving, and as an end result; DEATH",
