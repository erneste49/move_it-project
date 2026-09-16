##for x in range(1,6):
##    print(x)
##
##for y in range(5,0,-1):
##    print(y)

# ** printing the names except my name **

##names = ['Gabe', 'Ernest', 'Peace']
##for name in names:
##    if name == 'Ernest':
##        continue
##    print(name)


# **using else in for Loop **

##for x in range(10):
##    if x == 8:
##        break
##    print(x)
##else:
##    print('Loop completed Successfully')
# ** The else part in the for loop will only be executed if the condition above is met **


# ** WHILE LOOP IN PYTHON **

##x = 1
##while x <= 10:
##    print(x)
##    x += 1


##names = ['Gabe', 'Peace', 'Ernest']
##c = 0
##while c <= 2:
##    if names[c] == 'Peace':
##        break
##    print(names[c])
##    c = c+1
##else:
##    print('While loop completed successfully')
# **Using the else statement will only execute if the condition in the while loop is completed if not the else part will not run **



# **Writing a program that accepts number and loops untill q is entered and it displays the total of numbers entered **
##
##number = input('Enter a number, press "q" to quit: ')
##total = 0
##while number.upper() != 'Q':
##    total = total + int(number)
##    number = input('Enter a number, press "q" to quit: ')
##
##print('The total of numbers entered is: ', total)



# ** TUPLE **

#empty_tup = tuple()        # to creat an empty tuple
# tuple are created using "()" and must contain a comma "," when creating single or multiple item. items in a tuple cannot be updated or added
##numbers = (20, 67, 90, 45)
##print(numbers)
##print(numbers[2])


# changing the first character of a string
##last_name = 'franklin'
### convert a string to tuple, --> we use tupple() dunction
##print(last_name)
####print(tuple(last_name))
##lname_tuple = tuple(last_name)
##print(lname_tuple)
##new_name = ('F', ) + lname_tuple[1:]
##print(new_name)


# looping tuple
##numbers = (5,7,15,10)
##for n in numbers:
##    print(n)


##name = 'Ernest'
##name_tuple = tuple(name)
##print(name_tuple)
##name_list = list(name) # converting a string to list using function-->  "list()"
##print(name_list)


# Tuple assignmnt
##(math,eng,bio) = (30,40,50)
##print(math)
##print(eng)
##print(bio)


##email = 'peace12okoro@gmail.com'
##username, domain = email.split('@')
##print(domain)

##text = [('a', 0),('b', 1),('c', 2)]
##for letter, number in text:
##    print(letter,number)



##students = [('Alejandro', ['CompSci', 'Physics']),
##        ('justin', ['Math', 'CompSci', 'Stats']),
##        ('Ed', ['CompSci', 'Accounting', 'Economics']),
##        ('Margot', ['InfSys', 'Accounting', 'Economics', 'CompmLaw']),
##        ('Peter', ['Sociology', 'Economics', 'Law','Stats','Music'])]
##
##for stud_name,stud_subject in students:
##    print(stud_name, 'takes', len(stud_subject), 'Subjects')
##    



# Assigning students and score from two list

##scores = [20,21,19]
##students = ['Tom', 'Matt', 'Judy']
##
##for x in range (3):
##    print(students[x], 'scored', scores[x])
##
##for student,score in zip(students,scores):
##    print(student, 'scored', score)






# *** DICTIONARY ***   --> Functions in dictionary: 1. .key()   2. .values()    3. .items()     4. .get()       5. .po()

#scores = {'math':10, 'eng':20, 'bio':30, 'name':'Emeka'}
### to access a value from a dictionary
##print(scores['name'])
### to update a value of an object in dictionary
##scores['name'] = 'Peter'
##print(scores['name'])
### to add a new object toa dictionary
#scores['name2'] = 'Grace'
##print(scores)

# ** how to loop in dictionary **

##for sc in scores:
##    print(sc, scores[sc])

##print(scores.keys())
##print(scores.values())
##print(scores.items())

##for k in scores.keys():
##    print(k)
##for v in scores.values():
##    print(v)
##for i in scores.items():
##    print(i)


# creatinf dictionary to display only the values
##about_me = {'lastname':'Eze', 'firstname': 'Ernest',  'middlename':'roi', 'email':'roiernest@gmail.com' }
##
##for me in about_me.values():
##    print(me)
##print(about_me.values())

# using .pop()
#scores = {'math':10, 'eng':20, 'bio':30, 'name':'Emeka'}
#print(scores)
##scores.pop('name')
##print(scores)

# using .get()
##print(scores.get('name'))
##print(scores.get('email', 'Key not fount in dictionary'))
##print('The programme continues here')



##empty_dict = dict()      # dict() function can be used to create an empty dictionary
### empt_dict = {}
##empty_dict['key1'] = 'value1'
##print(empty_dict)



##students = [ ('tolani',4139),('John', 4127),('Wendy',4098) ]
##
##dictionary_list = dict(students)
####print(dictionary_list)
##
##print(dir(dictionary_list))



# *** SET ***

# fruits = {'orange', 'mango', 'apple', 'banana'}

# print(type(fruits))
# print(fruits)
# print('mango' in fruits)
##for i in fruits:
##    print(i)

#creating a empty set
##empty = set()
##print(type(empty))

# ** set functions**

##fruits = {'orange', 'mango', 'apple', 'banana'}
##print(fruits)
####fruits.add('grapes')
####fruits.clear()
##
##print(fruits)


python_guys = {'html', 'css', 'js', 'python', 'flask'}
php_guys = {'html', 'css' ,'js', 'php','laravel' }

#using difference() method
#result = python_guys.difference(php_guys)
#result = php_guys.difference(python_guys)

# using difference_update    --> updates the result in same variable
##php_guys.difference_update(python_guys)
##print(php_guys)

# using intersection() method --> returns common value in 2 collections
##result = python_guys.intersection(php_guys)
##print(result)

# using intersection update --> no need to assign result to variable as it will update existing variable
##python_guys.intersection_update(php_guys)
##print(python_guys)

# using remove
##python_guys.remove('css')
##print(python_guys)

#using discard
#python_guys.discard('html')
#print(python_guys)


##names = set()
##names.add('Gabe')
##names.add('Peace')
##names.add('Ernest')
##print(names)
##
##cars = set(('Toyota', 'Benz', 'Kia'))
##print(cars)

# using .pop()      --> using pop removes a randon item
##popped = python_guys.pop()
##print(popped)

# using symmetric_difference
##result = python_guys.symmetric_difference(php_guys)
##print(result)

# using symmetric_difference_update
python_guys.symmetric_difference_update(php_guys)
print(python_guys)









































