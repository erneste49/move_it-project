
class Member:
    """Every member created from this class will have the following attribute fullname, email and phone"""
    fullname = ""
    email = ""
    phone = ""
    
    #constructor
    def __init__(self, fullname, email, phone):
        #print(f"Welcome {fname} with Email: {email} and Phone No: {phone}")
        self.fullname = fullname
        self.email = email
        self.phone = phone
    
    def register_user(self):
        #this method collect needed value through attribute: self.fullname
        return f"{self.fullname} has been Successfully Registered!."
    
    #this method collect what it need via parameter
    def login_user(self, username, password):
        return f"""
        Your credentials 
        Username: {username} and 
        Password: {password} are confirmed. 
        Login Successful
        """
    
    #this method collect what it needs via attribute
    def get_profile_details(self):
        return f"Fullname: {self.fullname} | Email: {self.email} | Phone: {self.phone}"
    

#how to instantiate object of a class that has constructor attribute
member1 = Member("roi ernest", "roi@gmail.com", "08023454332")

#message = member1.register_user()
#print(message)

print(member1.login_user("roiernesto", "pass1234"))

# member2 =Member("Peace", "peace@gmail.com", "07082476524")
# member3 =Member("Gabe", "gabe@gmail.com", "09088776524") 

#how to get the doc string
#print(Member.__doc__)
        
  
    