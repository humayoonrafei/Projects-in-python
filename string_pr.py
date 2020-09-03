def common_letters(string_one,string_two):
  new_list=[]
  for i in string_one:
    if i in string_two:
      if not i in new_list:
        new_list.append(i)
  return new_list

print (common_letters("manhattan","sanfrancisco"))


def username_generator(first_name,last_name):
  username=first_name[:3]+last_name[:4]
  return username
# #
# Copeland’s Corporate Company has finalized what they want to their username and temporary password creation to be and have enlisted your help, once again, to build the function to generate them. In this exercise, you will create two functions, username_generator and password_generator.

# Let’s start with username_generator. Create a function called username_generator take two inputs, first_name and last_name and returns a username. The username should be a slice of the first three letters of their first name and the first four letters of their last name. If their first name is less than three letters or their last name is less than four letters it should use their entire names.

# For example, if the employee’s name is Abe Simpson the function should generate the username AbeSimp.

# Checkpoint 2 Passed
# 2.
# Great work! Now for the temporary password, they want the function to take the input user name and shift all of the letters by one to the right, so the last letter of the username ends up as the first letter and so forth. For example, if the username is AbeSimp, then the temporary password generated should be pAbeSim.

# Start by defining the function password_generator so that it takes one input, username and in it define an empty string named password.

# Checkpoint 3 Passed
# 3.
# Inside password_generator create a for loop that iterates through the indices username by going from 0 to len(username).

# To shift the letters right, at each letter the for loop should add the previous letter to the string password.
#
def password_generator(username):
  password=""
  for i in range(len(username)): # range here means to loop as many times for example range(5) means loop five times however here it loops with length of the username.
    password += username[i-1]  # here we add the alphabet from back such as the first one would be [0-1] is [-1] which is the last alphatbit and it will placed in the zeroth place in the new string
  return password

                                      ### my comments ###
# .split will be splitting a string into words

line_one = "The sky has given over"
line_one_words=line_one.split()

print(line_one_words)

# when removing all white spaces through a loop
# deeply look to the love_maybe_lines it has comma so it means different items . thus we loop on each item to be stripped .
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms',
                    '           like flowering mines    ', '\n', '   to conquer me home.    ']

love_maybe_lines_stripped = []

for i in love_maybe_lines:
  love_maybe_lines_stripped.append(i.strip())

love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_lines_stripped)