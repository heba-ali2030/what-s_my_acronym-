# give short describtion for the game
print(f'Hi, Tell me the full name and I will surprise you with  the Acronym ^_^')

# ask the user to enter full name of oranization or concept 
full_name = input('please enter the full meaning of the organization or concept ?\n')

# convert the input into list
full_name_new = full_name.split(' ')


# iterate over the string list and print the first letter of each word

first_word = full_name_new[:-1]
last_word = full_name_new [-1]
acronym = ''
for letter in first_word:
    acronym = acronym + letter[0] 
acronym = acronym + last_word[0]

# print the result in uppercase form and tell it to the user 
print(F'The Acronym of {full_name} is {acronym.upper()}')


