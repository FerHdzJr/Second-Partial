"""https://replit.com/join/gmospirtev-a00573910"""

age=int(input("Please introduce your age: "))
weight=float(input("Please introduce your weight: "))
height=float(input("Please introduce your height: "))
act=input("What level of physical activity do you have? [sedentary, moderate, active]\n")
act=act.lower()
bmi=weight/(height*height)

if age<=18:
  print("We recommend a high carbohydrate diet.")
elif age>18 and age<35:
  print("We recommend a high protein and lower carbohydrate diet.")
else:
  print("We recommend a low sugar diet.")

if age>=18 and age<=30:
  if act=="sedentary" or act=="moderate":
    print("You need aerobic exercises.")

if bmi<18 and act=="sedentary":
  print("You need to consult a nutritionist and increase your physical activity.")
if bmi>=18 and bmi<25:
  if act=="moderate" or act=="active":
    print("You are in good condition.")

if bmi>=25 and act=="sedentary":
  print("You need to consult a nutritionist, increase physical activity,")
  print("and reduce your weight.")
