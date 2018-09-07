from datetime import datetime
currentYear = datetime.now().year
print(currentYear)
Yob = int(input("Enter the year of birth"))
age = currentYear - Yob
def Yob(age):
   if age<18:
    print("The user is a minor.")
   else:
       if age<36:
        print("The user is a youth.")
       else:
        print("The user is an elder.")  

Yob(age)

