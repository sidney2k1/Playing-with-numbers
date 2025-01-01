#Take input from the user
number=int(input("Enter a number :"))
#store the original number for comparison later 
originalnumber=number
reversednumber=0
while number>0:
    digit=number%10
    reversednumber=reversednumber*10+digit
    number//=10
if originalnumber==reversednumber:
    print(f"{originalnumber} is a palindrome")
else:
    print(f"{originalnumber} is not a palindrome")