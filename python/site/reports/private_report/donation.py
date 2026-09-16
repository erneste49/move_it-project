#using absolute import
##import reports.payment

##def total_donation():
##    print('This is the total donation received')
##    #reports.payment.pay_func()



# *** USING RELATIVE IMPORT ***

from .. import payment
##from ... import home  
##import home

def total_donation():
    print('This is the total donation received')
    payment.pay_func()





