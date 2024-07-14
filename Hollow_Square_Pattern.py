# program to print Hollow Square Pattern

r=int(input("Enter the number of rows you want to print in square: ")) # taking input from user

# code to display a hollow square pattern
for i in range(1,r+1):
    if (i == 1) or (i == r): # checking for the first and last row of square o print the whole row
        for j in range(1,r+1):
            print("*",end=" ")
    else:
        for j in range(1,r+1): 
            if (j == 1) or (j == r): # checking for first and last column of square to print the pattern
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print("")