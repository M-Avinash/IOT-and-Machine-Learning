import random

count = 1 #Inital count which will be used to identify getting it right 
          #in the first guess
number = random.randint(1, 20)
#print('DEBUG: The random number is ' + str(number))
print('Guess a number between 1 and 20')
userinput = int(input())

def guess(userinput):
   
   if int(userinput) > int(number):
       print('too high, try again')
       exit  
   if int(userinput) < int(number):
       print('too low, try again')
       exit
   if userinput == int(number):
       print('thats right !!!')
       global count
       if int(count) ==1: #Using Initial count to identify single attempt guess
           print('wow you got it in a single attempt')
       else:
           print('you took ' + str(count) + ' attempts')
           exit
       
guess(userinput)
count = 2 #Increasing count to 2 since from now on minimum 2 attempts will be taken

while userinput != int(number):
    userinput = int(input())
    guess(userinput)
    count = count + 1 #Increment count at every attempt, here count starts from 2