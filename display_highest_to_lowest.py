#Ask user input
#Set a loop
#Set the conditions to find lowest number
number_list = []
while True:
    try:
        user_input = float(input("Enter a number: "))
        number_list.append(user_input)
    except ValueError:
        break
if number_list:
    sorted_list = sorted(number_list)
    sorted_list.sort(reverse=True)
print(sorted_list)

