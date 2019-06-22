#we are asking for a number and then will answer whether or not the number is a prime user_number

# first we need to make sure the entry is a positive, whole number
def get_user_num(prompt):
    try:
        value = int(input(prompt))
    except ValueError:
        print("That was not a whole number, try again.")
        return get_user_num(prompt)
    if value < 0:
        print("Sorry your response must not be negative, try again.")
        return get_user_num(prompt)
    else:
        print("You entered: " + str(value))
        return value

# now that we have a whole number, we can see if it's a prime number or not
def is_prime(value):
    divisor = value - 1
    while divisor > 1:
        if value % divisor == 0:
            return "Nope, not a prime number"
            break
        divisor -= 1
    return 'Congrats! You found the prime number: ' + str(value)

user_num = get_user_num("Gimme a whole number & I'll tell you if it's a prime number or not: ")
print(is_prime(user_num))
