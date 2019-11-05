#This program is going to be a interactive questionaire to determine whether a person is going to make the right choice when it comes to drinking and driving
#A function is going to be created in order to get this interactive game going, and a dictionary is also going to be made for this case
#Based off the answers they give to the questions they answer, it will determine if they are going to make the right choice or not. Using the data from this sheet to determine if they know the  rules  to driving while intoxicated
#Using a boolean, if more than half the results are true then they are making a good decision, but if half are false, then they are making a bad descion
#Mostly the question would consist of True or false questions with some multiple choice so the end can be determined.
#After they do the quiz, there is going to be a visual at the end to show the amount of accidents happen and the deaths the resulted
def drunk_accidents(deaths):
score = 0
    print "Welcome to the drunk driving test!"
    print " "
    print " A.) "
    print " B.) "
    print " C.) "
    Question_1  = raw_input("Question 1:  ")
    #Defining the question and using the users Raw input so that we can see if they got the right answer or not.
    #The code below is seeing if they type in the right answer, and using both cases of A incase they do think the quiz is case sensative
    if Question_1 == "A" or "a":
        score = score + 1
    #At the end of the quiz, the score is going to determine if they got a majority of the questions right, to see if they passed.
    else:
        score = score + 0
    print " "
    print " A.) "
    print " B.) "
    print " C.) "
    Question_2  = raw_input("Question 2:  ")
    if Question_2 == "A" or "a":
        score = score + 1
    else:
        score = score + 0
    print " "
    print " A.) "
    print " B.) "
    print " C.) "
    Question_3  = raw_input("Question 3:  ")
    if Question_3 == "A" or "a":
        score = score + 1
    else:
        score = score + 0
    print " "
    print " A.) "
    print " B.) "
    print " C.) "
    Question_4  = raw_input("Question 4:  ")
    if Question_4 == "A" or "a":
        score = score + 1
    else:
        score = score + 0
    print " "
    print " A.) "
    print " B.) "
    print " C.) "
    Question_5  = raw_input("Question 5:  ")
    if Question_5 == "A" or "a":
        score = score + 1
    else:
        score = score + 0
    if score >= 3:
        print "You passed! It  is very important to know what drunk driving could do, and how lethal it is."
    else:
        print "You did not pass! Learning the information about drunk driving is urgent, because one day it will help prevent you from ending the life of someone else"
return drunk_accidents
#The end of the code is going to print the statistics of drivers that get into drunk driving accidents
print "For every skull, 1,000 people died in a drunk driving accident:"
text = ""
for fatalties in range(10):
    text = text + str(fatalties)
    print "💀",
print ""
print ""
print "For every car, an accident has occured:",
for accidents in range(40):
    text = text + str(fatalties)
    print "🚘",
print ""
print "1 out of 4 accidents are caused due to drunk driving, and as an end result; DEATH",
