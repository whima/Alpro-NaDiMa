print("""
Welcome to Pizzeria!
order your pizza here
Menu :
(A) Frankfurter BBQ
(B) Meetmonsta
(C) Supersupreme
(D) Supersupreme chicken
(E) Meatlovers
(F) Chickenlovers
(G) Cheeselovers
(H) American favorite
""")

Bill = int(0)

Choose_topping = input("Select Topping (A-H) : ").lower()
if Choose_topping == "a":
    Bill += int(20000)
elif Choose_topping == "b":
    Bill += int(28000)
elif Choose_topping == "c":
    Bill += int(25000)
elif Choose_topping == "d":
    Bill += int(27000)
elif Choose_topping == "e":
    Bill += int(40000)
elif Choose_topping == "f":
    Bill += int(22000)
elif Choose_topping == "g":
    Bill += int(32000)
elif Choose_topping == "h":
    Bill += int(28000)

print("""
Crust variant
(A) Pan crust
(B) Cheesy bite crust
(C) Chilli cheesy stuffed crust
(D) Crown crust carnival
(E) Stuffed crust
""")
choose_crust = input("Select your pizza crust (A-E) : ").lower()
if choose_crust == "a":
    Bill += int(17000)
elif choose_crust == "b":
    Bill += int(12000)
elif choose_crust == "c":
    Bill += int(15000)
elif choose_crust == "d":
    Bill += int(25000)
elif choose_crust == "e":
    Bill += int(21000)

print("""
Size variant
(P) Personal
(M) Medium
(L) Large
""")
choose_size = input("What size do you want? (P/M/L) ").lower()
if choose_size == "p":
    Bill += int(30000)
elif choose_size == "m":
    Bill += int(45000)
elif choose_size == "l":
    Bill += int(60000)
  
extra_chesse = input("Do you want extra cheese for your pizza? (Y/n) ").lower()
if extra_chesse == "y":
    Bill += int(13000)
elif extra_chesse == "n":
    Bill += int(0)

print("""
thanks for your order!
Your bill is Rp""" + str(Bill))