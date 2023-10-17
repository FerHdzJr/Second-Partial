'''https://replit.com/join/hbgyehlwsi-a00573910'''

n=int(input("Enter the purchase amount: "))
s=input("Do you have a membership card?\n")
card=False
d1=0
d2=0
s=s.upper()
if s=="YES":
  card=True

if n>=100:
  print("Since your product costs more than $99.99 you receive a 10%")
  print("discount")
  d1=0.1
if card:
  print("You receive a membership discount of 5%")
  d2=0.05

if d1==0 and d2==0:
  print("You have no discounts available")
print(" ")
print("The final price is: $", n-d1*n-d2*n)
