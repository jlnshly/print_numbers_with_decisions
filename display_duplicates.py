#Ask user for input
#Assign variable
#Set decision
number_list = []
for i in range (1, 11):
    user_input = float(input("Enter a number: "))
    number_list.append(user_input)
duplicate_list = []
for user_input in number_list:
    if number_list.count(user_input) >= 2:
        duplicate_list.append(user_input)
        print(user_input)
