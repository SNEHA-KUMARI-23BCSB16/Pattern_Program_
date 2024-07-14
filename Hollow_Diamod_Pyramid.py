# program to display the Hollow Diamond Pyramid

r=int(input("Enter the number of rows for upper half of diamond pyramid: ")) # user input for the diamond ppattern


# code to display the upper part of hollow diamond pyramid
for i in range(1,r+1):
    for j in range(i,r):
        print(" ",end=" ")
    for k in range(1,(2*i)):
        if ( k == 1) or (k == (2*i)-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")

# code to display the lower half of the hollow diamond pyramid
for i in range(1,r):
    for j in range(i):
        print(" ",end=" ")
    for k in range(1,(2*r-2*i)):
        if k==1 or k == (2*r - 2*i) -1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("") 

