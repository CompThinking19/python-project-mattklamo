# -*- coding: utf-8 -*-
#This program is going to be a interactive questionaire to determine whether a person is going to make the right choice when it comes to drinking and driving
#A function is going to be created in order to get this interactive game going, and a dictionary is also going to be made for this case
#Based off the answers they give to the questions they answer, it will determine if they are going to make the right choice or not. Using the data from this sheet to determine if they know the  rules  to driving while intoxicated
#Using a boolean, if more than half the results are true then they are making a good decision, but if half are false, then they are making a bad descion
#Mostly the question would consist of True or false questions with some multiple choice so the end can be determined.
#After they do the quiz, there is going to be a visual at the end to show the amount of accidents happen and the deaths the resulted
class Question:
     def __init__(self, prompt, answer):
         #the __init__ functon is going to take 3 arguments that are going to run through the prompt, and the answer to initialized them through the class that will be used for when it is time to run the quiz function of the code.
          self.prompt = prompt
          self.answer = answer
#questions is going to take in all the questions for the quiz and display the questions along with the answers for this multiple choice quiz. This is an important part due to this being a bulk of the quiz itself. Without the question list, there would be no quiz at all.
questions = [
     "Question 1:What is the legal limit for BAC?\n(a).08 BAC\n(b).05 BAC\n(c)The limit is zero",
     "Question 2:What month do drunk driving accidents occur the most?\n(a) March\n(b)July\n(c)Decemeber",
     "Question 3:What type of motorvehicle get into more drunk driving accidents?\n(a) Motorcyle\n(b)Car\n(c)Trucks",
     "Question 4:Which driving age range causes the most drunk driving accidents?\n(a)16-20\n(b)35-44\n(c)21-34",
     "Question 5:Which state has the most fatalities due to drunk driving?\n(a)Texas\n(b)Flordia\n(c)California",
     "Question 6:What percentage of drivers were driving while intoxicated when they caused an accident?\n(a)25%\n(b)32%\n(c)38%",
     "Question 7:Which BAC level caused the most accidents?\n(a).08 BAC\n(b).16 BAC\n(c).22 BAC",
     "Question 8:How much money in damages has drunk driving accidents caused in 2015?\n(a)44 Billion\n(b)50 Billion\n(c)36 Billion",
     "Question 9:Of the 1,114 crashes that children were killed due to drunk driving, how many were due to drunk driving?\n(a)150\n(b)570\n(c)220",
     "Question 10:What percentage of drunk driving accidents happen at night?\n(a)70%\n(b)82%\n(c)67%",
]
#answers is going to go through each prompt of the questions and make sure it has an answer that correlates correctly with the question. Another very important part of the code, because the answers are needed to see if the user was able to input the right answer.
answers = [
     Question(questions[0],"a"),
     Question(questions[1],"b"),
     Question(questions[2],"a"),
     Question(questions[3],"c"),
     Question(questions[4],"a"),
     Question(questions[5],"b"),
     Question(questions[6],"b"),
     Question(questions[7],"a"),
     Question(questions[8],"c"),
     Question(questions[9],"a"),
]
def quiz(answers):
     score = 0
     #score equal to zero due to it being added by 1 each time the user inputs the right answer
     for question in answers:
          answer = raw_input(question.prompt)
          if answer == question.answer:
              #with the users raw input, need to see if the answer that put is equal to the answer in the answers list. If there answer does equal the correct then the score variable will go up 1
               score = score + 1
          else:
              print("Incorrect! Sorry")
     if score >= 8:
         # the score has to be greater than 8 so that the user can know if they really got a jist of the information that was displayed throughout the quiz. It is an important takeaway from the program if they are able to take away information that they did not know prior to taking the quiz.
        print("You passed! You got", score, "out of", len(answers), "It is very important to know what drunk driving could do, and how lethal it is.")
     else:
        print("Oh no!! You failed. You got", score, "out of", len(answers), "Learning the information about drunk driving is urgent, because one day it will help prevent you from ending the life of someone else")

quiz(answers)

print " There has been 10,874 deaths due to drunk driving. 25% of of motorvehicle accident fatalties are due do drunk driving. For every skull, 1,000 people died in a drunk driving accident:"
text = ""
#The range prints the skull 10 times due to the amnout of drunk driving accidents that happen per 1000 and the clutter  of the skulls would be a lot ot take in, so I wanted the range keyword to only print 10 skulls.
for fatalties in range(10):
    print "💀",
print ""
print "There has been 40,000 fatatlies from an accdient in 2017. For every car shown, an accident has occured:",
#The range prints the car 10 times due to the amnoutof drunk driving accidents that happen per 1000 as well as the clutter of the skulls, there would be a clutter of cars. The range function will playe a role in printing the 40 cars for the deaths for better visual.
for accidents in range(40):
    text = text + str(fatalties)
    print "",
    print "🚘",
print ""
print "1 out of 4 accidents fatalities are caused due to drunk driving. Drunk driving is preventable. Do the right thing and do not drink and drive.",
