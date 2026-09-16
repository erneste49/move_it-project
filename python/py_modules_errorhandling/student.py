
firstname = 'Timothy'
__lastname = 'Henry'        # adding __ (double underscore) makes the variable or function a private member
email = 'timhen@example.com'

def fullname():
    print(f'The students full name is {__lastname} - {firstname}')


def __show_email():
    print(f'Your email is: {email}')


##print(__name__)

if __name__ == '__main__':
    print(firstname)
    fullname()

































