# -*- coding: utf-8 -*-
#This program is going to be a interactive questionaire to determine whether a person is going to make the right choice when it comes to drinking and driving
#A function is going to be created in order to get this interactive game going, and a dictionary is also going to be made for this case
#Based off the answers they give to the questions they answer, it will determine if they are going to make the right choice or not. Using the data from this sheet to determine if they know the  rules  to driving while intoxicated
#Using a boolean, if more than half the results are true then they are making a good decision, but if half are false, then they are making a bad descion
#Mostly the question would consist of True or false questions with some multiple choice so the end can be determined.
#After they do the quiz, there is going to be a visual at the end to show the amount of accidents happen and the deaths the resulted
class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
#questions is going to take in all the questions for the quiz and display the questions along wiht the answers for this multiple choice quiz
questions = [
     "Question 1:What is the legal limit for BAC?\n(a).08 BAC\n(b).05 BAC\n(c)The limit is zero",
     "Question 2:What month do drunk driving accidents occur the most?\n(a) March\n(b)July\n(c)Decemeber",
     "Question 3:What type of motorvehicle get into more drunk driving accidents?\n(a) Motorcyle\n(b)Car\n(c)Trucks",
     "Question 4:Which driving age rangbe causes the most drunk driving accidents?\n(a)16-20\n(b)35-44\n(c)21-34",
     "Question 5:Which state has the most fatalities due to drunk driving?\n(a)Texas\n(b)Flordia\n(c)California",
]
#answers is going to go through each prompt of the questions and make sure it has an answer that correlates correctly with the question
answers = [
     Question(questions[0],"a"),
     Question(questions[1],"b"),
     Question(questions[2],"a"),
     Question(questions[3],"c"),
     Question(questions[4],"a"),
]

def quiz(answers):
     score = 0
     for question in answers:
          answer = raw_input(question.prompt)
          if answer == question.answer:
               score = score + 1
     if score >= 4:
        print("You passed! You got", score, "out of", len(answers), "It is very important to know what drunk driving could do, and how lethal it is.")
     else:
        print("Oh no!! You failed. You got", score, "out of", len(answers), "Learning the information about drunk driving is urgent, because one day it will help prevent you from ending the life of someone else")

quiz(answers)

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
