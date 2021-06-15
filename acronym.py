# give short describtion for the game
print(f'Hi, Tell me the full name and I will surprise you with  the Acronym ^_^')

# ask the user to enter full name of oranization or concept 
full_name = input('please enter the full meaning of the organization or concept ?\n')

# convert the input into list
full_name_list = full_name.split()
print(full_name_list)

# iterate over the string list and print the first letter of each word

for word in full_name_list:
    first_character = word[0]
        

# print the result in uppercase form and tell it to the user 
Acronym = ''. join(first_character)
print(Acronym)

# ask the user to run it again or exit
