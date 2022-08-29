import random
import string

total_chars = string.printable
password = ''
num_chars = 0
while num_chars <= 0 or num_chars >= 17:
    num_chars = int(input('How many characters?(1 - 16)'))
    if num_chars <= 0 or num_chars >= 17:
        print('1 - 16 characters only bitch')

pass_strength = 0
while pass_strength != 1 and pass_strength != 2 and pass_strength != 3 and pass_strength != 4:
    pass_strength = int(input('What password strength?\n1. Basic(numbers only)\n2. Weak(letters only)\n3. Medium(letters and numbers)\n4. Strong(letters, numbers & special characters)\n'))
    if pass_strength != 1 and pass_strength != 2 and pass_strength != 3 and pass_strength != 4:
        print('Can you read bitch? 1, 2, 3, or 4 only')

current_char = 0
match pass_strength:
    # nums only
    case 1:
        while (current_char < num_chars):
            randIndex = random.randint(0, 9)
            password = password + total_chars[randIndex]
            current_char += 1
    # letters only
    case 2:
        while (current_char < num_chars):
            randIndex = random.randint(10, 62)
            password = password + total_chars[randIndex]
            current_char += 1
    # letters and numbers
    case 3:
        while (current_char < num_chars):
            randIndex = random.randint(0, 62)
            password = password + total_chars[randIndex]
            current_char += 1
    # letters, numbers, and special characters
    case 4:
        while (current_char < num_chars):
            randIndex = random.randint(0, len(total_chars))
            password = password + total_chars[randIndex]
            current_char += 1

print(password)
