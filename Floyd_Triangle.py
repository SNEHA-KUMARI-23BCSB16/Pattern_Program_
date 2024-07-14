# program to display Floyd's Triangle 


num=int(input("Enter the number of rows upto which you want to print the Floyd's Triangle:")) # input the triangle length from user

k=1 # counter variable to update the value of triangle

for i in range(1,num+1): # iterarting for number of rows in triangle
    for j in range(i): # iterating for number of values n each row of triangle
        print(k,end=" ")
        k += 1
    print("")