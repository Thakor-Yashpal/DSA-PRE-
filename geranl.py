s = "deep learing"

print(s[::-1])



# def is_prime(n):
#     if n < 2: return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0: return False
#     return True


# def is_prime(n):
#     if n < 2 :return False
#     for i in range(2, int(5 **n)+1):
#         if n % i  == 0 : return False
#     return True
        



# def factorial(n1):
#     if n1 == 0 or n1 == 1:
#         return 1
#     else:
#         return n1 * factorial(n1 - 1)

# # Example usage
# print(factorial(10))


string = " can you pleace give me the coffee besuse  my code is not working on this computer, what if we have the numbers1,2,3,4,5,6,7,8,9,10"

char_count = {}

has_digit = True or False

for char in string:
    char_count[char] = char_count.get(char,0) + 1
    
    if char.isdigit():
        has_digit = True
    else:
        has_digit = False
        

for char, count in char_count.items():
    if count > 1:
        print(f"Character '{char}' appears {count} times.")

if has_digit:
    print("The string contains one or more digits:",has_digit)
else:
    print("The string does not contain any digits:",has_digit)
