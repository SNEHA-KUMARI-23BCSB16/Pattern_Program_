# program to display the Hourglass Pattern

r=int(input("Enter the number of row in first half of hour glass: ")) # taking user input

# code to display upper half of hourglass
for i in range(r,0,-1):
    for k in range(r,i,-1):
        print(" ",end=" ")
    for j in range((2*i)+1,1,-1):
        if ( j%2 == 1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")

# code to display lower half of hourglass    
for i in range(2,r+1):
    for j in range(r,i,-1):
        print(" ",end=" ")
    for k in range(1,(2*i)+1):
        if ( k%2 == 1 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")

      