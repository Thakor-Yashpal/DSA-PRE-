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
        



def factorial(n1):
    if n1 == 0 or n1 == 1:
        return 1
    else:
        return n1 * factorial(n1 - 1)

# Example usage
print(factorial(10))
