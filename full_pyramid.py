# program to display FUll Pyramid using special character "*"

r=int(input("Enter the number of row you want to print in pyramid:")) # taking user input for pyramid length

for i in range(1,r+1): # iterating through the length i.e., for row of pyramid
    for j in range(r,i,-1): # iterating in each row to print the required spaces
        print(" ",end=" ")
    for k in range(1,(2*i)+1): # iterating in each row to display the special character
        if ( k%2 == 1 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
        