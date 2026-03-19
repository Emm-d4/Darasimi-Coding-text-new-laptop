dec = int (input("enter a number to find it's binary value: ") )

#using loop
binary_result = ""

while dec > 0:
    remainder = dec % 2
    dec = dec // 2
    binary_result = str(remainder) + binary_result

print(binary_result)