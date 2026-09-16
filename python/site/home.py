#method:1 -- *** using Absolute import ***
#first method of importing module from a package ** using import syntax**
##import reports.payment
##
##reports.payment.pay_func()


# method:2 -- using from import
##from reports import payment
##payment.pay_func()
#or
##from reports.payment import pay_func
##pay_func()
##from reports.payment import pay_func as payfn
##payfn()


#import reports.payment

#printing variable saved in __init__.py in reports
##import reports
##print(reports.commission)
##from reports import commission as com
##print(com)


##import reports.payment
##reports.payment.pay_func ()

#method 3:  -- importing the modules in __init__.py and calling reports to access the modules
##import reports
##reports.payment.pay_func()
##reports.registration.register_func()


#using wildcard imports -- 
##from reports import *
##payment.pay_func()
##registration.register_func()


#using import 
##import admin.user_auth
##admin.user_auth.login()

#using from import
##from admin.user_auth import login
##login()

#using import method 
##import reports.private_report.donation
##reports.private_report.donation.total_donation()

#using from import
##from reports.private_report.donation import total_donation
##total_donation()


##from reports.private_report import donation
##donation.total_donation()


# *** USING ABSOLUTE IMPORT *** --> using the full file path name to locate a module. it starts from the root package/folder
##import admin.manage_user
##admin.manage_user.user_management()
#or
##from admin import manage_user
##manage_user.user_management()




# **** USING RELATIVE IMPORT **** uses from import only

from reports.private_report import donation
donation.total_donation()

























