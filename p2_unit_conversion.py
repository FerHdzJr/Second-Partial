'''https://replit.com/join/fwiwmyibjd-a00573910'''

print("---Unit converter---\n")

print("Enter the number of your convertion:")
print("1. kilometers to miles")
print("2. liters to gallons")
print("3. celcius to fahrenheit")
print("4. years to lustrum")
print("5. hours to minutes")

m=int(input())
n=int(input("Enter the amount you want to convert:\n"))
if(m==1):
  print(n, " kilometers are ", n*0.62, " miles")
elif m==2:
  print(n, " liters are ", n*0.264, " gallons")
elif m==3:
  print(n, "° celcuius is ", n*1.8+32, "° fahrenheit")
elif m==4:
  print(n, " years are ", n*0.2, " lustrum")
else:
  print(n, " hours are ", n*60, " minutes")
