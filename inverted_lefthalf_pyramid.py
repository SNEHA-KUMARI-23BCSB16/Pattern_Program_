# program to display inverted left half pyramid

r=int(input("Enter the number of row you want to print in pyramid:")) # taking user input

# method 1 iterating both loop for same range i.e. till rows and comparing the loop value and then displaying the result
for i in range(1,r+1): 
    for j in range(1,r+1):
        if(j >= i):
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print("")

# method 2 iterarting first loop for number of rows and second loop upto the value of first loop and displaying the result
for i in range(1,r+1):
    for j in range(1,i):
        print("  ",end=" ")
    for k in range(i,r+1):
        print("* ", end=" ")
    print("")
