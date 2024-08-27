'''
Andy dara vichet
Quiz program verison 2
19/07/2024

This program is a quiz which gives the user a question in which the user has to anwser.

quiz: New Zealand volcano
'''
#do i need to import anything?
import time
#What variables do i need to set up?
list_answer = ['']
name = ''
#this is for the scoring in which will add if u get the questions right.
Question = 0
numbers_question = 5
#do i need a loop to make it work?
loop = True
bool_loopded = False
#computer introduction
name = input('please enter your name: ')

print(f'Hello, {name}. Welcome to my quiz v1.0.')
time.sleep(2)
print("you will be anwsering 5 questions in which you'll be using numbers to anwser.")
time.sleep(2)
print()
print('you get as many trys you like but please dont guess too much :)')
time.sleep(1)
print()
print('Goodluck')
time.sleep(1)

#computer asks you Question1.
Question1 = print("Qt 1: What is the Highest volcano that is stil active in New Zealand to this day?")
print()
loop = True
user_choose = print('''
1. White island/Whakaari
2. Lake Rotorua
3. Mount Ruapehu
4. Mount Taranaki
''')
while bool_loopded is False:
  time.sleep(1)
  user_choose = input("please choose one of the following numbers: ")
  if user_choose == "3":
    print("correct")
    list_answer.append("correct")
    #question adds 1
    Question += 1
    print("score:",Question)
    print()
    bool_loopded = True
  elif user_choose != 3 or user_choose.isalpha():
    print("incorrect, anwser is '3'")
    bool_loopded = True
  else:
    print("invaild anwser")
  print()
time.sleep(1)

#Computer asks Question 2
Question2 = print("Qt 2: which volcano is the youngest in NZ? ")
user_choose = print('''
1. Rangitoto
2. Raoul Island
3.Mount Ngauruhoe
4.Mount Tarawera
''')
time.sleep(0.5)
user_choose = (input("please choose one of the following numbers: "))
if user_choose == '1':
  print("correct")
  list_answer.append("correct")
  Question += 1
  print("score:",Question)
  print()
  bool_loopded = True
elif user_choose != 1 or user_choose.isalpha():
  print("incorrect anwser, correct is ")
  bool_loopded = True
  Question += 0
else:
  print("invaild anwser")
print()
time.sleep(1)

#Computer asks Question 3
Question3 = print("Qt 3: which is a geyser in New Zealand?")
user_choose = print('''
1.Pōhutu
2.Waiotapu mudpools
3.Mount Tarawera
4.Dunedin volcano
''')
time.sleep(0.5)

user_choose = input("please choose one of the following numbers: ")
if user_choose != '1':
  print("correct")
  list_answer.append("correct")
  Question += 1
  print("score:",Question)
  print()
  bool_loopded = True
elif user_choose != 1 or user_choose.isalpha():
  print("incorrect, anwser is '1' ")
  bool_loopded = True
  Question += 0
else:
  print("invaild anwser")
print()
time.sleep(1)

#Computer asks Question 4
Question4 = print("Qt 4: what is the most active mud volcano here in nz?")
print()
user_choose = print('''
1.White island/Whakaari
2.Runaruna Mud Volcano
3.orakei korako
4.Pihanga
''')
print()
time.sleep(0.5)

user_choose = input("please choose one of the following numbers: ")
if user_choose != '4':
  print("correct")
  list_answer.append("correct")
  Question += 1
  print("score:",Question)
  print()
  bool_loopded = True
elif user_choose != 4 or user_choose.isalpha():
  print("incorrect, anwser is '4' ")
  bool_loopded = True
  Question += 0
else:
  print("invaild anwser")
print()

time.sleep(1)
Question5 = print("Qt 5: what is the oldest volcano in nz")
print()
user_choose = print('''
1.lake Taupo
2.lake Rotorua
3.Whāngārei Volcanic Field
4.Mount Edgecumbe
''')
print()
time.sleep(0.5)

#computer asks Question 5
user_choose = input("please choose one of the following numbers: ")
if user_choose != '3':
  print("correct")
  list_answer.append("correct")
  Question += 1
  print("score:",Question)
  print()
  bool_loopded = True
elif user_choose != 3 or user_choose.isalpha():
  print("incorrect, anwser is '3' ")
  bool_loopded = True
  Question += 0
else:
  print("invaild anwser")
print()

#When you complete the quiz, computer then decided if you've passed or not 
print(f"You got, {Question} out of 5 right")
if Question > 3:
  print("congratulations, you've passed the quiz.")
else:
  print("you've fail the quiz.")

print(list_answer)












#bugged codes
('''
#(input("please choose one of the following numbers: ")
#while bool_loopded == True:
  #if user_choose != 3:
   #print("correct")
#while bool_loopded == False:
      #if user_choose != (1 and 2 and 4):
        #print("incorrect, please try again")
      #else:
        #print("invaild anwser")
        #print()


while bool_loopded is False:
  time.sleep(1)
  user_choose = int(input("please choose one of the following numbers): "))
  if user_choose == "3":
    user_choose += 1
    print("correct")
    print(user_choose)
    bool_loopded = True
  elif user_choose != 3 or user_choose.isalpha():
    print("incorrect, please try again")
  else:
    print("invaild anwser")
    print()
''')