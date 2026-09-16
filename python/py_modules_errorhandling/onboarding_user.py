##usernames = []
##passwords= []
##
##def login():
##    print('login')
##
##def signup():
##    print('signup')
##
##def reset_password():
##    print('reset password')




usernames = []
passwords= []

def login(name, pwd):
    if name in usernames:
        if pwd in passwords: 
            print('Account login successful')
    else:
        print("Account not found")

##def signup(name, pwd):
##    if name not in usernames:
##        usernames.append(name)
##        print(' Account created successfully')
##    if pwd not in passwords:
##        passwords.append(pwd)

def signup(name, pwd):
    if name != '' and pwd != '':
        usernames.append(name)
        passwords.append(pwd)
        print(f'{name}, an account has been created for you')
        

def reset_password(name):
    if name in usernames:
        new = input('Enter your new password: ')
        print('password reset completed')
    else:
        print('Account not found')



if __name__ == '__main__':
    signup('ola', 1234)
    signup('ade', 4444)
    print(usernames)
    print(passwords)



































