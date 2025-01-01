def hcf(numbersmallest,numberlargest):
    while(numbersmallest):
        numberstore=numbersmallest
        numbersmallest=numberlargest%numbersmallest
        numberlargest=numberstore
    return numberlargest
numberlargest=int(input("Enter a number:"))
numbersmallest=int(input("Enter a number smaller than the other"))
lcm=int((numbersmallest/hcf(numbersmallest,numberlargest))*numberlargest)
print("the lcm of the numbers are:",lcm)