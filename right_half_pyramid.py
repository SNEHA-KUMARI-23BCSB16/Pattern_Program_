# to display * as a right half pyramid

r=int(input("Enter the number of row you want to print in pyramid:")) # user input

for i in range(0,r):
    for j in range(0,i+1):
        print( "* ", end=" " )
    print("")