#import this 

## ***Using decorator without parameter*** 

# import favourite_quote
# favourite_quote.my_quote()

def hello_decorator(fn):
    def wrapper():
        print("Hello everyone!.")
        fn()
        print("commands executed...")
    return wrapper

    
# w = hello_decorator(hello)
# w()
   
@hello_decorator
def hello():
    print("Welcome back to class!.")          
#hello()
#############################################

p_location = ["Ghana", "USA", "Niger"]
def secure_location(location1, location2, location3):
    def check_location(fn):
        def wwrapper():
            if location1 and location2 and location3 in p_location:
                print(f"{location1} \nAccess Granted")
            else:
                print(f"{location1} \nAccess Denied")
            
        return wwrapper
    return check_location
        

###########################################################

def check_user(fn):
    def wrapper():
        user = input("Enter your username: ")
        pwd = input("Enter your password: ")
        if user == "admin" and pwd == "1234":
            print("Welcome user, your result is 234")
            fn()
        else:
            print("Invalid login")
    return wrapper   

@check_user
def print_result():  
    print("Result printed successfully")

@check_user
def change_password():
    print("Password changed")
   
# print_result()
#change_password()

################################################
    
    
def decorate_hello(fn):
    def wrapper(s,n):
        print(f"{s} is the standard way of greting specified by {n}")
        fn(s,n)
    return wrapper

@decorate_hello
def hello (salute, name):
    print(name, "said", salute)
    
def say_hello():
    name = input("Enter your name: ")
    salute = input("Enter your salutation: ")
    hello(salute, name)

# greet = decorate_hello(hello)
# greet("Salut!", "Peace")
#hello("Bonjour!","Gabe")

#say_hello()



##########################################################
##  **** Using Decorator with  parameter


def check_election_result(fn):
    def wrapper():
        #print("Are you an Admin or Voter")
        user = input("Are you a Voter or Admin: ")
        if user.upper() == "ADMIN":
            print("Welcome Admin")
            fn()
        else:
            print("Welcome voter, elections has ended")
    return wrapper


@check_election_result    
def election_result():
    print("The winner of the Election is Peter Obi")
    
#election_result()

########### or 
users = ["peter_admin", 'john_admin', "mary_admin"]
passwords = ["admin123", "admin12", "admin1", "admin"]
def check_permission(fn):
    def wrapper():
        user = input("Enter the user: ")
        pwd = input("Enter password: ")
        if user in users and pwd in passwords:
            print("Valid login")
            fn()
        else:
            print("Invalid Login")
    return wrapper

@check_permission
def check_result():
    print("Here is the Election result!")  
#check_result()
######### using parameter for above code ###########

users = ["peter_admin", 'john_admin', "mary_admin", "roi"]
passwords = ["admin123", "admin12", "admin1", "admin"]

def check_permission(fn):
    def wrapper(user,pwd):
        if user in users and pwd in passwords:
            print("Valid login")
            fn()
        else:
            print("Invalid Login")
    return wrapper

@check_permission
def check_result():
    print("Here is the Election result!")  
    
#check_result("peter_admin", "admin123")
# print("-----------------------------------")
# check_result("roi", "admin")

############# using a decorator inside an outer decorator ############

pages = ["admin.html", "home.html", "result.html"]
users = ["peter_admin", 'john_admin', "mary_admin", "roi"]
passwords = ["admin123", "admin12", "admin1", "admin"]

def global_security(current_page, user, pwd, symbol):
    def check_permission(fn):
        def wrapper():
            if current_page in pages:
                if user in users and pwd in passwords:
                    print(symbol * 40)
                    print("Valid login")
                    fn()
                    print(symbol * 40)
                else:
                    print(symbol * 40)
                    print(f"Invalid Login details, \n you entered {user}, {pwd} ")
            else:
                print(symbol * 40)
                print(f"invalid page \n You are on {current_page}")
        return wrapper
    return check_permission

old_user = "john_admin"
new_user = "mary_admin"

@secure_location("Ghana", "USA", "Niger")
@global_security("result.html", old_user, "admin123", "-")
def check_result():
    print("Here is the Election result!")  
    
@global_security("home.html", "mary_admin", "admin12", "-")
def make_new_admin():
    print("New Admin has been created")

@global_security("result.html", "peter_admin", "admin123", "-")
def add_user():
    #new_user = "Tom"
    print(f"User Added \n{new_user} has been added")
    
@global_security("result.html", "john_admin", "admin123", "-")
def delete_user():
    #old_user = "Mark"
    print(f"User Deleted \n{old_user} has been deleted")
    

# check_result()
# make_new_admin()
# delete_user()
# add_user()

#check_result()

#################################
users = ["peter_admin", 'john_admin', "mary_admin"]
passwords = ["admin123", "admin12", "admin1", "admin"]

def check_login(user, pwd):
    def check_permission(fn):
        def wrapper():
             if user in users and pwd in passwords:
                print("Valid login")
                fn()
             else:
                print("Invalid Login")
        return wrapper
    return check_permission


# @check_login("peter_admin", "admin123")
# @check_permission("peter_admin")
# def delete_user(name):
#     print(f"User {name}, deleted")
    
#delete_user()
########################################################
## ******* DECORATOR IN OOP ************
class Staff:
    staff = "peter"
    
    def __name__(self, name):
        self.name = name
        
    @classmethod
    def hello(cls):
        print("Happy new month", cls.staff )
        
#Staff.hello()