# program to display diamond pattern

r=int(input("Enter the number of rows you want in the diamond pattern: ")) # Taking the row number input from user

for i in range(0,(r//2)+1): # iterating through first half of row to display upper triangle of diamond
    for j in range((r//2),i,-1): # iterating in each line to print space
        print(" ",end=" ")
    for k in range(0,(2*i)+1): # iterating to print "*" in each line along with space
        if ( k%2 == 0):
            print("* ",end=" ")
        else:
            print(" ",end=" ")
    print("")
for i in range((r//2)+1,1,-1): # iterating in next half of row to display lower half
    for j in range((r//2)+1,i,-1): # iterating to print spaces 
        print(" ",end=" ")
    for k in range(1,(2*i)): # iterating to display the pattern "*" along with spaces
        if (k%2 == 0):
            print("* ",end=" ")
        else:
            print(" ",end=" ")
    print("")
           