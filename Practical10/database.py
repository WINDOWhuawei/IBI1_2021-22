import re
class Staff():
    def _init_(self):
        print('jjj')
    def database(self,firstname,lastname,location,role):
        print('full name:',firstname,lastname,'  location:',location,'  role:',role)
p=Staff()
p.database('Amy','Johnson','International Campus','leadership')
#the return of example is "full name: Amy Johnson   location: International Campus   role: leadership"
