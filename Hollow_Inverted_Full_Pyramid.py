# program to display the Hollow_Inverted_Full_Pyramid

r=int(input("Enter the number of rows: ")) # taking row as input from user

# code to display the first line of pyramid
for i in range(0,2*r-1):
    if i%2==0:
        print("*",end=" ")
    else:
        print(" ",end=" ")
print("")

# code to display the rows other than the first row of pyramid
for i in range(1,r):
    for j in range(i):
        print(" ",end=" ")
    for k in range(1,(2*r-2*i)):
        if k==1 or k == (2*r - 2*i) -1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("") 


