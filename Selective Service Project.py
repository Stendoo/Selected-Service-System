print("The Selective Service System is used in case the U.S. needs to have a draft. Do you have to register for the Selective Service System?")

gender=input("Are you male or female?")
 
if gender == "female":
  print("No, you are not required to register for the Selective Service System.")
   
if gender == "male":
  print("It depends on how old you are.")
  age=input("How old are you?")
  
if gender == "male" and  int(age) in range(18, 26):
    print ("You are required to register for the Selective Service System.")
    
if gender == "male" and int(age) <=17:
  print("No, you are not required to register for the Selective Service System.")
  
if gender == "male" and int(age) >=26:
  print("It is too late for you to register for the Selective Service System.")
