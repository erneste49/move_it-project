'''This page contains process of importing a module in another module and using the lines of code in the module '''
#using import --> brings everything from the import module
##import student
##
##print(student.firstname)
##student.fullname()

#using from modulename import what_to_import     --> imports only a particular variable or function
##from student import (firstname, email, fullname)
##print(firstname)
##print(email)
##fullname()

#using wildcard import  --> imports everything from the module except the private members
##from student import *
##print(firstname)
##fullname()
##print(__lastname)   #gave an error because __lastname is a private member


## *** Alias keyword  "as"  *** --> used to rename
##import student as st
##st.fullname()

##from student import fullname as fn, firstname as fname
##fn()
##print(fname)

##import student          # to see all functions and variable in an imported module use "dir()"
##print(dir(student))


##print(student.__name__)
##print(__name__)


## **** using python built in modules ****
## os module
import os
##print(os.getlogin())
##file = r'C:\Users\HomePC\Desktop\moat\python\py_modules_errorhandling\student.py'
##result = os.stat(file)
##print(result.st_size)


#to get list of files in a directory
##my_folder = r'C:\Users\HomePC\Desktop\moat\python\py_modules_errorhandling'
##print(os.listdir(my_folder))
##for item in os.listdir(my_folder):
##    print(item)


#to get the current working directory 
##print(os.getcwd())

#to check if a directory leads to file or a folder
file = r'C:\Users\HomePC\Desktop\moat\python\py_modules_errorhandling\student.py'
my_folder = r'C:\Users\HomePC\Desktop\moat\python\py_modules_errorhandling'

#print(os.path.isfile(file))
#print(os.path.isfile(my_folder))


#how to create a folder --> ** os.mkdir('') **
#os.mkdir('images')
#print('Folder created successfully')

#how to rename a folder
##oldname = r'C:\Users\HomePC\Desktop\moat\python\py_modules_errorhandling\images'
##newname = r'C:\Users\HomePC\Desktop\moat\python\py_modules_errorhandling\pics'
##os.rename(oldname, newname)
##print('Folder successfully renamed')



## **sys works with command promt/terminal and evaluates values and display result based on py code in cmd
##import sys

##print(sys.argv)
##print(f'{sys.argv[1]} your total score is {int(sys.argv[2]) + int(sys.argv[3])}')


## **using math 
##import math

##balance = 10.78
#print(math.ceil(balance))       #math.ceil() rounds up balance to the nearest highest number
#print(math.floor(balance))      #math.floor() rounds up number to the nearest lowest number


## *** Error handling ***   **error that crash program are exception errors or runtime error**















