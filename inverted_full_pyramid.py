# program to display the inverted full pyramid


r=int(input("Enter the number of row you want to print in pyramid:")) # taking user input

# using two inner loop and iterating loop in backward direction
for i in range(r,0,-1):
    for k in range(r,i,-1):
        print(" ",end=" ")
    for j in range((2*i)+1,1,-1):
        if ( j%2 == 1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")  