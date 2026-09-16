
class Customer:
    
    def __init__(self, acctname, pwd):
        self.acctname = acctname
        self.pwd = pwd
        
    def create_acct(self):
        print(f"An account has been created for {self.acctname}")
        
    def pay_installment(self,acctno):
        print(f"Installment has been paid for {acctno}")
        
        
class Premium(Customer):
    
    def request_statement(self):
        print(f"Here is your statement for review")
        
p = Premium("ernest",  "pass678")
#p.create_acct()    
p.pay_installment("Cus2345")
#p.request_statement()
p.accntno = 'PRE2344'
p.pay_installment("CUS2466")
