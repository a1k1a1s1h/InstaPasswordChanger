import pickle
from instagram import Instagram



#####################################
#####################################
#####################################
#enter your new password here and run the program
updatepass = "upinTheClouds"

#####################################
#####################################
#####################################








usrname = '_akash__06_' #constant 
pwd = None 
currpwd = pickle.load(open("PasswordFile.p","rb"))


myID = Instagram(usrname,currpwd)
#myID.logIn()
#myID.changePassword(updatepass)
print(myID.Password())
myID.close()


