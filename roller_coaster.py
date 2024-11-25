print ("Welcome to the Roller Coaster of the Theme Park!");

height = int(input("what is you height in cm ?"));
if int(height)>120:
 #   print("you shold grow taller to ride the roller coaster!")
# else:
#    print("you can ride onroller coaster.")
    age = int(input("what is your age?"));
    if age <12 :
        bill = 5
    elif  age >12 and int(age) <= 18 :
	    bill = 7
    else:
	    bill = 12
    want_photo = input("Do you want to take a photo? enter Y for yes N for no");
    if want_photo =="Y":
        bill +=3
    elif want_photo =="N":
            bill +=0
# print(f"you total bill is {bill} dollars!")
else:
    print("you should grow taller to ride the roller coaster!")
print(f"thetotal bill is {bill} dollars!")
 



