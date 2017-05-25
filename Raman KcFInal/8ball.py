# coding: utf-8
import random 

while True:  #if true, get asked to enter a question and then a random answer wil appear when answered
        eight_question = raw_input('Please ask a question and press enter: ')#asks question
	eight_ball = ['Signs point to yes.','Yes.','Reply, hazy, try again.','Without a doubt.','My sources say no.','As I see it, yes.','You may rely on it.','Concentrate and ask again.','Outlook not so good.','It is decidedly so.','Better not tell you now.','Very doubtful.','Yes - definitely.','It is certain.','Cannot predict now.','Most likely.','Ask again later.','My reply is no.','Outlook good.','Don\'t count on it.']#respones picked randomly from list
        eight_answer = random.choice(eight_ball)##random choice of response from list
	print(eight_answer)#print the eightball response
	print('\n')#print question please ask a question again