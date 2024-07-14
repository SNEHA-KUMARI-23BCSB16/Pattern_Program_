# program to display inverted right half pyramid

r=int(input("Enter the number of row you want to print in pyramid:")) # user input

# METHOD 1
for i in range(r,0,-1):
    for j in range(1,i+1):
        if( j <= i):
            print(" *", end=" ")
        else:
            print("  ",end=" ")
    print("")

# METHOD 2
for i in range(1,r+1):
    for j in range(i,r+1):
        print("* ",end=" ")
    print("")