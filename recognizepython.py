num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #data type boolean
string = 'Hello World'# data type string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']#list with strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}# list with numbers,strings, and boolean
fruit = ('blueberry', 'strawberry', 'banana')# variable that contains a list of strings
print(type(fruit))#output: class "dict"
print(pizza_toppings[1])#output sausage
pizza_toppings.append('Mushrooms')# this would add mushrooms to the pizza toppings list at the end
print(person['name'])#output john
person['name'] = 'George'# this would replace the name john with george
person['eye_color'] = 'blue'#this would add eye color:blue to the person list
print(fruit[2])# output banana

if num1 > 45:# conditional if statement
    print("It's greater")#output if the number is greater than 45 it's greater
else:# conditional else statement
    print("It's lower")# output if the number is less than 45 it's lower

if len(string) < 5:    
""" this is a if else statement that gives an output on word length depending
on how many letters the word has and the output would be one of three
phrases based on this"""


    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):"""
all of theese next lines will output out a range of numbers defined 
by the range given in the parenthesis"""
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0 # a while loop that will output x 0,1,2,3,4
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()#this will delete the last item in the pizza toppings list
pizza_toppings.pop(1)#this will delete the item in the pizza toppings list at the 1 spot

print(person)#output name: john location:salt lake city age:37 is balding:false eye color: blue
person.pop('eye_color')# wil remove eye color from the person list
print(person)#output all items except the eye color

for topping in pizza_toppings:# this will print pizza topping until olives and then stop
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():#output will print hello 10 times
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):#output will print hello 4 times
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):#will print hello 10 times and 4 times
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)