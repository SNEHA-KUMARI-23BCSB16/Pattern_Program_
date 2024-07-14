# program to display rhombus pattern

r=int(input("Enter the number of rows you want to display: ")) # taking user input

for i in range(1,r+1):
    print(" "*i,end=" ")
    for j in range(r):
        print("* ",end=" ")
    print("")
    

