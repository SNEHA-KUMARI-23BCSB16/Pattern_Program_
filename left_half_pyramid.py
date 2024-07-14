# program to display left half pyramid

r=int(input("Enter the number of column you want to print in pyramid:")) # taking user input

# code to display left half pyramid
for i in range(r,0,-1):
    for k in range(0,i):
        print("  ",end=" ")
    for j in range(i,r+1):
            print("* ", end=" ")
    print("")