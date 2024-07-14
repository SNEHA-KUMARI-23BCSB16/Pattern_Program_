# program to print the Hollow Hourglass Pyramid


r=int(input("Enter the number of rows for upper half of Hourglass: ")) # taking user input

# code to display first line of Hourglass
for i in range(0,2*r-1):
    if i%2==0:
        print("*",end=" ")
    else:
        print(" ",end=" ")
print("")

# code to display the upper half of hourglass pyramid 
for i in range(r-1,0,-1):
    for k in range(r,i,-1):
        print(" ",end=" ")
    for j in range((2*i)+1,1,-1):
        if (i!=1) and (j==(2*i)+1) or (j==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")

# code to display the lower half of hourglass pyramid
for i in range(2,r):
    for j in range(r,i,-1):
        print(" ",end=" ")
    for k in range(1,(2*i)+1):
        if (i!=1) and (k==1) or (k == 2*i-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")

# code to display last line of hourglass
for i in range(1,2*r):
    if i%2!=0:
        print("*",end=" ")
    else:
        print(" ",end=" ")

