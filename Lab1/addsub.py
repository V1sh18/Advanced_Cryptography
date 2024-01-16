def add_mod_p(a, b, p):
    return (a + b) % p

def multiply_mod_p(a, b, p):
    return (a * b) % p

# Get prime modulus from the user
p = int(input("Enter the prime modulus (p): "))

# Get input elements from the user
element1 = int(input("Enter the first element in GF(p): "))
element2 = int(input("Enter the second element in GF(p): "))

# Perform addition and multiplication
result_add = add_mod_p(element1, element2, p)
result_multiply = multiply_mod_p(element1, element2, p)

# Display results
print(f"Addition: {element1} + {element2} = {result_add} (mod {p})")
print(f"Multiplication: {element1} * {element2} = {result_multiply} (mod {p})")

