# 1. Think about type conversion and come up with ideas!
import json
from collections import namedtuple
# importing "cmath" for complex number operations
import cmath

# 1. Automatic (Implicit) Conversion: Combining an int and a float
int_value = 10
float_value = 5.5
result = int_value + float_value  # Automatically converts int to float
print(f"Implicit Conversion (int + float): {result}")  # Output: 15.5 (float)

# 2. Explicit Conversion (Casting): Converting a string to int
age_str = "21"
age_int = int(age_str)  # Explicit conversion from string to int
print(f"Explicit Conversion (str to int): {age_int}")  # Output: 21 (int)

# 3. Custom Type Conversion: Defining a custom class with conversion methods
class Person:
    def __init__(self, age):
        self.age = age
    
    def __int__(self):  # Custom int conversion
        return self.age
    
p = Person(30)
print(f"Custom Conversion (__int__): {int(p)}")  # Output: 30 (int)

# 4. Converting Between Mutable and Immutable Types: List to Tuple and back
my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # List to tuple
print(f"List to Tuple: {my_tuple}")  # Output: (1, 2, 3)

my_new_list = list(my_tuple)  # Tuple back to list
print(f"Tuple to List: {my_new_list}")  # Output: [1, 2, 3]

# 5. Chained Conversion: Converting a string to float and then to int
num_str = "10.75"
num_int = int(float(num_str))  # First convert to float, then to int
print(f"Chained Conversion (str to float to int): {num_int}")  # Output: 10

# 6. JSON Conversion (Serialization): Converting dict to JSON string and back
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)  # Convert to JSON string
print(f"Dictionary to JSON: {json_str}")  # Output: JSON string of the dict

python_dict = json.loads(json_str)  # Convert JSON string back to dict
print(f"JSON to Dictionary: {python_dict}")  # Output: {'name': 'Alice', 'age': 25}

# 7. Complex Type Conversion: Convert dict to namedtuple
PersonTuple = namedtuple("PersonTuple", ["name", "age"])
person_dict = {"name": "Bob", "age": 28}
person_namedtuple = PersonTuple(**person_dict)  # Convert dict to namedtuple
print(f"Dictionary to NamedTuple: {person_namedtuple}")  # Output: PersonTuple(name='Bob', age=28)

# 8. Handling Conversion Errors: Safe conversion with try-except
invalid_str = "not_a_number"
try:
    num = int(invalid_str)  # Attempt to convert an invalid string to int
except ValueError:
    print(f"Conversion failed for value: '{invalid_str}'")  # Handles conversion error


# 2. Extract imaginary and real part of a complex number
# Extract imaginary and real part of a complex number
# Python code to demonstrate the working of complex(), real() and imag()
# https://www.geeksforgeeks.org/complex-numbers-in-python-set-1-introduction/

# Initializing real numbers
x = 5
y = 3

# converting x and y into complex number
z = complex(x, y)
# Initializing complex number alternatively
# z = 5+3i

# printing real and imaginary part of complex number
print("The real part of complex number is:", z.real)
print("The imaginary part of complex number is:", z.imag)

# 3. Arithmetic Operations on complex numbers
# Addition: For addition of complex numbers, one can write (a + ib) + (c + id) = (a + c) + i(b + d).
# Subtraction: For subtraction of complex numbers, one can write (a + ib) – (c + id) = (a – c) + i(b – d).
# Multiplication: For multiplication of complex numbers,we can write (a + ib). (c + id) = (ac – bd) + i(ad + bc).
# Division: For division of complex numbers, write (a + ib) / (c + id) = (ac + bd)/ (c2 + d2) + i(bc – ad) / (c2 + d2)

# Define two complex numbers
z1 = 3 + 4j
z2 = 1 - 2j

# Addition
add_result = z1 + z2
print(f"Addition: {z1} + {z2} = {add_result}")  # Output: (3+4j) + (1-2j) = (4+2j)

# Subtraction
sub_result = z1 - z2
print(f"Subtraction: {z1} - {z2} = {sub_result}")  # Output: (3+4j) - (1-2j) = (2+6j)

# Multiplication
mul_result = z1 * z2
print(f"Multiplication: {z1} * {z2} = {mul_result}")  # Output: (3+4j) * (1-2j) = (11-2j)

# Division
div_result = z1 / z2
print(f"Division: {z1} / {z2} = {div_result}")  # Output: (3+4j) / (1-2j) = (-1.4+1.6j)

# Absolute value (magnitude/ modulus)
abs_result = abs(z1)
print(f"Absolute value (magnitude) of {z1} = {abs_result}")  # Output: 5.0


