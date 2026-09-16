"""
    This is the introduction
    to javascript
"""
##a = 'Hello World'
##b = "Hi Everyone good to see you"
##c = '''
##    This is a
##    multi-line
##    string
##'''
##d = """
##    This is also a
##    multi-line
##    string
##"""
##print(a)
##print(b)
##print(c)
##print(d)

##e = 5
##f = 7
##print(e)
##print(f)



# this is a single line/inline comment about code below it is a greeting message
##greet = 'Hello Good morning friends'
##greet2 = 'He said "Hello friends" '
##print(greet)
##print(greet2)
##
##greet3 = ''' He said "Hello friends" '''
##print(greet3)

"""
    This is a
    multi-line
    comment
"""
"""
    This is also a
    multi-line
    comment
"""

# print(__doc__)

##name = input('Please enter your name: ')
##print(name)

##statement1 = "Peace You can do better"
##statement2 = "Don't relent practice more"
##print(statement1, statement2, sep=" - ")  # end=" " --> used to add new print on a new line or same line
##print('Thank you for registering with MOAT')


# concatinating string and variable together using + and , sign
# name = 'John'
##name = input('Enter your name')
##greeting = 'Welcome'
##print(greeting + ' ' + name + ' how are you doing')
##print(greeting, name, 'Hope you are good')

# assigning one value to multiple variable 
##your_name = 'Ernest'
##our_name = 'Ernest'
##my_name = 'Ernest'
##your_name = our_name = my_name = "Ernesto"
##
##print(your_name)
##print(our_name)
##print(my_name)
##
### to check the data type of a variable we use "type"
##print(type(our_name))

# print(help('keywords'))

##last_name = 'Mark'
##print(last_name)
##last_name = 'His name is ' + last_name
##print(last_name)

##student_score = 94
##print(student_score)
##student_score =  student_score + 6
### student_score += 6  # another way to write code in line 89
##print(student_score)

# assigning boolean value which are either True or False
# is_logged_in = True
# print(type(is_logged_in))

# performing calculaitons
##price = 500
##quantity = 5
##total = price * quantity
##print(total)

##num1 = 50
##num2 = 3
##result = num1 % num2
##print(result)
##
##num3 = -6
##print(num3)
##print(abs(num3))  # abs --> used to change a negative number to a positive number
##
### int () --> used to display whole number ignoring the decimal point, see below
##amount = 240.89
##print(amount)
##print(int(amount))
##
### converting string integer to actual integer
##age = '30'
##print(type(int(age)))

##converting integer to floating numb 
##points = 35
##print(points)
##print(float(points))

##num1 = 50
##num2 = 3
##
##div = num1 / num2
##mod = num1%num2
##print(div)
##print(mod)
##result = divmod(num1, num2) # using divmod to perform division and modolus operation together
##print(result)
##
### using raise to power ufnction in 2ways line 138, and 139
##print(5 ** 2)
##print(pow(5,2))

##rewards = 250
##rewards //= 5
##print(rewards)

##statement = 'Have a nice day'
### print(statement *3)  # adding * 4 repeats the variable 4 times
##print(len(statement))
##
##balance = 10000
##print(type(balance))  # type () --> used to check data type
### to convert an integer to a string we use-> str()
##print(type(str(balance)))
##
### we can't concantinate string and integer together hence it needs to be converted before concantination or use the , to concantinate
##print('This is your balance: ' + str(balance))
##print('Your balance is:', balance)
'''
name = input('Enter your name: ')
phone = input('Enter your Phone Number: ')
print('Thank you', name, ', your phone number is', phone)


math_score = input('Enter your score in math: ')
english_score = input('Enter your score in english: ')
biology_score = input('Enter your score in biology: ')
result = int(math_score) + int(english_score) + int(biology_score) 
average_score = result // 3

print('Your Average score is: ', average_score)
'''

# using index location to retreive string value
# sentence = 'I love python programming language'
# print(len(sentence))
# print(sentence[32])  # using positive index
# print(sentence[-1]) # using negative index

# to slice a string selecting the character using index location
##print(sentence[0:6])
##print(sentence[2:])
##print(sentence[:-9])
# using negative index to slice
##print(sentence[-20:-9])

# using step (skip) when slicing a string
##sentc = 'python'
##print(sentc[0:6:2]) 

##your_email = input('Enter your email: ')
##print('You are using a', your_email[-9:-4], 'mailbox')

# quote = input('Enter your quote for the day: ')
# print(quote.upper()) # converting string from lowercase to uppercase
# print(quote.lower()) # converting string from uppercase to lowercase
# print(quote.capitalize()) # to capitalize the first letter of the string

# print(quote.isupper()) # function to check if the string characters are in uppercase
# print(quote.split()) # to slice each word in a sentence individually

# below line 200 "dir" shows all the string method available
# print(dir(quote))

# using "in" and "not in" to check is a string/word is in another string/word
##username = 'administrator'
##result = 'admin' in username  # using "in" checks for the word admin in administator and returns True if found else it returns False
##result = 'guest' not in username # using "not in" checks if the word guest is not in administrator and returns True if not found in the word
##print(result)

##statement = 'I love javascript'
##print(statement.replace('javascript', 'python programming language'))

##data = 'peaceokoro123'
##print(data.isdigit()) # "isdigit()" is used to check if a string contains only degit and returns True, if it contains both alphabet False

# simple if statement
##age = input('Enter your age: ')
##if int(age) > 18:
##    print('You are an adult')
##    print('Thank you')
##print('This code is outside the if statement')

# if else Statements in python
##age = input('Enter your age: ')
##if int(age) > 18:
##    print('You are an adult')
##    print('You can enter')
##else:
##    print('You are a minor')
##    print('You still need to grow')

# Keyword "pass" is used in if else statement where there is not code/condition in an if statement

# if elif elif... else statement
##grade = input('Enter your grade: ')
##if grade.lower() == 'a':
##    print('Excellent')
##elif grade.lower() == 'b':
##    print('Very Good')
##elif grade.lower() == 'c':
##    print('Good')
##elif grade.lower() == 'd':
##    print('Pass')
##else:
##    print('Failed')


# using if statement inside an if statement
#math_score = int(input('Enter your math score: '))
#english_score = int(input('Enter your english score: '))

##if math_score > 50:
##    if english_score > 50:
##        print('Welldone, you did well.')
##    else:
##        print('You did not get a good score')
##else:
##    print('You can do better')


##if math_score > 50:
##    print('Welldone, you did well.')
##else:
##    print('You can do better')
##if english_score > 50:
##    print('Welldone, you did well.')
##else:
##    print('You can do better')

# using logical operator "and" checks both condition and must be true for condition to occur
##if math_score > 50 and english_score > 50:
##    print('Welldone, you did well.')
##else:
##    print('You can do better.')

# using logical operator "or"
##if math_score > 50 or english_score > 50:
##    print('Welldone, you did well.')
##else:
##    print('You can do better.')
##    


##data = 'nothing'
##print(data == 'nothing')

##data = "user"
##print(len(data) == 4)


##username = input('enter your username: ')
##password = input('Enter your password: ')
##
##
##if len(username) > 5 and len(password) > 0:
##    print('Account Created Successfully')
##else:
##    print('Account creation failed')



# login confirmation
##email = input('Enter your email')
##passwod = input('Enter your account password: ')
##if str(passwod) == 'pass123' and len(email) > 0:
##    print('Welcome to your Account')
##else:
##    print('Wrong email or password')



#tenary operator (line:318) --> can only be used for if else statement
score = 50
##if score > 50:
##    print('Passed')
##else:
##    print('Failed')

# using tenary operator to write above line of code
# print('Passed') if score > 50 else print('Failed')


#your_slogan = input('Enter your slogan: ')
##if your_slogan == '':
##    print('Your slogan is empty')
##else:
##    print(your_slogan.upper())

#print('Your slogan is empty') if your_slogan == '' else print(your_slogan.upper())




## PYTHON COLLECTION --> include (1.) list, (2.) Tupple, (3.) Set, (4.) Dictionary

##LIST
##numbers = [1,2,3,4,5]
##print(numbers[1])
##print(numbers[-2])

##num1 = [1,2,3]
##num2 = [4,5,6]
##result = num1 + num2
##print(result)
##print(num2 * 3)

##performing slicing on list
###result = items[0:5]
##result = items[-5:-1]
##result = items[::2]
#print('smith' in items) 


#cars =['honda', 'benz', 'toyota', 'kia', 'benz']
#print(cars)
##cars.append('bmw')
##cars.append('acura')      # .append() is used to add an item to a list
##print(cars)
##cars.clear()          # .clear() is used to clear the list
##print(cars)
##cars2 = cars.copy()       # .copy() is used to copy values of an existing list
##print(cars2)
##print(cars.count('benz'))         # we use .count() to count how many times an item show in a list 
##cars.extend(['jeep', 'hyundia'])    #we use .extend([]) --> used to add multiple items to the list
##print(cars.index('toyota'))     # .index() used to get index location
##cars.insert(0, 'Jeep')       # .insert() takes 2arguement and insert new item at the front
##cars.pop(2)      # .pop() is used to remove item from a list using the index location
##cars.remove('toyota')       # .remove()  used to remove by item by using item name
##cars.reverse()      # .reverse()  is used to reverse the order of a list
##cars.sort()         #.sort() is used to arrange the items in a list alphabetically
#print(cars)



##nums = [1,2,3]
####nums2 = nums.copy()     # .copy() is copying values and saving in a different memory location
##nums2 = nums        # using referencing
##nums[-1] = 4
##nums[1] = 5
##print(nums)
##print(nums2)


##usernames = ['demo', 'test', 'sample']
##username = input('Choose your username: ')
##if username in usernames:
##    print('Username not allowed')
##else:
##    print('Proceed')
###using tenary below
##print('Username is not allowed') if username in usernames else print('Proceed')


##items = ['pen', 'book', 'ruler']
##old_items = ['milk', 'crayon', 'biro', 'pencilcase']
##
##new_items = items + old_items[1:]
##print(new_items)



# collecting numbrs from users and displaying how many correct number they got
'''
raffle_num = [2,9,8]
correct = []
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if num1 in raffle_num and num1 not in correct:
    correct.append(num1)
if num2 in raffle_num and num2 not in correct:
    correct.append(num2)

print('You got', len(correct), 'correctly')
'''


## LOOP IN PYTHON

##grade = [12,10,8,11,7,47]
##for x in grade :
##    print('hello')


# using range to loop 
##print(list(range(1, 11,2)))
##print(list(range(10,0,-1)))


##for peace in range(10):
##    print(peace)
##
##
##for x in range(5):
##    print(x)

#for y in range(13):
#    print(y, 5**y)


for n in range(11):
    if n == 5:
        continue
    print(n)
##    if n == 6:
##        break
##    print(n)
















































