# ** Using function in python

##def greet_user():
##    ''' Doc String to tell about the function, This function greets users '''
##    print('Hello user! Welcome to my page How can we assit you today')
##    print('We are at your service send an email or call us today')
##    print(20 + 30)
##
##greet_user()
##print(greet_user.__doc__)



##user = 'Tim'    #Global variable
##
##def greet():
##    user2 = 'Peter'     #local variable
##    print('Hello Good day', user)
##    print('Good day', user2)
##greet()




##access = True
##def check_name(username):
##    global access       #keyword "global" is used to call a global variable in a function and change the value of the global variable
##    if 'admin' in username:
##        access = False
##        print('Account barred')
##
##def profile():
##    if access == True:
##        print('Welcome!')
##    else:
##        print('Access denied')
##
##check_name('administration')
##profile()
    



##def calculate_grade(user,score):
##    if score >= 50:
##        print(user,'you Passed')
##    else:
##        print(user,'you Failed')
##
##calculate_grade('ernest',60)
##calculate_grade('peace', 49)
##calculate_grade('Gabe',90)


'''
def prod_message(gender):
    if gender.upper() == 'MALE':
        print('Phones are available')
    elif gender.upper() == 'FEMALE':
        print('Shoes and Bags are available')
    else:
        print("No product match")

user_sex= input('Enter your gender: ')
prod_message(user_sex)
'''

# receiving number and counting from number to +10
##def addten(n):
##    for i in range(n, n+11):
##        print(i)
##
##addten(20)
    

# getting next age
##def next_age(age=''):
##    if age == '':
##        print('Please enter your age')
##    else:
##        print('You will be', int(age) +1, 'next year')
##
##ag = input('Enter your age: ')
##next_age(ag)


#function that checks score and awards grade
##def check_grade(score):
##    if score >= 70:
##        print('You Scored A')
##    elif score >= 50:
##        print('You Scored B')
##    else :
##        print('You scored F')
##    
##
##num = input("Enter your score: ")
##check_grade(int(num))




##def check_grade(student, score):
##    if score >= 70:
##        print(student, 'You Scored A')
##    elif score >= 50:
##        print(student, 'You Scored B')
##    else :
##        print(student, 'You scored F')
##    
##nam = input('Enter your name: ')
##num = input("Enter your score: ")
##check_grade( nam, int(num))



# using default parameter 
##def check_grade(student='user', score=10):
##    if score >= 70:
##        print(student, 'You Scored A')
##    elif score >= 50:
##        print(student, 'You Scored B')
##    else :
##        print(student, 'You scored F')
##    
####check_grade(score=88, student='Naomi' )
##check_grade('Adewale', 69)




# *** Args -> argument and kwargs -> keyword argument ***

##def calculate_score(score1, score2):
##    total = score1 + score2
##    print('Total score =', total)
##
##calculate_score(50, 80)

#using f string
##def calculate_score(score1, score2):
##    total = score1 + score2
##    print(f'Total score: {total}')      #using f string we add fin front of string and put the variable in {}
##calculate_score(50, 80)


##def calculate_score(score1, score2, score3, score4):
##    total = score1 + score2 + score3 +score4
##    print(f'Total score: {total}')      #using f string we add fin front of string and put the variable in {}
##calculate_score(50, 80, 20, 50)



# *** Packing ***

##def calculate_score(*args):           #packing is done using "*"
##    print(args)
##    total = sum(args)
##    print(f'The total is: {total}')
##   
##calculate_score(50, 80, 20, 50)



# ** unpacking **

##def calculate_score(sc1,sc2,sc3):
##    print(sc1+sc2+sc3)
##scores = [20,30,42]
##calculate_score(*scores)    # unpacking



#using packing and unpacking
##def calculate_score(*sc):       #packing
##    print(sum(sc))
##scores = [20,30,42,8]
##calculate_score(*scores)    # unpacking



##def student_details(fname, lname, no):
##    print(f'Firstname is : {fname}')
##    print(f'Lastname is : {lname}')
##    print(f'Student No : {no}')
##
##student_details(fname='Tim', lname='Jones', no='12345')


# **** using kwargs ****
#packing in kwargs      # packing is done using "**" 

##def student_details(**kwargs):
##    print(f'Firstname is : {kwargs["fname"]}')
##    print(f'Lastname is : {kwargs["lname"]}')
##    print(f'Student No : {kwargs["no"]}')
##
##student_details(fname='Tim', lname='Jonas', no ='12345')


##def student_details(**kwargs):
##    for key, value in kwargs.items():
##        print(f'{key} = {value}')
##        
##student_details(fname='Peace', lname='Okoro', no ='24356')



# *** packing ****
##def student_details(**kwargs):
##    for key, value in kwargs.items():
##        print(f'{key} = {value}')
##        
##student_details(fname='Peace', lname='Okoro', no ='24356', email = 'peaceokoro@example.com')


# *** unpacking kwargs ****
##def student_details(**kwargs):
##    for key, value in kwargs.items():
##        print(f'{key} is {value}')
##detail = {'firstname':'Peace', 'lastname':'Okoro', 'no':'24356', 'email':'peaceokoro@example.com', 'address':'yaba'}   
##student_details(**detail)



# *** using packing and unpacking kwargs ***
##nigeria = {'lagos':'ikeja', 'imo':'owerri', 'niger':'minna'}
##def display_state(**states):
##    for s in states:
##        print(f'{s} -> {states[s]}')
##display_state(**nigeria)




# *** returning a value from function ***
##def guess_luckynum (number):
##    lucky_num = 7
##    if int(number) == lucky_num:
##        print(f'The Lucky number is {number}')
##    else:
##        print('That is not the lucky number')
##
##data = input('Enter your lucky number: ')
##guess_luckynum(data)



def guess_luckynum (number):
    lucky_num = 7
    if int(number) == lucky_num:
        return number
    else:
        return 0

data = input('Enter your lucky number: ')
result = guess_luckynum(int(data)) + 5
print(result)
































