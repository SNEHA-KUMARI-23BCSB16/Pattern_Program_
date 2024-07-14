# program to display Pascal_Triangle


from math import factorial # calling factorial method from in built package

r=int(input("Enter the number of rows:")) # taking user input


for i in range(r):
    for j in range(r-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ") # calculating and displaying the factorial
    print("")
