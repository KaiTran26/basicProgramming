n = int(input("Number: ")) #takes the number and stores it in n
factorial = 1 #creates a global variable

for number in range(0 , n + 1): #loops for every number
    factorial *= number #multiplies number by the product of previous numbers

print("The factorial of" , n , "is :", factorial) #outputs the answer
