ticket = int(200)
amount = int(input("Enter Amount"))
balance =int(amount - ticket)
print(("Balance:") + str(balance))
age=int(input("Enter Age"))
if age>18:
    print("Over 18. Welcome to Club House.")
    print(("Balance:") +  str(balance))
else:
        print("18 or under.NOT ALLOWED")
        print(("Balance:")  + str(amount))
