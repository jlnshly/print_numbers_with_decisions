#Ask user for input
#Assign variable
#Set loop
#Set decisions
numbers = []
while True:
    try:
        user_input = float(input("Enter a number: "))
        numbers.append(user_input)
    except ValueError:
        break
highest_number = max(numbers)
print(highest_number)


