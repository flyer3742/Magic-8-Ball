#Randomizer to randomly selects a number 
import random
random_number = random.randint(1, 12)
print(random_number)
name = "Eric"
question = "Will there be thunderstorms today?"
answer = ""
#If user does not provide a name code below will run
if len(name) == 0:
  print("Question: " + question)
else:
  print(name + " asks: " + question)
#If user does not provide a question code below will run
if question == "":
  print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)
# if statements 1 - 12 and Error as else
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Don't count on it!"
elif random_number == 11:
  answer = "It looks hopeful."
elif random_number == 12:
  answer = "You can count on it!"
else:
   answer = "Error"
print("Magic 8-Ball's answer: " + answer)
