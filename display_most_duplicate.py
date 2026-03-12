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
duplicate_count = 0
most_duplicates = None
for user_input in numbers:
    counter = numbers.count(user_input)
    if counter > duplicate_count:
        most_duplicates = user_input
        duplicate_count = counter
print(most_duplicates)


