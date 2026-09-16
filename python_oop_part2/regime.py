
class Member:
    _nominees = []
    
    def __init__(self, party_name):
        self.party = party_name
        print(f"The name of this party is {self.party}")
    
    def agenda(self):
        print("Read about our agenda")
        
    def nominate(self, n):
        if n not in self._nominees:
            self._nominees.append(n)
            print(f"{n}, has been nominated")
        else:
            print(f"{n}, already nominated")
            
    def __impeach(self):
        print("The president has been impeached")    

