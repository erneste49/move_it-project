''' onboarding page that registers new user, login users and reset users password '''

usernames = []
passwords= []

def login(name, pwd):
    if name in usernames:
        index_position = usernames.index(name)
        if pwd == passwords[index_position]:
            print('Account login successful')          
        else:
            print("wrong password entered")
    else:
        print('invalid username or password')


def signup(name, pwd):
    if name != '' and pwd != '':
        usernames.append(name)
        passwords.append(pwd)
        print(f'{name}, an account has been created for you')
        

def reset_password(name, oldpwd, newpwd):
    if name in usernames:
        index_location = usernames.index(name)
        if oldpwd == passwords[index_location]:
            passwords[index_location] = newpwd
            print('password reset completed')
    else:
        print('Account not found')



if __name__ == '__main__':
    signup('ola', 1234)
    signup('ade', 4444)
    print(usernames)
    print(passwords)

    login('ola', 1234)
    login('ade', 4444)

    reset_password('ola', 1234, 9876)
    reset_password('ade', 4444, 5432)

    print(usernames)
    print(passwords)

  






























