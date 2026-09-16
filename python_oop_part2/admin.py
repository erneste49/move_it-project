from regime import Member

class President(Member):
    
    def __init__(self, party_name, p_name):
        super().__init__(party_name)        #the --> super() <-- is used to access property in the parent class
        self.name = p_name
    
    def approve_nomination(self, n):
        if n in self._nominees:
            print(f"{n}'s nomination has been approved by {self.name}")
        else:
            print(f"{n} was never nominated")
            
    def sack_minister(self, n):
        if n in self._nominees:
            self._nominees.remove(n)
            print(f"{n} has been sacked by {self.name}")
        else:
            print(f"{n} was not approved as a minister")
            
            
     #destructor method:--> also runs authomatically and last and can be used to close db connections       
    def __del__(self):
        print("This object has been destroyed")

pr = President("APC", "BAT")
pr.agenda()
pr.nominate('bayo')
pr.nominate('wike')
pr.nominate("Gabe")
print(pr._nominees)
pr.approve_nomination('wike')
pr.approve_nomination('peter')
pr.sack_minister('bayo')
pr.sack_minister('rufai')
print(pr._nominees)
