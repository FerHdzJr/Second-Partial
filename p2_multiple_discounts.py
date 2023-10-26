'''https://replit.com/join/ltcbdyjnbq-a00573910'''

print("---Price calculartor---\n")
x=int(input("Enter the price of your product:\n"))
cnt=int(input("Enter the number of purchased units: \n"))
cat=input("Enter the cathegory of the product: [A, B, C]\n")
total=cnt*x
print("Total cost before discount: ", cnt*x)
dis=0
if cat=="A":
  print("Discount applied: 10%")
  dis=0.1
elif cat=="B":
  print("Discount applied: 5%")
  dis=0.05
else:
  print("Discount applied: 2%")
  dis=0.02
if cnt>10:
  print("Additional discount (more than 10 units): 5%")
  print("Final cost is: ", total-total*dis-total*0.05)
else:
  print("Final cost is: ", total-total*dis)
