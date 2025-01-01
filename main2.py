numberlargest=int(input("Enter a larger number:"))
numbersmallest=int(input("Enter the smaller number:"))
while(numbersmallest):
    numberstore=numbersmallest
    numbersmallest=numberlargest%numbersmallest
    numberlargest=numberstore
print("HCF is",numberlargest)