import random
''' 
#Formating
name = "Danciu"
surname = "Andrei"

print("Hello, my name is {0:10} and {1}. Nice to meet you".format(name, surname))
number_1 = 3.14159
number_2 = 1000

print ("The number pi is {:.2f}".format(number_1))
print ("The number pi is {:,}".format(number_2))
print ("The number pi is {:b}".format(number_2))
print ("The number pi is {:o}".format(number_2))
print ("The number pi is {:X}".format(number_2))
print ("The number pi is {:e}".format(number_2))
'''
'''
#RNG
x = random.randint(1,6)
print (x)
y = random.random()
print (y)
myList = ['rock','paper','scissors']
z = random.choice(myList)
print (z)
cards = [1,2,3,4,5,6,7,8,8,9,"J","Q","K",'A']
random.shuffle(cards)
print (cards)
'''

#Exception Handling
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print("You can't divide by 0")
except ValueError as e:
    print(e)
    print("You cannot divide by something that is not a number")
except Exception as e:
    print(e)
    print ("something went wrong")
else: 
    print(result)
finally: print("This will always execute regardless of exception")
