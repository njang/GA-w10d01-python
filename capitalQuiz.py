import random
import numpy as np

def quiz():
  print('America is the best country in United States')
  state_capitals={'Washington':'Olympia','Oregon':'Salem','California':'Sacramento','Ohio':'Columbus','Nebraska':'Lincoln','Colorado':'Denver','Michigan':'Lansing','Massachusetts':'Boston','Florida':'Tallahassee','Texas':'Austin','Oklahoma':'Oklahoma City','Hawaii':'Honolulu','Alaska':'Juneau','Utah':'Salt Lake City','New Mexico':'Santa Fe','North Dakota':'Bismarck','South Dakota':'Pierre','West Virginia':'Charleston','Virginia':'Richmond','New Jersey':'Trenton','Minnesota':'Saint Paul','Illinois':'Springfield','Indiana':'Indianapolis','Kentucky':'Frankfort','Tennessee':'Nashville','Georgia':'Atlanta','Alabama':'Montgomery','Mississippi':'Jackson','North Carolina':'Raleigh','South Carolina':'Columbia','Maine':'Augusta','Vermont':'Montpelier','New Hampshire':'Concord','Connecticut':'Hartford','Rhode Island':'Providence','Wyoming':'Cheyenne','Montana':'Helena','Kansas':'Topeka','Iowa':'Des Moines','Pennsylvania':'Harrisburg','Maryland':'Annapolis','Missouri':'Jefferson City','Arizona':'Phoenix','Nevada':'Carson City','New York':'Albany','Wisconsin':'Madison','Delaware':'Dover','Idaho':'Boise','Arkansas':'Little Rock','Louisiana':'Baton Rouge'}
  wrong=[]
  playMore = 'yes'
  while(playMore == 'yes'):
    idx = np.random.permutation(50)
    # states = list(state_capitals.keys())[idx]
    states = list(state_capitals.keys())
    capitals = list(state_capitals.values())
    for x in range(0,2):
    # for x in range(0,len(states)):
      question = str(x+1)+') capital of '+states[x]+' is '
      choices = random.sample(capitals,4)
      correct = random.randint(0,3)
      choices[correct] = capitals[x]
      for y in range(0,4):
        question += '(' + str(y + 1) + ')' + choices[y] + ' '
      question += ':'
      userInput = int(input(question))
      # print('You guessed',userInput,'The correct answer is',correct+1)
      if (userInput == correct+1):
        print('You chose wisely.')
      else:
        wrong.append(states[x])
        print('You chose poorly.')
    print('Your score is ',len(states)-len(wrong),'/',len(states))
    playMore = input('Would you like to play more? (yes/no)')
quiz()