'''https://replit.com/join/njbivcrzxq-a00573910'''

dis=float(input("Enter the number of miles per day: "))
MPG=float(input("Enter the car's miles per gallon: "))
p=float(input("Enter current price of gasoline per gallon: "))
d=int(input("Enter the number of days of the trip: "))

ans=0

for i in range(0, d):
  ans+=p*(dis/MPG)

print("The total price of the trip will be: $"+str(ans))
