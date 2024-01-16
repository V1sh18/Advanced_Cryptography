def add_mod_p(a, b, p):
    return (a + b) % p

def subtract_mod_p(a, b, p):
    return (a - b) % p

def multiply_mod_p(a, b, p):
    return (a * b) % p

def inverse_mod_p(a, p):
    # Calculate the modular inverse using extended Euclidean algorithm
    _, inv, _ = extended_gcd(a, p)
    if inv < 0:
        inv += p  # Ensure the result is non-negative
    return inv

def divide_mod_p(a, b, p):
    # Check for division by zero
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    
    # Calculate the modular inverse of b
    inv_b = inverse_mod_p(b, p)

    # Perform division as multiplication by the modular inverse
    return multiply_mod_p(a, inv_b, p)

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

# Get prime modulus from the user
p = int(input("Enter the prime modulus (p): "))

# Get input elements from the user
element1 = int(input("Enter the first element in GF(p): "))
element2 = int(input("Enter the second element in GF(p): "))

# Perform arithmetic operations
result_add = add_mod_p(element1, element2, p)
result_subtract = subtract_mod_p(element1, element2, p)
result_multiply = multiply_mod_p(element1, element2, p)

try:
    result_divide = divide_mod_p(element1, element2, p)
except ValueError as e:
    result_divide = str(e)

# Display results
print(f"Addition: {element1} + {element2} = {result_add}")
print(f"Subtraction: {element1} - {element2} = {result_subtract}")
print(f"Multiplication: {element1} * {element2} = {result_multiply}")
print(f"Division: {element1} / {element2} = {result_divide} (mod {p})")

