# program to display the Hollow Full Pyramid

r=int(input("Enter the number of rows: ")) # user input for number of rows in the pyramid

# code to display the element of pyramid for length (row - 1)
for i in range(1,r):
    for j in range(i,r):
        print(" ",end=" ")
    for k in range(1,(2*i)):
        if (i != 1) and ( k == 1) or (k == (2*i)-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")

# code to print the last row of the hollow pyramid
for i in range(0,2*r-1):
    if i%2==0:
        print("*",end=" ")
    else:
        print(" ",end=" ")

    