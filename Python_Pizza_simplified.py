print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
if size!="S" and size!="M" and size!="L":
    print("Error!, please insert a valid input")
    
add_pepperoni = input("Do you want pepperoni? Y or N ")
if add_pepperoni!="Y" and add_pepperoni!="N":
    print("Error!, please insert a valid input")

extra_cheese = input("Do you want extra cheese? Y or N ")
if extra_cheese!="Y" and extra_cheese!="N":
    print("Error!, please insert a valid input")

#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1

bill=0

if size=="S":
    bill+=15
elif size=="M":
    bill+=20
else:
    bill+=25

if add_pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3

if extra_cheese=="Y":
    bill+=1

print(f"Your final bill is: ${bill}.")