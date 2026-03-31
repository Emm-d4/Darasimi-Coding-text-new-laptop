#define function to calculate cube
def cube(number):
    return number * number * number

#define a function which will execute cube function if the user entered nunmber divisible by 3
def by_three(num):
    if num % 3 == 0:
        return cube(num) #calling function cube()
    else:
        return False

X = 9
y = 4

#display result
result1 = by_three(X) #passing argument x
result2 = by_three(y) #passing argument y

print(result1)
print(result2)