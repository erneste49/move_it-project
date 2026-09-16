''' Learning about how to fix exception error aka run time error '''
## *** Error handling ***   **error that crash program are exception errors or runtime error**

##items = {'name':'John'}
##
##print(items.get('name'))
##print(items.get('score'))


##numerator = 10
##denominator = 0
##if denominator > 0:
##    result = numerator / denominator
##    print('The result is:',result)
##else:
##    print('You cannot devide by zero')


#using if statement to fix error
##weight= int(input('Enter your weight: '))
##height = int(input('Enter your height: '))
##
##if height > 0:
##    bmi = weight/height**2
##    print(bmi)
##print('The programme continues here')


## **** using "try:" aand "except:" to handle exception error in python ****

##try:
##    #import Os
##    
##    weight= int(input('Enter your weight: '))
##    height = int(input('Enter your height: '))
##    
##    bmi = weight/height**2
##    print(bmi)
##
##    item = [1,2]
##    item[3]
##except (ZeroDivisionError, IndexError, ModuleNotFoundError):
##    print('Something went wrong')



##try:
##    weight= int(input('Enter your weight: '))
##    height = int(input('Enter your height: '))
##    bmi = weight/height**2
##    print(bmi)
##
##    item = [1,2]
##    item[1]
##    import Os
##    
##except ZeroDivisionError:
##    print('You cannot divide by zero')
##except (IndexError):
##    print('The index location does not exit')
##except Exception:
##    print('An error occured')


#using ** try: except: else: finally: **
##try:
##    weight= int(input('Enter your weight: '))
##    height = int(input('Enter your height: '))
##    bmi = weight/height**2
##    print(bmi)
##
##    item = [1,2]
##    item[1]
##    #import Os
##    
##except ZeroDivisionError:
##    print('You cannot divide by zero')
##except (IndexError):
##    print('The index location does not exit')
##except Exception:
##    print('An error occured')
##else:
##    print('No exception occured')
##finally:
##    print('This code will always execute')
##
##print('The programme continues here')



# ** raising an exception **
'''
try:
    weight= int(input('Enter your weight: '))
    height = int(input('Enter your height: '))

    if height < 0:
        raise TypeError
    
    bmi = weight/height**2
    print(bmi)

    item = [1,2]
    item[1]
    #import Os
except TypeError:
    print('Height cannot be negative value')
except ZeroDivisionError:
    print('You cannot divide by zero')
except (IndexError):
    print('The index location does not exit')
except Exception:
    print('An error occured')
else:
    print('No exception occured')
finally:
    print('This code will always execute')

print('The programme continues here')
'''



prohibited = ['shit', 'kill', 'fight']
##try:
##    word = input('Enter a word: ')
##    if word in prohibited:
##        raise ValueError
##    print('You typed', word)
##except ValueError:
##    print('That word is prohibited')
##except Exception:
##    print('Something went wrong')
##else:
##    print('No error occured')



# *** using if: except: inside a fuction *** 
def word_checker():
    try:
        word = input('Enter a word: ')
        if word in prohibited:
            raise ValueError
        print('You typed', word)
    except ValueError:
        print('That word is prohibited')
    except Exception:
        print('Something went wrong')
    else:
        print('No error occured')
    

#word_checker()




















