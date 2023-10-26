'''https://replit.com/join/csnwjlqvvn-a00573910'''

mini=101
maxi=0
avg=0
cntp=0
cntf=0

print("Student grades analisis\n")
n=int(input("Enter the number of students:\n"))

for i in range(n):
  x=int(input("Enter the grade of student: "))
  if(x>maxi):
    maxi=x
  if(x<mini):
    mini=x
  avg+=x
  if(x>=60):
    cntp+=1
  else:
    cntf+=1

print("The avarage grade is: ", avg/n)
print("The highest grade is: ", maxi)
print("The lowest grade is: ", mini)
print("Students that passed: ", cntp)
print("Students that failed: ", cntf)
